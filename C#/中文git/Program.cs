using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace DuckStudio.ChineseGit
{
    public class Program
    {
        // 获取程序路径
        public static readonly string ScriptPath = Path.GetDirectoryName(Environment.GetCommandLineArgs()[0]);

        // 中文Git完整路径
        public static readonly string FullPath = Path.Combine(ScriptPath, "中文git.exe");

        // 定义版本号
        public const string Version = "v2.9.2-pack";

        // 配置文件路径
        public static readonly string configFile = Path.Combine(Path.GetDirectoryName(System.Reflection.Assembly.GetEntryAssembly().Location), "config.json");

        static void Main()
        {
            Environment.ExitCode = 0;
            bool autoCheckUpdate;
            bool autoGetNotice;

            if (File.Exists(configFile))
            {
                try
                {
                    // 读取配置文件内容并反序列化为对象
                    string configJson = File.ReadAllText(configFile);
                    var configData = JsonConvert.DeserializeObject<ConfigData>(configJson);

                    // 获取自动检查更新和自动获取通知的设置
                    autoCheckUpdate = bool.Parse(configData.Application.Run.AutoCheckUpdate);
                    autoGetNotice = bool.Parse(configData.Application.Run.AutoGetNotice);
                }
                catch (Exception e)
                {
                    // 如果读取或解析配置文件出错，设置默认值并显示错误信息
                    autoCheckUpdate = true;
                    autoGetNotice = true;
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"✕ 读取配置文件时出错:\n{e}\n[!] 请检查配置文件是否正确，您可以先删除配置文件然后运行应用以重新生成默认配置。");
                    Console.ResetColor();
                    Environment.ExitCode = 1;
                    return;
                }
            }
            else
            {
                // 如果配置文件不存在，则使用默认设置
                autoCheckUpdate = true;
                autoGetNotice = true;
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("⚠ 没有找到配置文件，将生成默认配置文件！");
                Console.ResetColor();

                try
                {
                    // 创建默认配置对象
                    var defaultConfig = new ConfigData
                    {
                        Information = new Information { Version = "v2.9" },
                        Application = new Application
                        {
                            Notice = new Notice { Time = "", Level = "", Content = "" },
                            Run = new Run { AutoCheckUpdate = "True", AutoGetNotice = "True" }
                        }
                    };

                    // 将默认配置对象序列化为 JSON 字符串
                    string jsonStr = JsonConvert.SerializeObject(defaultConfig, Formatting.Indented);

                    // 将 JSON 字符串写入配置文件
                    File.WriteAllText(configFile, jsonStr);
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("✓ 默认配置文件生成成功");
                    Console.ResetColor();
                }
                catch (Exception e)
                {
                    // 如果生成默认配置文件时出现错误，显示错误信息
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"✕ 生成默认配置文件时出错！请手动添加配置文件，否则某些功能可能无法正常运行！");
                    Console.WriteLine($"错误信息: {e}");
                    Console.ResetColor();
                    Environment.ExitCode = 1;
                    return;
                }
            }

            // 执行其他操作
            Console.WriteLine("继续执行其他操作...");
            Console.ReadKey();
        }

        // 定义用于反序列化 JSON 的类结构
        public class ConfigData
        {
            public Information Information { get; set; }
            public Application Application { get; set; }
        }

        public class Information
        {
            public string Version { get; set; }
        }

        public class Application
        {
            public Notice Notice { get; set; }
            public Run Run { get; set; }
        }

        public class Notice
        {
            public string Time { get; set; }
            public string Level { get; set; }
            public string Content { get; set; }
        }

        public class Run
        {
            public string AutoCheckUpdate { get; set; }
            public string AutoGetNotice { get; set; }
        }

        public static async Task<object> FetchJsonAsync()
        {
            string configUrl = "https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/files/json/config.json";
            HttpClient httpClient = new();
            httpClient.DefaultRequestHeaders.UserAgent.ParseAdd("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36");

            try
            {
                HttpResponseMessage response = await httpClient.GetAsync(configUrl);

                if (response.IsSuccessStatusCode)
                {
                    string jsonResponse = await response.Content.ReadAsStringAsync();
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("✓ 获取最新默认配置文件成功");
                    Console.ResetColor();
                    return JsonConvert.DeserializeObject<object>(jsonResponse);
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"✕ 无法获取最新默认配置文件");
                    Console.ForegroundColor = ConsoleColor.Blue;
                    Console.WriteLine($"[!] 返回状态码: {response.StatusCode}");
                    Console.ResetColor();
                    Environment.ExitCode = 1;
                    return null;
                }
            }
            catch (Exception e)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"✕ 尝试获取最新默认配置文件失败，错误: {e.Message}");
                Console.ResetColor();
                Environment.ExitCode = 1;
                return null;
            }
            finally
            {
                httpClient.Dispose();
            }
        }

        public static Dictionary<string, object> MergeJson(Dictionary<string, object> oldJson, Dictionary<string, object> newJson)
        {
            var updatedJson = new Dictionary<string, object>(oldJson);

            // 处理旧 JSON 中的键
            var keysToRemove = new List<string>();
            foreach (var key in updatedJson.Keys)
            {
                if (!newJson.ContainsKey(key))
                {
                    keysToRemove.Add(key);
                }
            }

            foreach (var key in keysToRemove)
            {
                updatedJson.Remove(key);
            }

            // 合并新 JSON 中的值
            foreach (var kvp in newJson)
            {
                if (updatedJson.TryGetValue(kvp.Key, out var existingValue) && existingValue is Dictionary<string, object> existingDict && kvp.Value is Dictionary<string, object> newDict)
                {
                    // 如果是字典类型，递归合并
                    updatedJson[kvp.Key] = MergeJson(existingDict, newDict);
                }
                else
                {
                    // 直接更新值
                    updatedJson[kvp.Key] = kvp.Value;
                }
            }

            return updatedJson;
        }

        public static async Task<int> UpdateJsonAsync()
        {
            try
            {
                // 获取最新的 JSON 数据
                object result = await FetchJsonAsync();
                if (result == null)
                {
                    return 1;
                }

                // 读取旧的 JSON 数据
                string oldJsonString = File.ReadAllText(configFile);
                var oldJson = JsonConvert.DeserializeObject<Dictionary<string, object>>(oldJsonString);

                // 合并 JSON 数据
                var newJson = (Dictionary<string, object>)result;
                var updatedJson = MergeJson(oldJson, newJson);

                // 将更新后的 JSON 数据写入文件
                string updatedJsonString = JsonConvert.SerializeObject(updatedJson, Formatting.Indented);
                File.WriteAllText(configFile, updatedJsonString);

                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("✓ 默认配置文件更新成功");
                Console.ResetColor();
                return 0;
            }
            catch (Exception e)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"✕ 更新配置文件时出错:\n{e}");
                Console.ResetColor();
                Environment.ExitCode = 1;
                return 1;
            }
        }
    }
}

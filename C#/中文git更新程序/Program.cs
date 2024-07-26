using System;
using System.ComponentModel;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string version = ParseCommandLineArguments(args); // 解析命令行参数获取版本号
        if (version == null)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("✕ 未指定版本号。请使用 --version <VERSION> 指定版本号。");
            Console.ResetColor();
            Environment.ExitCode = 1;
            Console.WriteLine("按任意键退出...");
            Console.ReadKey();
            return; // 退出程序
        }

        string newFilename = await DownloadUpdateFile(version);
        if (newFilename != null)
        {
            Environment.ExitCode = 0;
            ReplaceCurrentProgram(newFilename);
        }
        else
        {
            Environment.ExitCode = 1;
        }

        Console.WriteLine("按任意键退出...");
        Console.ReadKey();
    }

    static string ParseCommandLineArguments(string[] args)
    {
        for (int i = 0; i < args.Length; i++)
        {
            if (args[i] == "--version" && i + 1 < args.Length)
            {
                return args[i + 1];
            }
        }
        return null;
    }

    static async Task<string?> DownloadUpdateFile(string version)
    {
        string downloadUrl = $"https://github.com/DuckDuckStudio/Chinese_git/releases/download/{version}/Chinese_git.exe";
        string newFilename = "中文git.exe";

        using (HttpClient client = new HttpClient())
        {
            try
            {
                HttpResponseMessage response = await client.GetAsync(downloadUrl);
                if (response.IsSuccessStatusCode)
                {
                    using (Stream contentStream = await response.Content.ReadAsStreamAsync(),
                                 fileStream = new FileStream(newFilename, FileMode.Create, FileAccess.Write, FileShare.None))
                    {
                        await contentStream.CopyToAsync(fileStream);
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine("✓ 更新成功下载。");
                        Console.ResetColor();
                        return newFilename;
                    }
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"✕ 下载更新文件时出错: {response.StatusCode}");
                    Console.ResetColor();
                    return null;
                }
            }
            catch (Exception e)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"✕ 下载更新文件时出错: {e.Message}");
                Console.ResetColor();
                return null;
            }
        }
    }

    static void ReplaceCurrentProgram(string newFilename)
    {
        try
        {
            string currentPath = System.Reflection.Assembly.GetExecutingAssembly().Location;
            string currentDir = Path.GetDirectoryName(currentPath);
            // Path.GetDirectoryName() = os.path.dirname()

            string newFilePath = Path.Combine(currentDir, "中文git.exe");
            // Path.Combine() = os.path.join()

            File.Replace(newFilename, newFilePath, null);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("✓ 程序已成功更新。");
            Console.ResetColor();
        }
        catch (Exception e)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine($"✕ 替换当前程序时出错: {e.Message}");
            Console.ResetColor();
            Environment.ExitCode = 1;
        }
    }
}

import os
import sys
import json
import requests
import subprocess
from colorama import init, Fore

init(autoreset=True)
script_path = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(script_path, "中文git.py")
exit_code = 0 # 只有不正常退出需要定义

# ---------- 版本定义及更新 ----------
# 定义版本号
VERSION = 'v3.2'
# GitHub releases API URL
url = 'https://api.github.com/repos/DuckDuckStudio/Chinese_git/releases/latest'

# --- 读取配置文件 ---
def fetch_json():
    global exit_code
    config_url = "https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/files/json/config.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(config_url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            print(f"{Fore.GREEN}✓{Fore.RESET} 获取最新默认配置文件成功")
            return json_data
        else:
            print(f"{Fore.RED}✕{Fore.RESET} 无法获取最新默认配置文件\n{Fore.BLUE}[!]{Fore.RESET} 返回状态码: {Fore.YELLOW}{response.status_code}{Fore.RESET}")
            exit_code = 1
            return None
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 尝试获取最新默认配置文件失败，错误: {Fore.RED}{e}{Fore.RESET}")
        exit_code = 1
        return None
    
def merge_json(old_json, new_json):
    # 合并两个 JSON 对象
    updated_json = old_json.copy()
    
    # 处理旧 JSON 中的键
    keys_to_remove = []
    for key in updated_json:
        if key not in new_json:
            keys_to_remove.append(key)
    
    for key in keys_to_remove:
        del updated_json[key]
    
    # 合并新 JSON 中的值
    for key in new_json:
        if key in updated_json and isinstance(updated_json[key], dict) and isinstance(new_json[key], dict):
            # 如果是字典类型，递归合并
            updated_json[key] = merge_json(updated_json[key], new_json[key])
        else:
            # 直接更新值
            updated_json[key] = new_json[key]
    
    return updated_json

def update_json():
    global exit_code
    new_json = fetch_json()
    if not new_json:
        return 1
    try:
        with open(config_file, 'r') as f:
            old_json = json.load(f)
        
        updated_json = merge_json(old_json, new_json)
        
        # 将更新后的配置写入文件
        with open(config_file, 'w') as f:
            json.dump(updated_json, f, indent=4)
        
        print(f"{Fore.GREEN}✓{Fore.RESET} 默认配置文件更新成功")
        return 0
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 更新配置文件时出错:\n{Fore.RED}{e}{Fore.RESET}")
        exit_code = 1
        return 1

config_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "config.json")
if os.path.exists(config_file):
    try:
        with open(config_file, 'r') as file:
            config_data = json.load(file)
        auto_check_update = config_data['application']['run']['auto_check_update']
        auto_get_notice = config_data['application']['run']['auto_get_notice']
    except Exception as e:
        auto_check_update = True
        auto_get_notice = True
        print(f"{Fore.RED}✕{Fore.RESET} 读取配置文件时出错:\n{Fore.RED}{e}{Fore.RESET}\n{Fore.BLUE}[!]{Fore.RESET} 请检查配置文件是否正确，您可以先删除配置文件然后运行任意中文git的命令来重新生成默认配置文件。")
        exit_code = 1
else:
    # 没有配置文件就默认都要
    auto_check_update = True
    auto_get_notice = True
    print(f"{Fore.YELLOW}⚠{Fore.RESET} 您的中文Git的安装目录下似乎{Fore.YELLOW}缺少配置文件{Fore.RESET}，程序将尝试自动生成默认配置文件！")
    try:
        # 生成一个默认配置文件
        # 将数据结构转换为 JSON 格式的字符串
        json_str = {
            "information": {
                "version": "v3.0"
            },
            "application": {
                "notice": {
                    "time": "",
                    "level": "",
                    "content": ""
                },
                "run": {
                    "auto_check_update": "True",
                    "auto_get_notice": "True"
                }
            }
        }

        json_str = json.dumps(json_str, indent=4) # indent 参数用于设置缩进(4空)

        # 将 JSON 字符串写入文件
        with open(config_file, 'w') as f:
            f.write(json_str)
        print(f"{Fore.GREEN}✓{Fore.RESET} 默认配置文件生成成功")
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 默认配置文件生成失败！请{Fore.YELLOW}手动添加{Fore.RESET}配置文件，否则将无法运行一些功能！")
        exit_code = 1
        print(f"{Fore.BLUE}[!]{Fore.RESET} 如果你觉得这不应该可以提交Issue")
# -------------------

def always_check():# 每次执行命令都要检查的
    # ----------- 检查更新 ----------
    current_version = VERSION
    try:
        response = requests.get(url)
        data = response.json()
        latest_version = data['tag_name']  # 从 GitHub 获取最新版本号

        if latest_version != current_version:
            print(f"{Fore.BLUE}[!]{Fore.RESET} 发现新版本 {Fore.RED}{current_version}{Fore.RESET} → {Fore.GREEN}{latest_version}{Fore.RESET}\n运行 {Fore.BLUE}中文git 更新{Fore.RESET} 命令以更新。")
    except:
        pass

def check_for_updates():
    global exit_code
    # 提取版本号
    current_version = VERSION.split('-')[0]  # 分离可能的 '-pack' 后缀

    try:
        response = requests.get(url)
        data = response.json()
        latest_version = data['tag_name']  # 从 GitHub 获取最新版本号

        if latest_version != current_version:
            print(f"{Fore.BLUE}[!]{Fore.RESET} 发现新版本 {Fore.RED}{current_version}{Fore.RESET} → {Fore.GREEN}{latest_version}{Fore.RESET} 可用！")
            return latest_version
        else:
            print(f"{Fore.GREEN}✓{Fore.RESET} 您已安装最新版本 {Fore.BLUE}{current_version}{Fore.RESET}。")
            return None
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 检查更新时出错: {e}")
        exit_code = 1
        return None

def download_update_file(version):
    global exit_code
    # 根据版本确定下载 URL
    download_url = f'https://github.com/DuckDuckStudio/Chinese_git/releases/download/{version}/Chinese_git.py'
    spare_download_url = 'https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/Spare-Download/Chinese_git.py'
    spare_download_version_url = 'https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/Spare-Download/info.json'

    try:
        response = requests.get(download_url)
        
        # 重命名下载的文件为"中文Git.exe" 或 "中文Git.py"
        new_filename = '中文Git.py'
        
        with open(new_filename, 'wb') as f:
            f.write(response.content)
        
        print(f"{Fore.GREEN}✓{Fore.RESET} 更新成功下载。")
        
        return new_filename
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 下载更新文件时出错: {e}")
        exit_code = 1
        choice = input(f"{Fore.BLUE}?{Fore.RESET} 是否切换备用下载路线(是/否): ").lower()
        if choice in ['是', 'y', 'yes']:
            try:
                spare_download_version = requests.get(spare_download_version_url)
                data = spare_download_version.json()
                spare_download_version = data['version']# 获取备用路线的程序的版本号
            except Exception as e:
                print(f"{Fore.RED}✕{Fore.RESET} 获取备用路线版本信息时出错: {Fore.RED}{e}{Fore.RESET}")
                exit_code = 1
                return None
            if spare_download_version == version:
                try:
                    response = requests.get(spare_download_url)
                    
                    new_filename = '中文git.py'
                    
                    with open(new_filename, 'wb') as f:
                        f.write(response.content)
                    
                    print(f"{Fore.GREEN}✓{Fore.RESET} 更新成功下载。")
                    
                    return new_filename
                except Exception as e:
                    print(f"{Fore.RED}✕{Fore.RESET} 下载更新文件时出错: {e}")
                    exit_code = 1
                    return None
            else:
                print(f"{Fore.RED}✕{Fore.RESET} 备用路线{Fore.YELLOW}版本不一致{Fore.RESET}\n备用路线版本为{Fore.BLUE}{spare_download_version}{Fore.RESET}，而GitHub Releases上的最新版为{Fore.BLUE}{version}{Fore.BLUE}\n{Fore.YELLOW}如果你遇到了这个错误，请前往GitHub提交Issue，感谢！{Fore.RESET}")
                exit_code = 1
                return None
        return None

def replace_current_program(new_filename):
    global exit_code
    try:
        # 用下载的文件替换当前程序
        os.replace(new_filename, sys.argv[0])
        if update_json() == 1:
            print(f"{Fore.YELLOW}⚠{Fore.RESET} 请手动更新配置文件并提交issue")
        print(f"{Fore.GREEN}✓{Fore.RESET} 程序已成功更新。")
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 替换当前程序时出错: {e}")
        exit_code = 1

# 自动检查更新并提示用户安装
def auto_update():
    new_version = check_for_updates()

    if new_version:
        # 询问用户是否安装更新
        choice = input(f"{Fore.BLUE}?{Fore.RESET} 是否要安装此更新? (是/否): ").lower()
        if choice in ['是','y','yes']:
            new_filename = download_update_file(new_version)
            if new_filename:
                replace_current_program(new_filename)
        else:
            print(f"{Fore.BLUE}[!]{Fore.RESET} 已跳过更新。")

# ---------- 版本...更新 结束 ----------
# ---------- 公告获取 -----------------
notice_url = 'https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/notice/notice.txt'
previous_notice_file = os.path.join(script_path, 'previous_notice.txt')# 显示过的公告

def get_notice_content(url, manual=False):
    global exit_code
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            return content
        else:
            if manual:
                print(f"{Fore.RED}✕{Fore.RESET} 获取最新公告失败！\n状态码: {Fore.BLUE}{response.status_code}{Fore.RESET}")
                t = input(f"{Fore.BLUE}?{Fore.RESET} 是否读取本地最新公告({Fore.GREEN}是{Fore.RESET}/{Fore.RED}否{Fore.RESET}):").lower()
                if t in ['是', 'y', 'yes']:
                    display_notice('本地')
                else:
                    exit_code = 1
            return None
    except Exception as e:
        if manual:
            print(f"{Fore.RED}✕{Fore.RESET} 获取最新公告失败！\n错误信息: {Fore.RED}{e}{Fore.RESET}")
            t = input(f"{Fore.BLUE}?{Fore.RESET} 是否读取本地最新公告({Fore.GREEN}是{Fore.RESET}/{Fore.RED}否{Fore.RESET}):").lower()
            if t in ['是', 'y', 'yes']:
                display_notice('本地')
            else:
                exit_code = 1
        return None

def save_previous_notice(content):
    with open(previous_notice_file, 'w') as file:
        file.write(content)

def read_previous_notice():
    try:
        with open(previous_notice_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""
    except Exception:
        return "" # 以防出现像 microsoft/winget-pkgs #156224 中的错误

def display_notice(manual=False):
    global exit_code
    if manual:
        content = get_notice_content(notice_url, True)
    elif not manual:
        content = get_notice_content(notice_url)

    if manual == "本地":
        content = read_previous_notice()
        if content == "":
            print(f"{Fore.RED}✕{Fore.RESET} 没有本地公告")
            exit_code = 1
            return
    else:
        previous_notice = read_previous_notice()

    if content:
        try:
            lines = content.split('\n')

            # ---- 值提取 ----
            level_line = lines[0].strip()
            level = int(level_line.split(':')[1])
            # -- 等级↑ 是否强制↓ --
            force_line = lines[1].strip()
            force = bool(force_line.split(':')[1])
            # ----------------
        except Exception as e:
            if not manual:
                return
            else:
                print(f"{Fore.RED}✕{Fore.RESET} 最新公告{Fore.YELLOW}不符合{Fore.RESET}规范，请联系开发者反馈！")
                print(f"{Fore.RED}✕{Fore.RESET} 反馈时{Fore.YELLOW}请带上错误信息{Fore.RESET}:\n{Fore.RED}{e} | {Fore.CYAN}{level_line} {Fore.RED}|{Fore.CYAN} {force_line}{Fore.RESET}")
                exit_code = 1
                return

        if level == 1:
            color = Fore.RED
        elif level == 2:
            color = Fore.YELLOW
        elif level == 3:
            color = Fore.GREEN
        elif level == 4:
            color = Fore.BLUE
        else:
            color = ''

        if manual:
            print(f"{color}[!最新公告({level}级)!]{Fore.RESET}")
            for line in lines[2:]:
                print(line)
            print(f"{color}[!------------!]{Fore.RESET}")
        elif manual == "本地":
            print(f"{color}[!最新本地公告({level}级)!]{Fore.RESET}")
            for line in lines[2:]:
                print(line)
            print(f"{color}[!------------!]{Fore.RESET}")
        else:
            if content != previous_notice:
                if force:
                    print(f"\n{color}[!有新公告({level}级)!]{Fore.RESET}")
                    for line in lines[2:]:
                        print(line)
                    print(f"{color}[!------------!]{Fore.RESET}")
                save_previous_notice(content)
# ---------- 公告获取 结束 ------------

def git_command(command, *args):
    global exit_code
    args = list(args) # 统一类型
    git_command_mapping = {
        "拉取": ["git", "pull"],
        "推送": ["git", "push"],
        "提交": ["git", "commit", "-m"],
        "新建分支": ["git", "checkout", "-b"],
        "合并": ["git", "merge"],
        "变基": ["git", "rebase"],
        "暂存": ["git", "add"],
        "状态": ["git", "status"],
        "日志": ["git", "log"],
        "删除分支": ["git", "branch", "-D"],
        "远程地址": ["git", "remote", "-v"],
        "远程更新": ["git", "remote", "update"],
        "远程分支": ["git", "branch", "-r"],
        "克隆": ["git", "clone"],
        "签出到": ["git", "checkout"],
        "图形化日志" :["git", "log", "--graph"],
        "是否忽略": ["git", "check-ignore", "-v"],
        "初始化": ["git", "init"],
        "本地分支": ["git", "branch"],
        "所有分支": ["git", "branch", "-a"],
        "强推": ["git", "push", "--force"],
        "更名分支": ["git", "branch", "-m"],
        # --- 特殊功能 ---
        "版本": ["git", "--version"],
        "更新": ["update"], # 没用到git
        "公告": ["notice"], # 没用到git
        # --- 结束 ---
        "还原": ["git", "revert"],
        "重置": ["git", "reset"],
        "差异": ["git", "diff"],
        "清理": ["git", "clean"], # TODO: 之后可以添加此命令的参数处理，例如 -n -f -df -xf 等
        "清理引用": ["git", "remote", "prune"],
        "配置": ["git", "config"],
    }
    if command == "帮助":
        print("使用方法:")
        print("中文git <中文指令> [参数]")
        print("即: 中文git <你想干什么> [具体要啥]")
        print("\n支持的中文命令请查看用户手册: https://github.com/DuckDuckStudio/Chinese_git/blob/main/USER_HANDBOOK.md#可用命令")
        return

    git_command = git_command_mapping.get(command)
    if git_command:
        try:
            if command == "提交":
                result = subprocess.run(['git', 'diff', '--cached', '--quiet'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0: # 0 代表没有修改, 1 代表有修改
                    print(f"{Fore.YELLOW}⚠{Fore.RESET} 你似乎还没有暂存任何修改")
                    choice = input(f"{Fore.BLUE}?{Fore.RESET} 是否要先暂存所有修改后直接提交: ").lower()
                    if choice in ['是', 'y', 'yes']:
                        subprocess.run(['git', 'add', '--all'], capture_output=True, text=True)
                    else:
                        exit_code = 1
                        print(f"{Fore.RED}✕{Fore.RESET} 请先暂存修改后再提交")
                if not args and exit_code != 1: # 没有提交信息且前面没出错
                    commit_message = input("请输入提交信息: ")
                    if not commit_message:
                        # 还不输提交信息? 玩我呢
                        print(f"{Fore.RED}✕{Fore.RESET} 请提供提交信息")
                        exit_code = 1
                    result = subprocess.run(git_command + [commit_message], capture_output=True, text=True)
                else:
                    # 有提交信息就直接提交
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "暂存":
                if args and args[0] == "所有":
                    result = subprocess.run(git_command + ['--all'], capture_output=True, text=True)
                elif not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 你要暂存什么你没告诉我啊")
                    exit_code = 1
                else:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "签出到":
                if not args:
                    branch = input("请输入需要切换的分支: ")
                    result = subprocess.run(git_command + [branch], capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
                    exit_code = 1
            elif command == "新建分支":
                if not args:
                    new_branch = input("请输入新分支名称: ")
                    result = subprocess.run(git_command + [new_branch], capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
            elif command == "删除分支":
                if not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 删除分支命令需要指定要删除的分支名称")
                    exit_code = 1
                elif len(args) == 2:
                    if args[1] == "+确认":
                        git_command = ["git", "branch", "-d"]
                result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "版本":
                print("中文Git by 鸭鸭「カモ」")
                print(f"版本: {Fore.BLUE}{VERSION}{Fore.RESET}")
                print(f"安装在: {Fore.BLUE}{full_path}{Fore.RESET}")
                result = subprocess.run(git_command, capture_output=True, text=True)
            elif command == "公告":
                display_notice(True)
                return
            elif command == "还原":
                if not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 还原命令需要参数")
                    exit_code = 1
                else:
                    if args[0] == "最新提交":
                        result = subprocess.run(git_command + ['HEAD'], capture_output=True, text=True)
                    elif args[0].startswith("倒数第"):
                        try:
                            if args[0].endswith('个提交'):
                                num = args[0]
                                num = num[3:-3]
                            else:
                                num = int(args[0][3:])
                            result = subprocess.run(git_command + [f'HEAD~{num}'], capture_output=True, text=True)
                        except ValueError:
                            print(f"{Fore.RED}✕{Fore.RESET} 参数错误，请输入倒数第n个提交，n为正整数。")
                            exit_code = 1
                    else:
                        result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "克隆":
                if not args:
                    repository = input("请输入远程仓库链接: ")
                    result = subprocess.run(git_command + [repository], capture_output=True, text=True)
                else:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "是否忽略":
                if not args:
                    file = input("请输入需要检查的文件/文件夹: ")
                    if not file:
                        print(f"{Fore.RED}✕{Fore.RESET} 文件/文件夹名不能为空")
                        exit_code = 1
                    result = subprocess.run(git_command + [file], capture_output=True, text=True)
                else:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "本地分支":
                if len(args) > 2:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
                    exit_code = 1
                elif args[0] == "+最后提交":
                    git_command.append("-v")
                elif (args[0] == "+最后提交" and args[1] == "+与上游分支关系") or (args[0] == "+与上游分支关系" and args[1] == "+最后提交"):
                    git_command.append("-vv")
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 无效的参数")
                    exit_code = 1
                result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "合并":
                if not args:
                    branch = input("请输入需要合并到当前分支的分支: ")
                    result = subprocess.run(git_command + [branch], capture_output=True, text=True)
                else:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "更名分支":
                if not args:
                    old_branch = input("请输入旧分支名:")
                    new_branch = input("请输入新分支名:")
                    if old_branch == new_branch:
                        print(f"{Fore.RED}✕{Fore.RESET} 新旧分支名称相同")
                        exit_code = 1
                    result = subprocess.run(git_command + [old_branch, new_branch], capture_output=True, text=True)
                if args < 2:
                    print(f"{Fore.RED}✕{Fore.RESET} 缺少参数")
                    exit_code = 1
                else:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "更新":
                print("中文Git by 鸭鸭「カモ」")
                print(f"当前版本: {Fore.BLUE}{VERSION}{Fore.RESET}")
                print("正在检查更新...")
                auto_update()
                return
            elif command == "重置":
                if not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 重置指令需要具体的参数。")
                    exit_code = 1
                elif len(args) > 2:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
                    exit_code = 1
                elif len(args) == 2:
                    if args[1] == "+保留更改": # 默认
                        git_command.append("--mixed")
                    elif args[1] == "+删除更改":
                        git_command.append("--hard")
                    else:
                        print(f"{Fore.RED}✕{Fore.RESET} 无效的附加参数")
                        exit_code = 1
                    
                if args[0] in ["最新提交", "HEAD"]:
                    print(f"{Fore.YELLOW}⚠{Fore.RESET} 虽然您这样做不会出错，但这样做有意义吗(思考)")
                    result = subprocess.run(git_command + ['HEAD'], capture_output=True, text=True)
                elif args[0].startswith("倒数第"):
                    try:
                        if args[0].endswith('个提交'):
                            num = args[0]
                            num = num[3:-3]
                        else:
                            num = int(args[0][3:])
                        result = subprocess.run(git_command + [f'HEAD~{num}'], capture_output=True, text=True)
                    except ValueError:
                        print(f"{Fore.RED}✕{Fore.RESET} 参数错误，请输入倒数第n个提交，n为正整数。")
                        exit_code = 1
                else:
                    result = subprocess.run(git_command + args, capture_output=True, text=True)
            elif command == "清理引用":
                if not args:
                    # 默认
                    git_command.append("origin")
                result = subprocess.run(git_command + args, capture_output=True, text=True)
            else:
                result = subprocess.run(git_command + args, capture_output=True, text=True)

            if result.returncode == 0 and exit_code == 0:
                print(result.stdout)
            elif exit_code != 1: # 已设置错误代码的都已输出错误信息
                print(f"{Fore.RED}✕{Fore.RESET} 错误: {result.stderr}")
                exit_code = 1
            
            if auto_check_update == "True":
                always_check() # 自动检查更新
            if auto_get_notice == "True":
                display_notice() # 自动公告获取
        except Exception as e:
            print(f"{Fore.RED}✕{Fore.RESET} 执行命令时出错: {e}")
            if auto_check_update == "True":
                always_check() # 自动检查更新
            if auto_get_notice == "True":
                display_notice() # 自动公告获取
            exit_code = 1
    else:
        print("不支持的命令:", command)
        if auto_check_update == "True":
            always_check() # 自动检查更新
        if auto_get_notice == "True":
            display_notice() # 自动公告获取
            exit_code = 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        git_command(sys.argv[1], *sys.argv[2:])
    else:
        print("使用方法:")
        print("中文git <中文指令> [参数]")
        print("即: 中文git <你想干什么> [具体要啥]")
        if auto_check_update == "True":
            always_check() # 自动检查更新
        if auto_get_notice == "True":
            display_notice() # 自动公告获取
        exit_code = 1
sys.exit(exit_code)

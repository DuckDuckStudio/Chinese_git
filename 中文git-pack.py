import os
import sys
import requests
import subprocess
from colorama import init, Fore

init(autoreset=True)
script_path = os.path.dirname(sys.argv[0])
full_path = os.path.join(script_path, "中文git.exe")

# ---------- 版本定义及更新 ----------
# 定义版本号
VERSION = 'v2.7-pack'

def always_check():# 每次执行命令都要检查的
    # ----------- 检查更新 ----------
    current_version = VERSION.split('-')[0]# 分离-pack
    url = 'https://api.github.com/repos/DuckDuckStudio/Chinese_git/releases/latest'
    try:
        response = requests.get(url)
        data = response.json()
        latest_version = data['tag_name']  # 从 GitHub 获取最新版本号

        if latest_version != current_version:
            print(f"{Fore.BLUE}[!]{Fore.RESET} 发现新版本 {Fore.RED}{current_version}{Fore.RESET} → {Fore.GREEN}{latest_version}{Fore.RESET}\n运行 {Fore.BLUE}中文git 更新{Fore.RESET} 命令以更新。")
    except:
        pass

def check_for_updates():
    # 提取版本号
    current_version = VERSION.split('-')[0]  # 分离可能的 '-pack' 后缀

    # GitHub releases API URL
    url = 'https://api.github.com/repos/DuckDuckStudio/Chinese_git/releases/latest'

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
        return None

# 自动检查更新并提示用户安装
def auto_update():
    new_version = check_for_updates()

    if new_version:
        # 询问用户是否安装更新
        choice = input(f"{Fore.BLUE}?{Fore.RESET} 是否要安装此更新? (是/否): ").lower()
        if choice in ['是','y','yes']:
            print(f"{Fore.BLUE}[!]{Fore.RESET} 正在尝试更新更新程序...")
            new_filename = download_update_file(new_version)
            if new_filename:
                replace_current_program(new_filename)
            else:
                return
            print(f"{Fore.BLUE}[!]{Fore.RESET} 检测到您使用的是打包版，请前往新窗口继续...")
            print(f"{Fore.BLUE}[!]{Fore.RESET} 正在启动更新程序...")
            try:
                os.system(f"start {script_path}\\中文git更新程序.exe --version {new_version}")
                sys.exit()
            except FileNotFoundError:
                print(f"{Fore.RED}✕{Fore.RESET} 未找到更新程序，请前往发行版页手动下载补全！")
            except Exception as e:
                print(f"{Fore.RED}✕{Fore.RESET} 启动更新程序时出错: {Fore.RED}{e}{Fore.RESET}")
        else:
            print(f"{Fore.BLUE}[!]{Fore.RESET} 已跳过更新。")

# ------- 更新更新程序 -------
def download_update_file(version):
    # 根据版本确定下载 URL
    download_url = f'https://github.com/DuckDuckStudio/Chinese_git/releases/download/{version}/Pack_Version_Update.exe'
    #spare_download_url = f'https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/Spare-Download/Pack_Version_Update.exe'

    try:
        response = requests.get(download_url)
        
        new_filename = '中文git更新程序.exe'
        
        with open(new_filename, 'wb') as f:
            f.write(response.content)
        
        print(f"{Fore.GREEN}✓{Fore.RESET} 更新成功下载。")
        
        return new_filename
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 下载更新文件时出错: {e}")
        #choice = input(f"{Fore.BLUE}?{Fore.RESET} 是否切换备用下载路线(是/否):").lower()
        #if choice in ['是', 'y']:
        #    try:
        #        response = requests.get(spare_download_url)
        #        filename = response.headers['Content-Disposition'].split('=')[1]
        #        
        #        new_filename = '中文Git.exe'
        #        
        #        with open(new_filename, 'wb') as f:
        #            f.write(response.content)
        #        
        #        print(f"{Fore.GREEN}✓{Fore.RESET} 更新成功下载。")
        #        
        #        return new_filename
        #    except Exception as e:
        #        print(f"{Fore.RED}✕{Fore.RESET} 下载更新文件时出错: {e}")
        #        return None
        return None
    
def replace_current_program(new_filename):
    try:
        # 用下载的文件替换当前程序
        os.replace(new_filename, os.path.join(os.path.dirname(sys.argv[0]), "中文git更新程序.exe"))
        print(f"{Fore.GREEN}✓{Fore.RESET} 更新程序已成功更新。")
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 替换当前更新程序时出错: {e}")

# ---------- 版本...更新 结束 ----------
# ---------- 公告获取 -----------------
notice_url = 'https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/notice/notice.txt'
previous_notice_file = os.path.join(script_path, 'previous_notice.txt')# 显示过的公告

def get_notice_content(url, manual=False):
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
            return None
    except Exception as e:
        if manual:
            print(f"{Fore.RED}✕{Fore.RESET} 获取最新公告失败！\n错误信息: {Fore.RED}{e}{Fore.RESET}")
            t = input(f"{Fore.BLUE}?{Fore.RESET} 是否读取本地最新公告({Fore.GREEN}是{Fore.RESET}/{Fore.RED}否{Fore.RESET}):").lower()
            if t in ['是', 'y', 'yes']:
                display_notice('本地')
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
    if manual == True:
        content = get_notice_content(notice_url, True)
    elif manual == False:
        content = get_notice_content(notice_url)

    if manual == "本地":
        content = read_previous_notice()
        if content == "":
            print(f"{Fore.RED}✕{Fore.RESET} 没有本地公告")
            return
    else:
        previous_notice = read_previous_notice()

    if content:
        lines = content.split('\n')
        level_line = lines[0].strip()
        level = int(level_line.split(':')[1])

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

        if manual == True:
            print(f"{color}[!最新公告({level}级)!]{Fore.RESET}")
            for line in lines[1:]:
                print(line)
            print(f"{color}[!------------!]{Fore.RESET}")
        elif manual == "本地":
            print(f"{color}[!最新本地公告({level}级)!]{Fore.RESET}")
            for line in lines[1:]:
                print(line)
            print(f"{color}[!------------!]{Fore.RESET}")
        else:
            if content != previous_notice:
                print(f"\n{color}[!有新公告({level}级)!]{Fore.RESET}")
                for line in lines[1:]:
                    print(line)
                print(f"{color}[!------------!]{Fore.RESET}")
                save_previous_notice(content)
# ---------- 公告获取 结束 ------------
# ---------- 各命令函数 ---------------
def check_git_stash():
    staged_changes = False
    unstaged_changes = False

    git_stash = subprocess.run(["git", "stash", "show"], capture_output=True, text=True)
    output_lines = git_stash.stdout.split('\n')

    print(output_lines)

    if output_lines != ['']:
        staged_changes = True

    # --------

    git_stash = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True)
    output_lines = git_stash.stdout.split('\n')

    print(output_lines)

    if output_lines != ['']:
        unstaged_changes = True

    return staged_changes, unstaged_changes
# ------------------------------------------

def git_command(command, *args):
    git_command_mapping = {
        "拉取": "pull",
        "推送": "push",
        "提交": "commit",
        "新建分支": "checkout -b",
        "切换分支": "checkout",
        "合并": "merge",
        "暂存": "add",
        "状态": "status",
        "日志": "log",
        "删除分支": "branch -D",
        "远程地址": "remote -v",
        "远程更新": "remote update",
        "远程分支": "branch -r",
        "克隆": "clone",
        "签出到": "checkout",
        "图形化日志" :"log --graph",
        "是否忽略": "check-ignore -v",
        "初始化": "init",
        "本地分支": "branch",
        "强推": "push --force",
        "更名分支": "branch -m",
        # --- 特殊功能 ---
        "版本": "-v",
        "更新": "update",
        "公告": "notice",
        # --- 结束 ---
        "还原": "revert",
        "重置": "reset",
        "差异": "diff",
        "清理引用": "remote prune origin",
        # 可根据需要添加更多映射
    }
    if command == "帮助":
        print("使用方法:")
        print("中文git <中文指令> [参数]")
        print("即：中文git <你想干什么> [具体要啥]")
        print("\n支持的中文指令:")
        print("中文git", end=" ")
        for cmd in git_command_mapping:
            print(f"[{cmd}]", end=" ")
        print("\n详细支持命令请查看用户手册：https://github.com/DuckDuckStudio/Chinese_git/blob/main/USER_HANDBOOK.md#可用命令")
        return

    git_command = git_command_mapping.get(command)
    if git_command:
        try:
            if command == "提交":
                staged, unstaged = check_git_stash()
                print("暂存的更改:", staged)
                print("未暂存的更改:", unstaged)
                if staged:
                    print(f"{Fore.BLUE}[!]{Fore.BLUE} 将提交暂存区的内容")
                elif unstaged:
                    print(f"{Fore.YELLOW}⚠{Fore.RESET} 没有已暂存的更改，但检测到未暂存的更改")
                    if input(f"{Fore.BLUE}?{Fore.RESET} 是否暂存所有并提交({Fore.GREEN}是{Fore.RESET}/{Fore.RED}否{Fore.RESET}):").lower() in ['y', 'yes', '是']:
                        subprocess.run('git ' + 'add ' + '--all')
                        print(f"{Fore.GREEN}✓{Fore.RESET} 已暂存所有更改")
                    else:
                        print(f"{Fore.RED}✕{Fore.RESET} 没有已暂存的更改")
                        return
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 没有更改")
                    return

                if not args:
                    commit_message = input("请输入提交信息: ")
                    if not commit_message:
                        # 还不输提交信息？玩我呢
                        print(f"{Fore.RED}✕{Fore.RESET} 请提供提交信息")
                        return
                    result = subprocess.run('git ' + git_command + ' -m "' + commit_message + '"', capture_output=True, text=True)
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "暂存":
                if args and args[0] == "所有":
                    result = subprocess.run('git ' + git_command + ' --all', capture_output=True, text=True)
                elif not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 你要暂存什么你没告诉我啊")
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "切换分支" or command == "签出到":
                if not args:
                    branch = input("请输入需要切换的分支：")
                    result = subprocess.run('git ' + git_command + ' ' + branch, capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
            elif command == "新建分支":
                if not args:
                    new_branch = input("请输入新分支名称: ")
                    result = subprocess.run('git ' + git_command + ' ' + new_branch, capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
            elif command == "删除分支":
                if not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 删除分支命令需要指定要删除的分支名称")
                    return
                elif len(args) > 2:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
                    return
                elif len(args) == 2:
                    if args[1] == "+确认":
                        git_command = "branch -d"
                    else:
                        print(f"{Fore.RED}✕{Fore.RESET} 无效的附加参数")
                        return
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "版本":
                print("中文Git by 鸭鸭「カモ」")
                print(f"版本：{Fore.BLUE}{VERSION}{Fore.RESET}")
                print(f"安装在: {Fore.BLUE}{full_path}{Fore.RESET}")
                result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "还原":
                if not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 还原命令需要参数")
                else:
                    if args[0] == "最新提交":
                        result = subprocess.run('git ' + git_command + ' HEAD', capture_output=True, text=True)
                    elif args[0].startswith("倒数第"):
                        try:
                            if args[0].endswith('个提交'):
                                num = args[0]
                                num = num[3:-3]
                            else:
                                num = int(args[0][3:])
                            result = subprocess.run(['git ', git_command, f'HEAD~{num}'], capture_output=True, text=True)
                        except ValueError:
                            print(f"{Fore.RED}✕{Fore.RESET} 参数错误，请输入倒数第n个提交，n为正整数。")
                            return
                    else:
                        result = subprocess.run('git ' + git_command + ' ' + args[0], capture_output=True, text=True)
            elif command == "克隆":
                if not args:
                    repository = input("请输入远程仓库链接(以.git结尾)：")
                    result = subprocess.run('git ' + git_command + ' ' + repository, capture_output=True, text=True)
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "是否忽略":
                if not args:
                    file = input("请输入需要检查的文件/文件夹：")
                    if not file:
                        print(f"{Fore.RED}✕{Fore.RESET} 文件/文件夹名不能为空")
                        return
                    result = subprocess.run('git ' + git_command + ' ' + file, capture_output=True, text=True)
                    print (result)
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "查看本地分支":
                if len(args) > 2:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
                    return
                elif args[0] == "+最后提交":
                    git_command = "branch -v"
                elif (args[0] == "+最后提交" and args[1] == "+与上游分支关系") or (args[0] == "+与上游分支关系" and args[1] == "+最后提交"):
                    git_command = "branch -vv"
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 无效的参数")
                    return
                result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "合并":
                if not args:
                    branch = input("请输入需要合并到当前分支的分支：")
                    result = subprocess.run('git ' + git_command + ' ' + branch, capture_output=True, text=True)
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "更名分支":
                if not args:
                    old_branch = input("请输入旧分支名:")
                    new_branch = input("请输入新分支名:")
                    if old_branch == new_branch:
                        print(f"{Fore.RED}✕{Fore.RESET} 新旧分支名称相同")
                        return
                    result = subprocess.run('git ' + git_command + ' ' + old_branch + ' ' + new_branch, capture_output=True, text=True)
                if args < 2:
                    print(f"{Fore.RED}✕{Fore.RESET} 缺少参数")
                    return
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "更新":
                print("中文Git by 鸭鸭「カモ」")
                print("正在检查更新...")
                auto_update()
                return
            elif command == "公告":
                display_notice(True)
                return
            elif command == "重置":
                if not args:
                    print(f"{Fore.RED}✕{Fore.RESET} 重置指令需要具体的参数。")
                    return
                elif len(args) > 2:
                    print(f"{Fore.RED}✕{Fore.RESET} 多余的参数")
                    return
                elif len(args) == 2:
                    if args[1] == "+保留更改":# 默认
                        git_command = "reset --mixed"
                    elif args[1] == "+删除更改":
                        git_command = "reset --hard"
                    else:
                        print(f"{Fore.RED}✕{Fore.RESET} 无效的附加参数")
                        return
                    
                if args[0] in ["最新提交", "HEAD"]:
                    print(f"{Fore.YELLOW}⚠{Fore.RESET} 虽然您这样做不会出错，但这样做有意义吗(思考)")
                    result = subprocess.run('git ' + git_command + ' HEAD', capture_output=True, text=True)
                elif args[0].startswith("倒数第"):
                    try:
                        if args[0].endswith('个提交'):
                            num = args[0]
                            num = num[3:-3]
                        else:
                            num = int(args[0][3:])
                        result = subprocess.run(['git ', git_command, f'HEAD~{num}'], capture_output=True, text=True)
                    except ValueError:
                        print(f"{Fore.RED}✕{Fore.RESET} 参数错误，请输入倒数第n个提交，n为正整数。")
                        return
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            else:
                result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)

            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f"{Fore.RED}✕{Fore.RESET} 错误: {result.stderr}")
            
            always_check()# 自动检查更新
            display_notice() # 自动公告获取
        except Exception as e:
            print(f"{Fore.RED}✕{Fore.RESET} 执行git命令时出错: {e}")
            always_check()# 自动检查更新
            display_notice() # 自动公告获取
    else:
        print("不支持的命令:", command)
        always_check()# 自动检查更新
        display_notice() # 自动公告获取

if __name__ == "__main__":
    if len(sys.argv) > 1:
        git_command(sys.argv[1], *sys.argv[2:])
    else:
        print("使用方法:")
        print("中文git <中文指令> [参数]")
        print("即：中文git <你想干什么> [具体要啥]")
        always_check()
        display_notice() # 自动公告获取

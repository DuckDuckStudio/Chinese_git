import subprocess
import requests
import sys
import os

# ---------- 版本定义及更新 ----------
# 定义版本号
VERSION = 'v1.9'

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
            print("发现新版本 {} 可用！".format(latest_version))
            return latest_version
        else:
            print("您已安装最新版本 {}。".format(current_version))
            return None
    except Exception as e:
        print("检查更新时出错：", e)
        return None

def download_update_file(version):
    # 根据版本号是否包含 '-pack' 后缀来确定文件后缀名
    file_extension = '.exe' if '-pack' in version else '.py'

    # 根据版本确定下载 URL
    download_url = 'https://github.com/DuckDuckStudio/Chinese_git/releases/download/{}/Chinese_git{}'.format(version, file_extension)

    try:
        response = requests.get(download_url)
        filename = response.headers['Content-Disposition'].split('=')[1]
        
        # 重命名下载的文件为"中文Git.exe" 或 "中文Git.py"
        new_filename = '中文Git{}'.format(file_extension)
        
        with open(new_filename, 'wb') as f:
            f.write(response.content)
        
        print("更新成功下载。")
        
        return new_filename
    except Exception as e:
        print("下载更新文件时出错：", e)
        return None

def replace_current_program(new_filename):
    try:
        # 用下载的文件替换当前程序
        os.replace(new_filename, sys.argv[0])
        print("程序已成功更新。")
    except Exception as e:
        print("替换当前程序时出错：", e)

# 自动检查更新并提示用户安装
def auto_update():
    new_version = check_for_updates()

    if new_version:
        # 询问用户是否安装更新
        choice = input("是否要安装此更新？ (是/否): ").lower()
        if choice == '是':
            new_filename = download_update_file(new_version)
            if new_filename:
                replace_current_program(new_filename)
        else:
            print("已跳过更新。")

# ---------- 版本...更新 结束 ----------

script_path = os.path.dirname(__file__)
full_path = os.path.join(script_path, "中文git.py")

def git_command(command, *args):
    git_command_mapping = {
        "拉取": "pull",
        "推送": "push",
        "提交": "commit",
        "新建分支": "checkout -b",
        "切换分支": "checkout",
        "合并": "merge",
        "暂存": "add",
        "查看状态": "status",
        "查看日志": "log",
        "重置": "reset",
        "删除分支": "branch -D",
        "远程地址": "remote -v",
        "远程更新": "remote update",
        "查看远程分支": "branch -r",
        "版本": "-v",
        "克隆": "clone",
        "配置": "config",
        "签出到": "checkout",
        "查看图形化日志" :"log --graph",
        "是否忽略": "check-ignore -v",
        "初始化": "init",
        "查看本地分支": "branch",
        "强推": "push --force",
        "更名分支": "branch -m",
        # --- 更新 ---
        "更新": "update",
        # --- 结束 ---
        "还原": "revert",
        "重置": "reset",
        # 可根据需要添加更多映射
    }
    git_config_subcommands = {
        "全局": "--global",
        "系统": "--system"
    }
    if command == "帮助":
        print("使用方法:")
        print("python 中文git.py <中文指令> [参数]")
        print("即：python 中文git.py <你想干什么> [具体要啥]")
        print("支持的中文指令:")
        for cmd in git_command_mapping:
            print("-", cmd)
        print("详细支持命令请查看用户手册：https://github.com/DuckDuckStudio/Chinese_git/blob/main/USER_HANDBOOK.md#可用命令")
        return

    git_command = git_command_mapping.get(command)
    if git_command:
        try:
            if command == "提交":
                if not args:
                    commit_message = input("请输入提交信息: ")
                    result = subprocess.run('git ' + git_command + ' -m "' + commit_message + '"', capture_output=True, text=True)
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "暂存":
                if args and args[0] == "所有":
                    result = subprocess.run('git ' + git_command + ' --all', capture_output=True, text=True)
                elif not args:
                    print("你要暂存什么你没告诉我啊")
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "切换分支" or command == "签出到":
                if not args:
                    branch = input("请输入需要切换的分支：")
                    result = subprocess.run('git ' + git_command + ' ' + branch, capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
                else:
                    print("多余的参数")
            elif command == "新建分支":
                if not args:
                    new_branch = input("请输入新分支名称: ")
                    result = subprocess.run('git ' + git_command + ' ' + new_branch, capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
                else:
                    print("多余的参数")
            elif command == "删除分支":
                if not args:
                    print("删除分支命令需要指定要删除的分支名称。")
                    return
                elif len(args) > 2:
                    print("多余的参数")
                    return
                elif len(args) == 2:
                    if args[1] == "+确认":
                        git_command = "branch -d"
                    else:
                        print("无效的附加参数")
                        return
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "版本":
                print("中文Git by 鸭鸭「カモ」")
                print(f"版本：{VERSION}")
                print("安装在", full_path)
                result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "还原":
                if not args:
                    print("请输入要还原的提交（最新提交/倒数第n个提交/具体某个提交）: ")
                else:
                    if args[0] == "最新提交":
                        result = subprocess.run('git ' + git_command + ' HEAD', capture_output=True, text=True)
                    elif args[0].startswith("倒数第"):
                        try:
                            num = int(args[0][3:])
                            result = subprocess.run(['git ', git_command, f'HEAD~{num}'], capture_output=True, text=True)
                        except ValueError:
                            print("参数错误，请输入倒数第n个提交，n为正整数。")
                            return
                    else:
                        result = subprocess.run('git ' + git_command + ' ' + args[0], capture_output=True, text=True)
            elif command == "克隆":
                if not args:
                    repository = input("请输入远程仓库链接(以.git结尾)：")
                    result = subprocess.run('git ' + git_command + ' ' + repository, capture_output=True, text=True)
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "配置":
                if not args:
                    print("配置命令需要指定配置选项和值。")
                elif len(args) == 1:
                    print("配置命令需要指定配置值。")
                else:
                    config_option = args[0]
                    config_value = args[1]
                    config_subcommand = None
                # 检查是否存在配置范围
                if len(args) == 3:
                    config_subcommand = args[2]
                    if config_subcommand not in git_config_subcommands:
                        print("配置范围错误，可选范围为：全局、系统。")
                        return
                git_config_command = ['git ', git_command, config_option, config_value]
                if config_subcommand:# 如果存在配置范围
                    git_config_command.insert(2, git_config_subcommands[config_subcommand])
                result = subprocess.run(git_config_command, capture_output=True, text=True)
            elif command == "是否忽略":
                if not args:
                    file = input("请输入需要检查的文件/文件夹：")
                    if not file:
                        print("文件/文件夹名不能为空")
                        return
                    result = subprocess.run('git ' + git_command + ' ' + file, capture_output=True, text=True)
                    print (result)
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "查看本地分支":
                if len(args) > 2:
                    print("多余的参数")
                    return
                elif args[0] == "+最后提交":
                    git_command = "branch -v"
                elif (args[0] == "+最后提交" and args[1] == "+与上游分支关系") or (args[0] == "+与上游分支关系" and args[1] == "+最后提交"):
                    git_command = "branch -vv"
                else:
                    print("无效的参数")
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
                        print("新旧分支名称相同")
                        return
                    result = subprocess.run('git ' + git_command + ' ' + old_branch + ' ' + new_branch, capture_output=True, text=True)
                if args < 2:
                    print("缺少参数")
                    return
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            elif command == "更新":
                print("中文Git by 鸭鸭「カモ」")
                print(f"当前版本：{VERSION}")
                print("正在检查更新...")
                auto_update()
                return
            elif command == "重置":
                if not args:
                    print("重置指令需要具体的参数。")
                    return
                elif len(args) > 2:
                    print("多余的参数")
                    return
                elif len(args) == 2:
                    if args[1] == "+取消暂存区":# 默认
                        git_command = "reset --mixed"
                    elif args[1] == "+保持不变":
                        git_command = "reset --soft"
                    elif args[1] == "+删除更改":
                        git_command = "reset --hard"
                    else:
                        print("无效的附加参数")
                        return
                else:
                    result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
            else:
                result = subprocess.run('git ' + git_command + ' ' + ' '.join(args), capture_output=True, text=True)
                
            if result.returncode == 0:
                print(result.stdout)
            else:
                print("错误:", result.stderr)
        except Exception as e:
            print("执行git命令时出错:", e)
    else:
        print("不支持的git命令:", command)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        git_command(sys.argv[1], *sys.argv[2:])
    else:
        print("使用方法:")
        print("python 中文git.py <中文指令> [参数]")
        print("即：python 中文git.py <你想干什么> [具体要啥]")

import subprocess
import sys
import os

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
        "删除提交": "reset --hard HEAD~",
        "克隆": "clone",
        "配置": "config",
        "签出到": "checkout",
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
        print("详细支持命令请查看README_DEV文件：https://github.com/DuckDuckStudio/Chinese_git/blob/main/README_DEV.md#可用命令")
        return

    git_command = git_command_mapping.get(command)
    if git_command:
        try:
            if command == "提交":
                if not args:
                    commit_message = input("请输入提交信息: ")
                    result = subprocess.run(['git', git_command, '-m', commit_message], capture_output=True, text=True)
                else:
                    result = subprocess.run(['git', git_command, '-m', args[0]], capture_output=True, text=True)
            elif command == "暂存":
                if args and args[0] == "所有":
                    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
                elif not args:
                    print("[错误]你要暂存什么你没告诉我啊")
                else:
                    result = subprocess.run(['git', 'add'] + list(args), capture_output=True, text=True)
            elif command == "切换分支" or command == "签出到":
                if not args:
                    branch = input("请输入需要切换的分支：")
                    result = subprocess.run(['git', git_command, branch], capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
                else:
                    print("切换分支命令只接受一个参数。")
            elif command == "新建分支":
                if not args:
                    new_branch = input("请输入新分支名称: ")
                    result = subprocess.run(['git', git_command, new_branch], capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
                else:
                    print("新建分支命令只接受一个参数。")
            elif command == "删除分支":
                if not args:
                    print("删除分支命令需要指定要删除的分支名称。")
                elif len(args) == 1:
                    result = subprocess.run(['git', git_command, args[0]], capture_output=True, text=True)
                else:
                    print("删除分支命令只接受一个参数。")
            elif command == "版本":
                print("中文Git by 鸭鸭「カモ」")
                print("版本：v1.3")
                print("安装在", full_path)
                result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
            elif command == "删除提交":
                if not args:
                    print("请输入要删除的提交类型（最新提交/倒数第n个提交/具体某个提交）。")
                else:
                    if args[0] == "最新提交":
                        result = subprocess.run(['git', git_command, 'HEAD~1'], capture_output=True, text=True)
                    elif args[0].startswith("倒数第"):
                        try:
                            num = int(args[0][3:])
                            result = subprocess.run(['git', git_command, f'HEAD~{num}'], capture_output=True, text=True)
                        except ValueError:
                            print("参数错误，请输入倒数第n个提交，n为正整数。")
                            return
                    else:
                        result = subprocess.run(['git', git_command, args[0]], capture_output=True, text=True)
            elif command == "克隆":
                if not args:
                    repository = input("请输入远程仓库链接(以.git结尾)：")
                    result = subprocess.run(['git', git_command, repository], capture_output=True, text=True)
                else:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
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
                git_config_command = ['git', git_command, config_option, config_value]
                if config_subcommand:# 如果存在配置范围
                    git_config_command.insert(2, git_config_subcommands[config_subcommand])
                result = subprocess.run(git_config_command, capture_output=True, text=True)
            else:
                result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
                
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

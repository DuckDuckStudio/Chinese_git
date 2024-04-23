import subprocess
import sys
import os

script_path = os.path.dirname(__file__)
full_path = os.path.join(script_path, "中文git.exe")

def git_command(command, *args):
    git_command_mapping = {
        "拉取": "pull",
        "推送": "push",
        "提交": "commit",
        "新建分支": "checkout -b",
        "切換分支": "checkout",
        "合併": "merge",
        "暫存": "add",
        "查看狀態": "status",
        "查看日誌": "log",
        "重置": "reset",
        "刪除分支": "branch -D",
        "遠端地址": "remote -v",
        "遠端更新": "remote update",
        "查看遠端分支": "branch -r",
        "版本": "-v",
        "刪除提交": "reset --hard HEAD~",
        "克隆": "clone",
        "配置": "config",
        "簽出到": "checkout",
        "查看圖形化日誌": "log --graph",
        "是否忽略": "check-ignore -v",
        "初始化": "init",
        "查看本地分支": "branch",
        # 可根據需要添加更多映射
    }
    git_config_subcommands = {
        "全局": "--global",
        "系統": "--system"
    }
    if command == "幫助":
        print("使用方法:")
        print(full_path, " <中文指令> [參數]")
        print("即：", full_path, "<你想幹什麼> [具體要啥]")
        print("支持的中文指令:")
        for cmd in git_command_mapping:
            print("-", cmd)
            print("詳細支持命令請查看README_DEV文件：https://github.com/DuckDuckStudio/Chinese_git/blob/main/README_DEV.md#可用命令")
        return

    git_command = git_command_mapping.get(command)
    if git_command:
        try:
            if command == "提交":
                if not args:
                    commit_message = input("請輸入提交信息： ")
                    result = subprocess.run(['git', git_command, '-m', commit_message], capture_output=True, text=True)
                else:
                    result = subprocess.run(['git', git_command, '-m', args[0]], capture_output=True, text=True)
            elif command == "暫存":
                if args and args[0] == "所有":
                    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
                elif not args:
                    print("你要暫存什麼你沒告訴我啊")
                else:
                    result = subprocess.run(['git', 'add'] + list(args), capture_output=True, text=True)
            elif command == "切換分支" or command == "簽出到":
                if not args:
                    branch = input("請輸入需要切換的分支：")
                    result = subprocess.run(['git', git_command, branch], capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
                else:
                    print("多餘的參數")
            elif command == "新建分支":
                if not args:
                    new_branch = input("請輸入新分支名稱： ")
                    result = subprocess.run(['git', git_command, new_branch], capture_output=True, text=True)
                elif len(args) == 1:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
                else:
                    print("多餘的參數")
            elif command == "刪除分支":
                if not args:
                    print("刪除分支命令需要指定要刪除的分支名稱。")
                elif len(args) > 2:
                    print("多餘的參數")
                    return
                elif len(args) == 2 and args[1] == "+確認":
                    git_command = "git branch -d"
                else:
                    print("無效的附加參數")
                    return
                result = subprocess.run(['git', git_command, args[0]], capture_output=True, text=True)
            elif command == "版本":
                print("中文Git by 鸭鸭「カモ」")
                print("版本：v1.5-pack")
                print("繁體中文翻譯版")
                print("安裝在：", full_path)
                result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
            elif command == "刪除提交":
                if not args:
                    print("請輸入要刪除的提交類型（最新提交/倒數第n個提交/具體某個提交）。")
                else:
                    if args[0] == "最新提交":
                        result = subprocess.run(['git', git_command, 'HEAD~1'], capture_output=True, text=True)
                    elif args[0].startswith("倒數第"):
                        try:
                            num = int(args[0][3:])
                            result = subprocess.run(['git', git_command, f'HEAD~{num}'], capture_output=True, text=True)
                        except ValueError:
                            print("參數錯誤，請輸入倒數第n個提交，n為正整數。")
                            return
                    else:
                        result = subprocess.run(['git', git_command, args[0]], capture_output=True, text=True)
            elif command == "克隆":
                if not args:
                    repository = input("請輸入遠程倉庫鏈接（以.git結尾）：")
                    result = subprocess.run(['git', git_command, repository], capture_output=True, text=True)
                else:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
            elif command == "配置":
                if not args:
                    print("配置命令需要指定配置選項和值。")
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
                        print("配置範圍錯誤，可選範圍為：全局、系統。")
                        return
                git_config_command = ['git', git_command, config_option, config_value]
                if config_subcommand:# 如果存在配置范围
                    git_config_command.insert(2, git_config_subcommands[config_subcommand])
                result = subprocess.run(git_config_command, capture_output=True, text=True)
            elif command == "是否忽略":
                if not args:
                    file = input("請輸入需要檢查的文件/文件夾：")
                    result = subprocess.run(['git', git_command, file], capture_output=True, text=True)
                else:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
            elif command == "查看本地分支":
                if len(args) > 2:
                    print("多餘的參數")
                    return
                elif args[0] == "+最後提交":
                    git_command = "branch -v"
                elif (args[0] == "+最後提交" and args[1] == "+與上游分支關係") or (args[0] == "+與上游分支關係" and args[1] == "+最后提交"):
                    git_command = "branch -vv"
                else:
                    print("無效的參數")
                result = subprocess.run(['git', git_command], capture_output=True, text=True)
            elif command == "合併":
                if not args:
                    branch = input("請輸入需要合併到當前分支的分支：")
                    result = subprocess.run(['git', git_command, branch], capture_output=True, text=True)
                else:
                    result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
            else:
                result = subprocess.run(['git', git_command] + list(args), capture_output=True, text=True)
                
            if result.returncode == 0:
                print(result.stdout)
            else:
                print("錯誤:", result.stderr)
        except Exception as e:
            print("執行git命令時出錯:", e)
    else:
        print("不支持的git命令:", command)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        git_command(sys.argv[1], *sys.argv[2:])
    else:
        print("使用方法:")
        print(full_path, " <中文指令> [參數]")
        print("即：", full_path, "<你想幹什麼> [具體要啥]")

import os
import sys
import requests
import argparse
from colorama import init, Fore

init(autoreset=True)

exit_code = 0

def download_update_file(version):
    global exit_code
    # 根据版本确定下载 URL
    download_url = f'https://github.com/DuckDuckStudio/Chinese_git/releases/download/{version}/Chinese_git.exe'
    #spare_download_url = f'https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/Spare-Download/Chinese_git.exe'

    try:
        response = requests.get(download_url)
        
        new_filename = '中文git.exe'
        
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
        exit_code = 1
        return None
    
def replace_current_program(new_filename):
    global exit_code
    try:
        # 用下载的文件替换当前程序
        os.replace(new_filename, os.path.join(os.path.dirname(sys.argv[0]), "中文git.exe"))
        print(f"{Fore.GREEN}✓{Fore.RESET} 程序已成功更新。")
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 替换当前程序时出错: {e}")
        exit_code = 1
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="打包版中文Git的更新程序")
    parser.add_argument("--version", type=str, required=True, help="更新到的版本")
    args = parser.parse_args()

    new_filename = download_update_file(args.version)
    if new_filename:
        replace_current_program(new_filename)

    input(f"按{Fore.BLUE}Enter{Fore.RESET}键退出...")

sys.exit(exit_code)

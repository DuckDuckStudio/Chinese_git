import os
import sys
import py7zr
import zipfile
import shutil
import requests
import subprocess
from colorama import init, Fore
# 中文Git发行版自动打包程序 - CN源码
# 被中文命名骂怕了...

# --- 初始化 ---
init(autoreset=True)# 颜色显示
脚本位置 = os.path.dirname(os.path.abspath(sys.argv[0]))# 所在目录
os.chdir(脚本位置)# 确保命令执行位置
# ------------

# --- 仓库配置 ---
仓库 = "Chinese_git"
仓库_分布式版本控制系统链接 = f"https://github.com/DuckDuckStudio/{仓库}.git"
仓库位置 = os.path.join(脚本位置, 仓库)
# ----------------

# --- 发行版配置 ---
发行版本 = input("请输入发行版版本: ")

## --- 规范版本 ---
if 发行版本.startswith("v."):
    发行版本 = "v" + 发行版本[2:]
elif not 发行版本.startswith("v"):
    发行版本 = "v" + 发行版本
## -------------------

打包版位置 = os.path.join(脚本位置, 'Releases', 发行版本, 'Chinese_git')
源码版位置 = os.path.join(脚本位置, 'Releases', 发行版本, 'Chinese_git_py')
发行版位置 = os.path.join(脚本位置, 'Releases', 发行版本)

## --- 创建目录 ---
os.makedirs(打包版位置, exist_ok=True)
os.makedirs(源码版位置, exist_ok=True)
## ------------------

打包版主程序 = os.path.join(仓库位置, "中文git.exe")
打包版更新程序 = os.path.join(仓库位置, "中文git更新程序.exe")
源码版主程序 = os.path.join(仓库位置, "中文git.py")
公告文件 = os.path.join(仓库位置, "previous_notice.txt")
许可文件 = os.path.join(仓库位置, "LICENSE")
配置文件 = os.path.join(仓库位置, "config.json")
# -----------------------

# --- 定义 ---
def 克隆():
    结果 = subprocess.run(["git", "clone", 仓库_分布式版本控制系统链接], capture_output=True, text=True)
    if 结果.returncode == 0:
        print(f"{Fore.GREEN}✓{Fore.RESET} 克隆仓库成功")
        return True
    else:
        print(f"{Fore.RED}✕{Fore.RESET} 克隆仓库时出错:\n{Fore.RED}{结果.stderr}{Fore.RESET}")
        return False

def 获取公告():
    try:
        响应 = requests.get("https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/notice/notice.txt")
        响应.raise_for_status()
        with open(公告文件, 'wb') as 文件:
            文件.write(响应.content)
        print(f"{Fore.GREEN}✓{Fore.RESET} 获取公告文件成功")
        return True
    except Exception as 错误:
        print(f"{Fore.RED}✕{Fore.RESET} 获取公告文件时出错:\n{Fore.RED}{错误}{Fore.RESET}")
        return False

def 重命名文件(旧名称, 新名称, 目录):
    try:
        旧文件 = os.path.join(目录, 旧名称)
        新文件 = os.path.join(目录, 新名称)
        os.rename(旧文件, 新文件)
        return True
    except Exception as 错误:
        print(f"{Fore.RED}✕{Fore.RESET} 处理文件名时出错:\n{Fore.RED}{错误}{Fore.RESET}")
        return False

def 复制文件():
    try:
        shutil.copy(打包版主程序, 打包版位置)
        shutil.copy(打包版更新程序, 打包版位置)
        # ---
        shutil.copy(源码版主程序, 源码版位置)
        # ---
        shutil.copy(公告文件, 源码版位置)
        shutil.copy(公告文件, 打包版位置)
        # ---
        shutil.copy(许可文件, 源码版位置)
        shutil.copy(许可文件, 打包版位置)
        # ---
        shutil.copy(配置文件, 源码版位置)
        shutil.copy(配置文件, 打包版位置)
        # -----
        shutil.copy(打包版主程序, 发行版位置)
        if not 重命名文件(os.path.basename(打包版主程序), "Chinese_git.exe", 发行版位置):
            return False
        shutil.copy(打包版更新程序, 发行版位置)
        if not 重命名文件(os.path.basename(打包版更新程序), "Pack_Version_Update.exe", 发行版位置):
            return False
        shutil.copy(源码版主程序, 发行版位置)
        if not 重命名文件(os.path.basename(源码版主程序), "Chinese_git.py", 发行版位置):
            return False
        # -----
        print(f"{Fore.GREEN}✓{Fore.RESET} 复制文件成功")
        return True
    except Exception as 错误:
        print(f"{Fore.RED}✕{Fore.RESET} 复制文件时出错:\n{Fore.RED}{错误}{Fore.RESET}")
        return False

def 生成打包文件():
    # 发行版本 已在前面定义
    if 发行版本.startswith('v'):
        打包文件版本 = 发行版本[1:]
    打包文件 = f'''[Setup]
AppName=中文Git
#define cngitversion "{打包文件版本}"
AppVersion=v{{#cngitversion}}
VersionInfoVersion={{#cngitversion}}
AppPublisher=DuckStudio
VersionInfoCopyright=Copyright (c) 鸭鸭「カモ」
AppPublisherURL=https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/
DefaultDirName={{autopf}}\\Chinese_git
DefaultGroupName=中文Git
UninstallDisplayIcon={{app}}\\中文git.exe
OutputDir={发行版位置}
OutputBaseFilename=Chinese_git_Setup_v{{#cngitversion}}
SetupIconFile={os.path.join(os.path.dirname(脚本位置), "ico.ico")}
LicenseFile={os.path.join(os.path.dirname(脚本位置), "LICENSE")}
Compression=lzma2
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\\ChineseSimplified.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\\Japanese.isl"

[Files]
Source: "{打包版位置}\\*"; DestDir: "{{app}}"

[Icons]
Name: "{{group}}\\中文Git"; Filename: "{{app}}\\中文git.exe"

[Run]
Filename: "{{sys}}\\cmd.exe"; Parameters: "/C setx PATH ""{{app}};%PATH%"" /M"; Flags: runhidden

[UninstallRun]
Filename: "{{sys}}\\cmd.exe"; Parameters: "/C setx PATH ""%PATH:{{app}};=%"" /M"; Flags: runhidden; RunOnceId: UninstallSetPath
    '''
    try:
        with open(os.path.join(发行版位置, "pack.iss"), 'w') as 文件:
            文件.write(打包文件)
        print(f"{Fore.GREEN}✓{Fore.RESET} 已生成打包用iss文件")
        return True
    except Exception as 错误:
        print(f"{Fore.RED}✕{Fore.RESET} 生成打包用iss文件时出错:\n{Fore.RED}{错误}{Fore.RESET}")
        return False

def 压缩文件夹为7z格式(源码目录, 目标目录, 存档名称):
    try:        
        # 压缩文件夹为7z格式
        with py7zr.SevenZipFile(os.path.join(目标目录, 存档名称 + '.7z'), 'w') as 存档:
            存档.writeall(源码目录, arcname=os.path.basename(源码目录))
        
        print(f"{Fore.GREEN}✓{Fore.RESET} 压缩7z发行版 {Fore.BLUE}{存档名称}{Fore.RESET} 成功")
        return True
    except Exception as 错误:
        print(f"{Fore.RED}✕{Fore.RESET} 压缩7z发行版 {Fore.BLUE}{存档名称}{Fore.RESET} 时出错:\n{Fore.RED}{错误}{Fore.RESET}")
        return False

def 压缩文件夹为zip格式(源码目录, 目标目录, 存档名称):
    try:
        # 压缩文件夹为zip格式
        with zipfile.ZipFile(os.path.join(目标目录, 存档名称 + '.zip'), 'w', zipfile.ZIP_DEFLATED) as 存档:
            for 路径, 目录, 文件 in os.walk(源码目录):
                for 单个文件 in 文件:
                    存档.write(os.path.join(路径, 单个文件), os.path.relpath(os.path.join(路径, 单个文件), 源码目录))
        
        print(f"{Fore.GREEN}✓{Fore.RESET} 压缩zip发行版 {Fore.BLUE}{存档名称}{Fore.RESET} 成功")
        return True
    except Exception as 错误:
        print(f"{Fore.RED}✕{Fore.RESET} 压缩zip发行版 {Fore.BLUE}{存档名称}{Fore.RESET} 时出错:\n{Fore.RED}{错误}{Fore.RESET}")
        return False

def 压缩发行版():
    压缩文件夹为zip格式(打包版位置, 发行版位置, "Chinese_git")
    压缩文件夹为zip格式(源码版位置, 发行版位置, "Chinese_git_py")
    压缩文件夹为7z格式(打包版位置, 发行版位置, "Chinese_git")
    压缩文件夹为7z格式(源码版位置, 发行版位置, "Chinese_git_py")
# -----------


# --- main ---
def 主函数():
    if 克隆():
        if 获取公告():
            if 复制文件():
                if 生成打包文件():
                    压缩发行版()
# ------------

主函数()
input("按 Enter 键退出...")

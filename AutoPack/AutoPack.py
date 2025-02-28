import os
import sys
import py7zr
import zipfile
import shutil
import requests
import subprocess
from colorama import init, Fore
# 中文Git发行版自动打包程序

# --- init ---
init(autoreset=True)# 颜色显示
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))# 所在目录
os.chdir(script_dir)# 确保命令执行位置
# ------------

# --- repo config ---
repo = "Chinese_git"
repo_git = f"https://github.com/DuckDuckStudio/{repo}.git"
repo_dir = os.path.join(script_dir, repo)
# -------------------

# --- releases config ---
releases_version = input("请输入Releases版本: ")

## --- uniform tag ---
if releases_version.startswith("v."):
    releases_version = "v" + releases_version[2:]
elif not releases_version.startswith("v"):
    releases_version = "v" + releases_version
## -------------------

pack_releases_dir = os.path.join(script_dir, 'Releases', releases_version, 'Chinese_git')
py_releases_dir = os.path.join(script_dir, 'Releases', releases_version, 'Chinese_git_py')
releases_dir = os.path.join(script_dir, 'Releases', releases_version)

## --- create dir ---
os.makedirs(pack_releases_dir, exist_ok=True)
os.makedirs(py_releases_dir, exist_ok=True)
## ------------------

pack_main = os.path.join(repo_dir, "中文git.exe")
pack_update = os.path.join(repo_dir, "中文git更新程序.exe")
py_main = os.path.join(repo_dir, "中文git.py")
noitce_file = os.path.join(repo_dir, "previous_notice.txt")
license_file = os.path.join(repo_dir, "LICENSE")
config_file = os.path.join(repo_dir, "config.json")
# -----------------------

# --- def ---
def clone():
    result = subprocess.run(["git", "clone", repo_git, "--depth", "1"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{Fore.GREEN}✓{Fore.RESET} 克隆仓库成功")
        return True
    else:
        print(f"{Fore.RED}✕{Fore.RESET} 克隆仓库时出错:\n{Fore.RED}{result.stderr}{Fore.RESET}")
        return False

def get_noitce():
    try:
        response = requests.get("https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/notice/notice.txt")
        response.raise_for_status()
        with open(noitce_file, 'wb') as file:
            file.write(response.content)
        print(f"{Fore.GREEN}✓{Fore.RESET} 获取公告文件 (方法一) 成功")
        return True
    except Exception as e:
        print(f"{Fore.YELLOW}⚠{Fore.RESET} 获取公告文件 (方法一) 时出错:\n{Fore.RED}{e}{Fore.RESET}")
        try:
            result = subprocess.run(["git", "clone", "https://github.com/DuckDuckStudio/yazicbs.github.io.git", "--depth", "1"], capture_output=True, text=True)
            if result.returncode == 0:
                shutil.copy(".\\yazicbs.github.io\\Tools\\chinese_git\\notice\\notice.txt", noitce_file)
                print(f"{Fore.GREEN}✓{Fore.RESET} 获取公告文件 (方法二) 成功")
                return True
            else:
                print(f"{Fore.RED}✕{Fore.RESET} 获取公告文件 (方法二) 时出错:\n{Fore.RED}{result.stderr}{Fore.RESET}")
                return False
        except Exception as e:
            print(f"{Fore.RED}✕{Fore.RESET} 获取公告文件 (方法二) 时出错:\n{Fore.RED}{e}{Fore.RESET}")
            return False

def rename_file(old_name, new_name, dir):
    try:
        old_file = os.path.join(dir, old_name)
        new_file = os.path.join(dir, new_name)
        os.rename(old_file, new_file)
        return True
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 处理文件名时出错:\n{Fore.RED}{e}{Fore.RESET}")
        return False

def copy_file():
    try:
        shutil.copy(pack_main, pack_releases_dir)
        shutil.copy(pack_update, pack_releases_dir)
        # ---
        shutil.copy(py_main, py_releases_dir)
        # ---
        shutil.copy(noitce_file, py_releases_dir)
        shutil.copy(noitce_file, pack_releases_dir)
        # ---
        shutil.copy(license_file, py_releases_dir)
        shutil.copy(license_file, pack_releases_dir)
        # ---
        shutil.copy(config_file, py_releases_dir)
        shutil.copy(config_file, pack_releases_dir)
        # -----
        shutil.copy(pack_main, releases_dir)
        if not rename_file(os.path.basename(pack_main), "Chinese_git.exe", releases_dir):
            return False
        shutil.copy(pack_update, releases_dir)
        if not rename_file(os.path.basename(pack_update), "Pack_Version_Update.exe", releases_dir):
            return False
        shutil.copy(py_main, releases_dir)
        if not rename_file(os.path.basename(py_main), "Chinese_git.py", releases_dir):
            return False
        # -----
        print(f"{Fore.GREEN}✓{Fore.RESET} 复制文件成功")
        return True
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 复制文件时出错:\n{Fore.RED}{e}{Fore.RESET}")
        return False

def generate_iss_file():
    # releases_version 已在前面定义
    if releases_version.startswith('v'):
        iss_version = releases_version[1:]
    iss_file = f'''[Setup]
AppName=中文Git
#define cngitversion "{iss_version}"
AppVersion=v{{#cngitversion}}
VersionInfoVersion={{#cngitversion}}
AppPublisher=DuckStudio
VersionInfoCopyright=Copyright (c) 鸭鸭「カモ」
AppPublisherURL=https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/
DefaultDirName={{autopf}}\\Chinese_git
DefaultGroupName=中文Git
UninstallDisplayIcon={{app}}\\中文git.exe
OutputDir={releases_dir}
OutputBaseFilename=Chinese_git_Setup_v{{#cngitversion}}
SetupIconFile={os.path.join(os.path.dirname(script_dir), "ico.ico")}
LicenseFile={os.path.join(os.path.dirname(script_dir), "LICENSE")}
Compression=lzma2
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\\ChineseSimplified.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\\Japanese.isl"

[Files]
Source: "{pack_releases_dir}\\*"; DestDir: "{{app}}"

[Icons]
Name: "{{group}}\\中文Git"; Filename: "{{app}}\\中文git.exe"

[Run]
Filename: "{{sys}}\\cmd.exe"; Parameters: "/C setx PATH ""{{app}};%PATH%"" /M"; Flags: runhidden

[UninstallRun]
Filename: "{{sys}}\\cmd.exe"; Parameters: "/C setx PATH ""%PATH:{{app}};=%"" /M"; Flags: runhidden; RunOnceId: UninstallSetPath
    '''
    try:
        with open(os.path.join(releases_dir, "pack.iss"), 'w') as file:
            file.write(iss_file)
        print(f"{Fore.GREEN}✓{Fore.RESET} 已生成打包用iss文件")
        return True
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 生成打包用iss文件时出错:\n{Fore.RED}{e}{Fore.RESET}")
        return False

def compress_folder_to_7z(source_folder, target_folder, archive_name):
    try:        
        # 压缩文件夹为7z格式
        with py7zr.SevenZipFile(os.path.join(target_folder, archive_name + '.7z'), 'w') as archive:
            archive.writeall(source_folder, arcname=os.path.basename(source_folder))
        
        print(f"{Fore.GREEN}✓{Fore.RESET} 压缩7z发行版 {Fore.BLUE}{archive_name}{Fore.RESET} 成功")
        return True
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 压缩7z发行版 {Fore.BLUE}{archive_name}{Fore.RESET} 时出错:\n{Fore.RED}{e}{Fore.RESET}")
        return False

def compress_folder_to_zip(source_folder, target_folder, archive_name):
    try:
        # 压缩文件夹为zip格式
        with zipfile.ZipFile(os.path.join(target_folder, archive_name + '.zip'), 'w', zipfile.ZIP_DEFLATED) as archive:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    archive.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), source_folder))
        
        print(f"{Fore.GREEN}✓{Fore.RESET} 压缩zip发行版 {Fore.BLUE}{archive_name}{Fore.RESET} 成功")
        return True
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 压缩zip发行版 {Fore.BLUE}{archive_name}{Fore.RESET} 时出错:\n{Fore.RED}{e}{Fore.RESET}")
        return False

def compress_releases():
    try:
        compress_folder_to_zip(pack_releases_dir, releases_dir, "Chinese_git")
        compress_folder_to_zip(py_releases_dir, releases_dir, "Chinese_git_py")
        compress_folder_to_7z(pack_releases_dir, releases_dir, "Chinese_git")
        compress_folder_to_7z(py_releases_dir, releases_dir, "Chinese_git_py")
        return True
    except:
        return False
# -----------

def jobs_clean_up(step):
    # 按照失败的步骤清理工作文件
    if step == "clone":
        if os.path.exists(repo_dir):
            try:
                shutil.rmtree(pack_releases_dir)
                shutil.rmtree(py_releases_dir)
                shutil.rmtree(repo_dir)
                print(f"{Fore.GREEN}✓{Fore.RESET} 成功清理工作文件")
            except Exception as e:
                print(f"{Fore.RED}✕{Fore.RESET} 清理失败，因为:\n{Fore.RED}{e}{Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}⚠{Fore.RESET} 跳过清理，因为目录 {Fore.BLUE}{repo_dir}{Fore.RESET} 不存在")

# --- main ---
def main():
    try:
        if clone():
            if get_noitce():
                if copy_file():
                    if generate_iss_file():
                        if compress_releases():
                            return 0
            else:
                jobs_clean_up("clone")
        else:
            jobs_clean_up("clone")
        # 如果某个操作失败
        return 1
    except KeyboardInterrupt:
        print(f"{Fore.BLUE}[!]{Fore.RESET} 操作取消")
        return 2
# ------------

sys.exit(main())

import os
import sys
import platform

system = platform.system()
print(f'[WARN] Test flag: System is {system}')
if system == 'Darwin':
    # macOS 系统文件名
    main_exe = '中文git_macos'
    update_exe = '中文git更新程序_macos'
elif system == 'Linux':
    # Linux 系统文件名
    main_exe = '中文git_linux'
    update_exe = '中文git更新程序_linux'
elif system == 'Windows':
    # Windows 系统文件名
    main_exe = '中文git_windows.exe'
    update_exe = '中文git更新程序_windows.exe'
else:
    raise NotImplementedError(f"[ERROR] 未知的操作系统: {system}")

script_path = os.path.dirname(sys.argv[0])

try:
    os.remove(os.path.join(os.path.dirname(script_path), main_exe))
    os.remove(os.path.join(os.path.dirname(script_path), update_exe))
except FileNotFoundError:
    if system == 'Windows':
        print("[WARN] No file need to del.")
    else:
        print("[WARN] 没有需要删除的旧文件")
    sys.exit(0)
except Exception as e:
    if system == 'Windows':
        print(f"[ERROR] Failed to del file(s): {e}")
    else:
        print(f"[ERROR] 删除文件时出错: {e}")
    sys.exit(1)

if system == 'Windows':
    print("[INFO] Successfully del old file(s).")
else:
    print("[INFO] 旧文件删除完成！")

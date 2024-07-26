# 中文Git 用户手册

[![项目展示图](https://duckduckstudio.github.io/yazicbs.github.io/project_photos/Chinese_git.png)](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

项目网站：[[点我前往]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

这是 中文Git 的用户手册，你可以在这里找到一些关于 中文Git 的使用方法。  

## 如何获取
请前往[仓库发行版页](https://github.com/DuckDuckStudio/Chinese_git/releases/)下载最新版中文Git。  
如果你已有中文Git，只是希望更新，请查看条目[如何更新中文Git](#如何更新)。  

### 使用 winget
你也可以使用 _winget_ 来获取中文Git，请留意支持 _winget_ 获取的版本。  
使用以下命令安装:  
```bash
winget install DuckStudio.ChineseGit
```
输出类似这样:  
![1718315176839](https://duckduckstudio.github.io/Chinese_git/image/README/1718315176839.png)  

> [!TIP]
> 使用 _winget_ 获取的不用配置Python。  

> [!TIP]
> 设支持的版本号为n，则 $2.4 \leqslant n \leqslant 2.9$  

## 依赖

### Git

在使用 中文Git 前，你必须先配置好 Git 。中文Git 只是一个帮你用中文命令来执行 Git 命令的工具，不能代替 Git 。  
运行以下命令以检查：  

```bash
git -v
```

如果输出类似于以下内容，则说明无需进行更改：  

```
C:\Users\user_name>git -v
git version 2.42.0.windows.1
```

如果无法执行命令:  
* 未下载 Git  
请 [下载Git](https://git-scm.com/downloads) 。
* 已下载 Git  
请 **将Git添加到环境变量** (方法可自行百度，添加完后若未起效请重启您的设备)  

### Python

如果你希望从源码 (`中文git.py`) 使用 中文Git ，请先配置好 Python。  

运行以下命令以检查:  

```bash
python --version
```

你可能会看到类似这样的输出：  

```
C:\Users\user_name>python --version
Python 3.12.0
```

运行以下命令以安装所需库:  

```bash
pip install -r requirements.txt
```

如果无法执行命令:  
* 未下载 Python 解释器  
请 [下载Python](https://www.python.org/downloads/) 。  
* 已下载 Python 解释器  
请 **将Python添加到环境变量** (具体请参阅[[Q：我该如何添加Python到系统PATH环境变量]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#add-python-to-path))  

在您配置完这些依赖后，您应该就可以正常的使用 中文Git 了。  
目前来看，你似乎可以使用 中文Git 的Python源码来在 Linux 和 macos 系统上运行 中文Git ，但是我没试过，所以不能保证稳定性。  

## 如何使用
### 优化
每次都要输这么多的命令...烦死了。  
我们来优化一下命令吧！  
1. 新建一个文件夹，名称随意(这里假设叫`Chinese_git_Script`。~~很复杂也没事，反正命令用不到~~)
2. 在文件夹中新建一个叫`中文git.ps1`的脚本，并在脚本中添加以下内容:  
  - 对于 **py版** :  
  ```powershell
  param(
      [string]$command,
      [string[]]$inputArgs
  )

  python "D:\中文Git的完整路径\中文git.py" $command $inputArgs
  ```
  > [!WARNING]
  > 如果你创建了虚拟Python环境，请将`python`改为虚拟环境中的`python.exe`。  
  > 示例:  
  > ```powershell
  > param(
  >     [string]$command,
  >     [string[]]$inputArgs
  > )
  > $venv_python = "D:\虚拟环境路径\Scripts\python.exe"
  > $scriptPath = "D:\完整路径\中文git.py"
  > & $venv_python $scriptPath $command $inputArgs
  > ```
  - 对于 **打包版** :  
  ```powershell
  param(
      [string]$command,
      [string[]]$inputArgs
  )

  D:\中文Git的完整路径\中文git.exe $command $inputArgs
  ```
  也可以对更新程序的命令进行简化，如果你有需要的话。新建一个`更新中文git.ps1`，并添加以下内容:  
  ```powershell
  param(
      [string]$command,
      [string[]]$inputArgs
  )

  D:\打包版中文Git的更新程序的完整路径\中文git更新程序.exe $command $inputArgs
  ```
3. 将我们前面新建好的目录添加到系统环境变量`PATH`中。  
   类似的具体操作请参阅 [[芙芙工具箱] Q：我该如何添加python到系统PATH环境变量](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/常见问题Q&A/主程序/index.html#add-python-to-path)  
4. 重启你的设备。
5. 验证  
   运行以下命令以验证配置:  
   ```bash
   中文git 版本
   ```
   你应该会看到如下输出:  
   ```
   中文Git by 鸭鸭「カモ」
   版本：v2.x
   安装在: D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git\Script\中文git\中文git.py
   git version 2.42.0.windows.1
   
   ```
   *(版本不一样没关系)*  

这样，你就可以不用在每次执行 中文Git 时都使用完整路径了，您只需使用以下代码即可:  
```powershell
中文git 命令
```
请将`命令`替换为你需要执行的 中文Git 的命令，详细可用命令请查看下方的 [可用命令](#可用命令) 条目  

## 可用命令
以下是 中文Git 目前的可用命令，如需添加更多命令请提交 Issues 或者 PR  
关于如何贡献，请查看[CONTRIBUTING](https://github.com/DuckDuckStudio/Chinese_git/blob/main/CONTRIBUTING.md)文件。  

> [!TIP]
> 这里的可用命令为仓库中最新版本的可用命令，每个Releases的可用命令请查看对应的tag的README/README_DEV/USER_HANDBOOK。  
> 例如(v1.8的可用命令):  
> [https://github.com/DuckDuckStudio/Chinese_git/blob/**v1.8**/USER_HANDBOOK.md#可用命令](https://github.com/DuckDuckStudio/Chinese_git/blob/v1.8/USER_HANDBOOK.md#可用命令)  

| 在中文Git中的命令 | 在Git中的命令    | 用途                               |
| ------------ | ------------------- | ---------------------------------- |
| 拉取         | pull                | 从远程仓库拉取源码                 |
| 推送         | push                | 将本地仓库中的提交推送到远程仓库中 |
| 提交         | commit -m           | 提交您的更改                       |
| 新建分支     | checkout -b         | 创建一个全新的分支                 |
| 切换分支 / 签出到 | checkout        | 切换到另一个分支                   |
| 合并         | merge               | 合并分支（可能会产生冲突）         |
| 暂存         | add                 | 暂存您的修改以备提交               |
| 状态     | status              | 查看当前仓库状态                   |
| 日志     | log                 | 查看提交日志                       |
| 删除分支 (+确认) | branch -D(-d)   | 删除指定分支(+合并检查)             |
| 远程地址     | remote -v           | 查看远程仓库地址                   |
| 远程分支 | branch -r           | 查看远程仓库的分支列表             |
| 版本         | -v                  | 显示中文Git版本和Git版本           |
| 克隆         | clone               | 克隆远程仓库到本地                 |
| 图形化日志 | log --graph        | 查看图形化的提交日志                |
| 是否忽略      | check-ignore -v    | 检查文件/文件夹是否被`.gitignore`忽略 |
| 初始化        | init               | 初始化一个新的 Git 仓库             |
| 本地分支 (+最新提交 +与上游分支关系) | branch (-v/-vv) | 列出所有本地分支(+最新提交 +与上游分支关系) |
| 强推          | push --force       | 将本地仓库的提交**强制**推送到远程仓库中 |
| 更名分支      | branch -m          | 修改本地仓库分支名                  |
| 更新          | /                  | 更新 中文Git                       |
| 还原          | revert             | 新建一个提交来撤销指定提交所做的更改 |
| 重置 (+保留更改(默认)/+删除更改) | reset (--mixed/--hard) | 移动 HEAD 指针以及修改暂存区和工作目录中的文件状态 |
| 公告         | /                  | 显示中文Git版本的最新公告           |
| 差异         | diff                | 显示文件间的差异                   |
| 清理引用 | remote prune origin | 清除在远程仓库中不存在的分支        |

> [!NOTE]
> 对于`提交`命令，如果提交信息带空格请用`"`将提交信息括起来  
> 对于`新建分支`命令，该命令会在新建完分支后自动签出到新分支  

## 如何更新
- 对于`v1.6`及以下版本:  
  把你旧的 中文Git 删掉换成新的 中文Git 就行。  
- 对于`v1.7`-`v2.3`版本:  
  - py版  
  运行命令`中文git 更新`。  
  - 打包版  
  把你旧的 中文Git 删掉换成新的 中文Git 就行。  
- 对于`v2.4`及以上版本:  
  运行命令`中文git 更新`。  

> [!NOTE]
> 如果你使用`v2.4`及以上版本的**打包版**中文Git，则你可以`cd`到安装目录后运行`.\Pack_Version_Update.exe --version vx.y`手动更新中文Git到指定版本，请将命令中的`vx.y`替换为你需要更新到的版本。  

## 配置文件说明
默认配置文件 *(v2.9)* 如下:  
```json
{
    "information": {
        "version": "v2.9"
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
```

- `information` → 关于程序与配置文件的信息
  - `version` → 配置文件对应的程序版本 *(暂未使用)*
- `application` → 关于程序的设置
  - `notice` → 关于公告的信息 *(暂未使用)*
    - `time` → 最新公告的发布时间 *(暂未使用)*
    - `level` → 最新公告的等级 *(暂未使用)*
    - `content` → 最新公告的内容 *(暂未使用)*
  - `run` → 关于运行时的设置
    - `auto_check_update` → 是否在每次执行完命令后都检查更新 (默认为`True`，不为`True`时不自动检查) - 禁用该功能可大幅提升运行速度，但将失去自动更新检查功能
    - `auto_get_notice` → 是否在每次执行完命令后都获取最新公告 (默认为`True`，不为`True`时不自动获取) - 禁用该功能可大幅提升运行速度，但将失去自动公告获取

## 已知问题

请见[Issues页](https://github.com/DuckDuckStudio/Chinese_git/issues)。

## 关于编码
中文Git 的所有项目文件源码以及发行版文件均使用 UTF-8 编码，如出现乱码请使用 UTF-8 编码而非简体中文系统默认的 GBK 编码。

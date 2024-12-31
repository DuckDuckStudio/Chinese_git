# 中文Git

[![项目展示图](https://duckduckstudio.github.io/yazicbs.github.io/project_photos/Chinese_git.png)](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

项目网站：[[点我前往]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

> [!NOTE]
> 想要贡献更新这些文档以及中文Git项目？请查看[CONTRIBUTING](https://github.com/DuckDuckStudio/Chinese_git/blob/main/CONTRIBUTING.md)文件。感谢您的支持！您的支持是我们持续维护的动力！  
> 项目遵循 GPL-2.0 许可协议。  

## 项目介绍

中文Git是一个简单的工具，旨在使不熟悉英文的用户更轻松地使用Git。  
通过中文Git，您可以使用中文命令执行常见的Git操作，无需再背诵英文指令！  

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
> 设支持的版本号为n，则 $2.4 \leqslant n \leqslant 2.10$  
> winget会错误的将版本2.10显示为版本2.1，更多信息请见[microsoft/winget-pkgs#196868](https://github.com/microsoft/winget-pkgs/issues/196868)  

## 项目依赖

在使用中文Git之前，请确保您满足以下依赖，否则中文Git将无法正常工作。  

### Python

请确保您的系统已配置Python环境，并已安装所需库。  
运行以下命令检查Python版本：

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

如果无法运行命令，请参考芙芙工具箱文档中的[[Q：我该如何添加Python到系统PATH环境变量]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#add-python-to-path)  

### Git

请确保您的系统已经配置了Git。  
Git是一个版本管理工具...(省略一大段介绍，您也知道的)...在使用中文Git之前，必须配置好Git。  
运行以下命令检查Git版本：

```bash
git -v
```

如果输出类似于以下内容，则说明无需进行更改：  

```
git version 2.47.1.windows.1
```

如果无法运行命令，请[下载Git](https://git-scm.com/downloads)。如果已经下载了Git但无法运行命令，请将Git添加到环境变量中。（配置方法与Python相同，请参考官方文档[https://git-scm.com/book/zh/v2](https://git-scm.com/book/zh/v2%EF%BC%89)）  

> [!NOTE]
> 即使使用打包版，此项也是必须的。

## 如何执行命令

通常情况下，您可以使用以下命令执行中文Git：  

```bash
python 中文git.py 命令
```

如果您使用的是已打包好的中文Git，则使用以下命令：  

```bash
path\to\中文git.exe 命令
```

> [!NOTE]
> 在使用 python 运行 中文Git 时，请确保 中文git.py 的路径正确！可以使用相对路径。  
> 在使用 打包后的中文Git.exe 运行时，请使用绝对路径  

### 优化
每次都要输这么多的命令...烦死了。  
我们来优化一下命令吧！

#### 打包版
1. 将程序目录添加到系统环境变量`PATH`中。  
   类似的具体操作请参阅 [[芙芙工具箱] Q：我该如何添加python到系统PATH环境变量](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/常见问题Q&A/主程序/index.html#add-python-to-path)  
2. 重启你的设备
3. 验证  
   运行以下命令以验证配置:  
   ```bash
   中文git 版本
   ```
   你应该会看到如下输出:  
   ```
   中文Git by 鸭鸭「カモ」
   版本：v2.x
   安装在: D:\...\Chinese_git\中文git.exe
   git version 2.47.1.windows.1
   
   ```
   *(版本不一样没关系)*  

#### 源码
> [!WARNING]
> 此方法可能仅对只传入一个参数时才有效，更多信息请见[DuckDuckStudio/Fufu_Tools#97](https://github.com/DuckDuckStudio/Fufu_Tools/issues/97)    

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
3. 将我们前面新建好的目录添加到系统环境变量`PATH`中。  
   类似的具体操作请参阅 [[芙芙工具箱] Q：我该如何添加python到系统PATH环境变量](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/常见问题Q&A/主程序/index.html#add-python-to-path)  
4. 重启你的设备
5. 验证  
   运行以下命令以验证配置:  
   ```bash
   中文git 版本
   ```
   你应该会看到如下输出:  
   ```
   中文Git by 鸭鸭「カモ」
   版本：v2.x
   安装在: D:\...\Chinese_git\中文git.py
   git version 2.47.1.windows.1
   
   ```
   *(版本不一样没关系)*  

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

> [!TIP]  
> 如果 winget 上有可用的新版本的话，你也可以试试这个命令:  
> ```bash
> winget update --id DuckStudio.ChineseGit
> ```

> [!NOTE]
> 如果你使用`v2.4`及以上版本的**打包版**中文Git，则你可以`cd`到安装目录后运行`.\Pack_Version_Update.exe --version vx.y`手动更新中文Git到指定版本，请将命令中的`vx.y`替换为你需要更新到的版本。  
> 请注意，自 v2.4 起，中文git的更新程序默认认为中文git叫`中文git.py`或`中文git.exe`，并不是GitHub发行版上的`Chinese_git.py`或`Chinese_git.exe`。  

## 可用命令

以下是中文Git支持的命令列表。如果您需要的Git命令不在列表中，请[提交Issues](https://github.com/DuckDuckStudio/Chinese_git/issues)告诉我们！  

> [!TIP]
> 这里的可用命令为仓库中最新版本的可用命令，每个Releases的可用命令请查看对应的tag的`README/README_DEV/USER_HANDBOOK`。  
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
| 远程分支      | branch -r          | 查看远程仓库的分支列表               |
| 所有分支      | branch -a          | 查看仓库的所有分支列表               |
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

### 示例

```bash
$ python 中文git.py 暂存 所有
$ python 中文git.py 提交 更新README
$ python 中文git.py 推送
```

输出如下：  

```
[Power by 虚空终端] PS D:\...\Chinese_git> python 中文git.py 暂存 所有

[Power by 虚空终端] PS D:\...\Chinese_git> python 中文git.py 提交 更新README
[main 11bef48] 更新README
 2 files changed, 200 insertions(+), 1 deletion(-)
 create mode 100644 "\344\270\255\346\226\207git.py"

[Power by 虚空终端] PS D:\...\Chinese_git> python 中文git.py 推送
错误: fatal: unable to access 'https://github.com/DuckDuckStudio/Chinese_git.git/': Failure when receiving data from the peer
```

## 已知问题

请见[Issues页](https://github.com/DuckDuckStudio/Chinese_git/issues)。

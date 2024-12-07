# 中文Git

[![项目展示图](https://duckduckstudio.github.io/yazicbs.github.io/project_photos/Chinese_git.png)](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

[![GitHub Release](https://img.shields.io/github/release/DuckDuckStudio/Chinese_git?style=flat)](https://github.com/DuckDuckStudio/Chinese_git/releases/latest) [![Github All Releases](https://img.shields.io/github/downloads/DuckDuckStudio/Chinese_git/total.svg?style=flat)]() [![Github LICENSE](https://img.shields.io/github/license/DuckDuckStudio/Chinese_git?style=flat)]()  

项目网站：[[点我前往]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

你还在为忘记 git 的命令而发愁吗？  
你还要每次执行 git 命令都要去搜索吗？  
机会来了！使用中文Git，这些统统不是问题!  
~~赶紧拿起电话订购吧！~~  

> [!NOTE]
> 本 README 文件内容为直白讲述，如果看不惯请查看 [README_DEV](https://github.com/DuckDuckStudio/Chinese_git/blob/main/README_DEV.md) 文件。  
> 如果你希望协助更新这些文档以及 中文Git ，请查看[CONTRIBUTING](https://github.com/DuckDuckStudio/Chinese_git/blob/main/CONTRIBUTING.md)文件。感谢您的支持！您的支持是我们继续维护的动力！  
> 项目LICENSE：GPL-2.0  
> 你也可以查看 中文Git 的[用户手册](https://github.com/DuckDuckStudio/Chinese_git/blob/main/USER_HANDBOOK.md)来了解更多信息。  

## 项目介绍
中文Git 是一个使用中文命令操作 Git 的简单工具，旨在使不熟悉英文的用户更轻松地使用 Git。  
使用 中文Git 可以使用中文指令进行常见的 Git 操作，再也不用去背英文啦！  

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
> 设支持的版本号为n，则 $2.4 \leqslant n \leqslant 2.10$  
> winget会错误的将版本2.10显示为版本2.1，更多信息请见[microsoft/winget-pkgs#196868](https://github.com/microsoft/winget-pkgs/issues/196868)  

## 项目依赖
在使用 中文Git 前，请确保你有以下依赖，否则 中文Git 将变成废物。  

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

如果你无法运行指令，请参阅芙芙工具箱文档(懒得再写一个文档了)中的[[Q：我该如何添加python到系统PATH环境变量]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#add-python-to-path)  

对于实在是不会配置(或者根本就是懒)的人，也有个备选方案，你可以前往仓库发行版下载最新版本的压缩包，里面包含打包好的 中文Git.exe 程序。但在执行命令时可能会不一样，详细请参阅下面的[如何执行命令](#如何执行命令)。  
> [!TIP]
> 使用 _winget_ 获取的不用配置Python。  

### Git
请确保你的设备中已配置 Git 。  
Git是一个版本管理工具...(省略一堆介绍，反正你也知道)...在使用 中文Git 前必须配置 Git 。  
运行以下命令以检查：
```bash
git -v
```
如果你看到类似这样的输出则表明你不用管他了：  
```
git version 2.47.1.windows.1
```
如果你无法运行命令，请[下载Git](https://git-scm.com/downloads)。如果你已下载Git还无法运行命令，请添加Git到环境变量。(看我干嘛，我又没在[官方文档](https://git-scm.com/book/zh/v2)中找到如何配置，上面的 Python 怎么配置的 Git 就怎么配置)
> [!IMPORTANT]
> 此项为必须，即使你使用打包版

## 如何执行命令

一般情况下，你可以使用以下这个命令来使用 中文Git :  
```bash
python 中文git.py 命令
```
如果你使用的是打包好的 中文Git ，请用以下命令来使用 中文Git :  
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

这些是在 中文Git 中可以使用的命令，如果你需要的 Git 命令在这里没有列出...快点[提交Issues](https://github.com/DuckDuckStudio/Chinese_git/issues)听见没！搞快点！  

> [!TIP]
> 这里的可用命令为仓库中最新版本的可用命令，每个Releases的可用命令请查看对应的tag的`README/README_DEV/USER_HANDBOOK`。  
> 例如(v1.8的可用命令):  
> [https://github.com/DuckDuckStudio/Chinese_git/blob/**v1.8**/USER_HANDBOOK.md#可用命令](https://github.com/DuckDuckStudio/Chinese_git/blob/v1.8/USER_HANDBOOK.md#可用命令)  

| 现在叫啥 | 原来长啥样 | 干啥的 |
|-----|-----|-----|
| 拉取 | pull | 从远程仓库拉取源码 |
| 推送 | push | 将本地仓库中的提交推送到远程仓库中 |
| 提交 | commit -m | 提交你的更改 |
| 新建分支 | checkout -b | 创建一个全新的分支 |
| 切换分支 / 签出到 | checkout | 我不在这个分支写了！我要去另一个分支写！ |
| 合并 | merge | 混合在一起~ (可能有问题) |
| 暂存 | add | ~~我就只暂存，就是不提交。欸~就是玩~~ 将你的修改暂时存起来以备提交 |
| 状态 | status | 让我看看！看看你是什么状态！ |
| 日志 | log | 让我看看！看看你之前都提交了什么玩意 |
| 删除分支 (+确认) | branch -D(-d) | 这个家没有你(删除的分支)的位置了！ |
| 远程地址 | remote -v | 你在另一头(远程)叫什么，住哪里(链接) |
| 远程分支 | branch -r | 你在另一头(远程)有谁(哪些分支) |
| 所有分支 | branch -a | 列出仓库的所有分支 |
| 版本 | -v | 如命令所示，显示你使用的 中文Git 版本与 Git 版本 |
| 克隆 | clone | 你的代码就是我的！我的代码还是我的！ |
| 图形化日志 | log --graph | 查看图形化的提交日志 |
| 是否忽略 | check-ignore -v | 看看我有没有把你丢掉 |
| 初始化 | init | 新 宠 |
| 本地分支 (+最新提交 +与上游分支关系) | branch (-v/-vv) | 列出所有本地分支(+最新提交 +与上游分支关系) |
| 强推 | push --force | 让我先拉取再推送？我就不！ |
| 更名分支 | branch -m | 我不叫旧分支名了，我要叫新分支名！ |
| 更新 | / | 我要玩新的中文Git嘛~ |
| 还原 | revert | 还是以前的好 |
| 重置 (+保留更改(默认)/+删除更改) | reset (--mixed/--hard) | 把我推到过去，让我重来一次！ |
| 公告 | / | 没人比我更懂中文Git |
| 差异 | diff | 找 不 同 ~ |
| 清理引用 | remote prune origin | 清除在远程仓库中不存在的分支 |

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
[Powered by 虚空终端] PS D:\...\Chinese_git> python 中文git.py 暂存 所有

[Powered by 虚空终端] PS D:\...\Chinese_git> python 中文git.py 提交 更新README
[main 11bef48] 更新README
 2 files changed, 200 insertions(+), 1 deletion(-)
 create mode 100644 "\344\270\255\346\226\207git.py"

[Powered by 虚空终端] PS D:\...\Chinese_git> python 中文git.py 推送
错误: fatal: unable to access 'https://github.com/DuckDuckStudio/Chinese_git.git/': Failure when receiving data from the peer
```
~~可以看到推送失败了(倒~~  

## 已知问题

请见[Issues页](https://github.com/DuckDuckStudio/Chinese_git/issues)。

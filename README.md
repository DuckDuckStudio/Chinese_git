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

## 项目依赖
在使用 中文Git 前，请确保你有以下依赖，否则 中文Git 将变成废物。  

### Python
请确保你的设备已配置 Python 环境并且已将 Python 添加到系统环境变量中。  
运行以下命令以检查：
```bash
python --version
```
如果你看到类似这样的输出则表明你不用管他了：  
```
C:\Users\user_name>python --version
Python 3.12.0
```
如果你无法运行指令，请参阅芙芙工具箱文档(懒得再写一个文档了)中的[[Q：我该如何添加python到系统PATH环境变量]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#add-python-to-path)  

对于实在是不会配置(或者根本就是懒)的人，也有个备选方案，你可以前往仓库发行版下载最新版本的压缩包，里面包含打包好的 中文Git.exe 程序。但在执行命令时可能会不一样，详细请参阅下面的[如何执行命令](#如何执行命令)。  

### Git
请确保你的设备中已配置 Git 。  
Git是一个版本管理工具...(省略一堆介绍，反正你也知道)...在使用 中文Git 前必须配置 Git 。  
运行以下命令以检查：
```bash
git -v
```
如果你看到类似这样的输出则表明你不用管他了：  
```
C:\Users\user_name>git -v
git version 2.42.0.windows.1
```
如果你无法运行命令，请[下载Git](https://git-scm.com/downloads)。如果你已下载Git还无法运行命令，请添加Git到环境变量。(看我干嘛，我又没在[官方文档](https://git-scm.com/book/zh/v2)中找到如何配置，上面的 Python 怎么配置的 Git 就怎么配置)
> [!NOTE]
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

如果你希望在使用 打包后的中文Git.exe 时不用每次都输入绝对路径，请执行以下代码：  
在 PowerShell 中:  
```powershell
New-Alias 中文git "中文git.exe的绝对路径"
```
在 cmd 中:  
```bash
doskey 中文git="中文git.exe的绝对路径"
```
仅本次会话有效，除非将以上代码添加进配置文件。  
PowerShell 的配置文件请在 PowerShell 中运行以下命令打开:  
```powershell
notepad $PROFILE
```
如果文件不存在，请在`C:\Users\user_name\Documents\WindowsPowerShell\`中创建一个叫`Microsoft.PowerShell_profile.ps1`的文件，然后再试一次(文件夹也不存在的也是新建)。  
如果出现错误：请参考[[Powered by 虚空终端]项目的描述](https://github.com/DuckDuckStudio/powered_by_akasha_terminal/blob/main/README.md#if-error)<div id="tp-point"></div>(其实就是懒得再写遍文档)  

## 如何更新
- 对于`v1.6`及以下版本:  
  把你旧的 中文Git 删掉换成新的 中文Git 就行。  
- 对于`v1.7`及以上版本:  
  运行命令`中文git 更新`。  
  *(请将`中文git`替换为`中文Git.exe`的路径或`python 中文Git.py`)*  

## 可用命令

这些是在 中文Git 中可以使用的命令，如果你需要的 Git 命令在这里没有列出...快点[提交Issues](https://github.com/DuckDuckStudio/Chinese_git/issues)听见没！搞快点！  

| 现在叫啥 | 原来长啥样 | 干啥的 |
|-----|-----|-----|
| 拉取 | pull | 从远程仓库拉取源码 |
| 推送 | push | 将本地仓库中的提交推送到远程仓库中 |
| 提交 | commit -m | 提交你的更改 |
| 新建分支 | checkout -b | 创建一个全新的分支 |
| 切换分支 / 签出到 | checkout | 我不在这个分支写了！我要去另一个分支写！ |
| 合并 | merge | 混合在一起~ (可能有问题) |
| 暂存 | add | ~~我就只暂存，就是不提交。欸~就是玩~~ 将你的修改暂时存起来以备提交 |
| 查看状态 | status | 让我看看！看看你是什么状态！ |
| 查看日志 | log | 让我看看！看看你之前都提交了什么玩意 |
| 删除分支 (+确认) | branch -D(-d) | 这个家没有你(删除的分支)的位置了！ |
| 远程地址 | remote -v | 你在另一头(远程)叫什么，住哪里(链接) |
| 查看远程分支 | branch -r | 你在另一头(远程)有谁(哪些分支) |
| 版本 | -v | 如命令所示，显示你使用的 中文Git 版本与 Git 版本 |
| 删除提交 | reset --hard HEAD~n | 我！不！提！交！了！ |
| 克隆 | clone | 你的代码就是我的！我的代码还是我的！ |
| 配置 | config | 听我说~ |
| 查看图形化日志 | log --graph | 查看图形化的提交日志 |
| 是否忽略 | check-ignore -v | 看看我有没有把你丢掉 |
| 初始化 | init | 新 宠 |
| 查看本地分支 (+最新提交 +与上游分支关系) | branch (-v/-vv) | 列出所有本地分支(+最新提交 +与上游分支关系) |
| 强推 | push --force | 让我先拉取再推送？我就不！ |
| 更名分支 | branch -m | 我不叫旧分支名了，我要叫新分支名！ |
| 更新 | / | 我要玩新的中文Git嘛~ |

> [!NOTE]
> 对于`配置`命令，请将配置范围放在**第三个参数**  
> 对于`提交`命令，如果**提交信息带空格请用`"`将提交信息括起来**  
> 对于`新建分支`命令，该命令会在新建完分支后**自动签出到新分支**  
> 对于`查看本地分支`命令的参数，示例`$ 中文git 查看本地分支 +最新提交 +与上游分支关系`  
> 对于`删除分支`命令，如果不加参数的话是**强制的**，不管你要删除的分支有没有被合并。如果需要预先检查请执行`$ 中文git 删除分支 branch +确认`  

### 示例

```bash
$ python 中文git.py 暂存 所有
$ python 中文git.py 提交 更新README
$ python 中文git.py 推送
```

输出如下：  

```
[Powered by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 暂存 所有

[Powered by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 提交 更新README
[main 11bef48] 更新README
 2 files changed, 200 insertions(+), 1 deletion(-)
 create mode 100644 "\344\270\255\346\226\207git.py"

[Powered by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 推送
错误: fatal: unable to access 'https://github.com/DuckDuckStudio/Chinese_git.git/': Failure when receiving data from the peer
```
~~可以看到推送失败了(倒~~  

## 已知问题

以下是 中文Git 目前的已知问题：  
* [在未暂存任何内容时提交 中文Git 会提示错误但不给出任何错误信息 Issues#3](https://github.com/DuckDuckStudio/Chinese_git/issues/3)
* 打包版在 Windows7 上可能无法运行 - 可能的解决方案：使用 Nuitka 打包
* 在非 utf-8 编码的设备上解压版本发行版压缩包可能会出现乱码 - 可能的解决方案：使用 Bandizip 解压
* 在使用 中文Git 执行部分命令时不会有输出，但命令成功执行
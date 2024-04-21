# 中文Git

![项目展示图](https://duckduckstudio.github.io/yazicbs.github.io/porject_photos/Chinese_git.png)

你还在为忘记 git 的命令而发愁吗？<br>
你还要每次执行 git 命令都要去搜索吗？<br>
机会来了！使用中文Git，这些统统不是问题!<br>
~~赶紧拿起电话订购吧！~~<br>

> [!NOTE]
> 本 README 文件内容为直白讲述，如果看不惯请查看 [README_DEV](https://github.com/DuckDuckStudio/Chinese_git/blob/main/README_DEV.md) 文件。<br>
> 如果你希望协助更新这些文档以及 中文Git ，请查看[CONTRIBUTING](https://github.com/DuckDuckStudio/Chinese_git/blob/main/CONTRIBUTING.md)文件。感谢您的支持！您的支持是我们继续维护的动力！<br>
> 项目LICENSE：MIT<br>

## 项目介绍
中文Git 是一个使用中文命令操作 Git 的简单工具，旨在使不熟悉英文的用户更轻松地使用 Git。<br>
使用 中文Git 可以使用中文指令进行常见的 Git 操作，再也不用去背英文啦！<br>

## 项目依赖
在使用 中文Git 前，请确保你有以下依赖，否则 中文Git 将变成废物。<br>

### Python
请确保你的设备已配置 Python 环境并且已将 Python 添加到系统环境变量中。<br>
运行以下命令以检查：
```bash
python --version
```
如果你看到类似这样的输出则表明你不用管他了：<br>
```
C:\Users\user_name>python --version
Python 3.12.0
```
如果你无法运行指令，请参阅芙芙工具箱文档(懒得再写一个文档了)中的[[Q：我该如何添加python到系统PATH环境变量]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#add-python-to-path)<br>

对于实在是不会配置(或者根本就是懒)的人，也有个备选方案，你可以前往仓库发行版下载最新版本的已经打包好的 中文Git 程序，但在执行命令时可能会不一样，详细请参阅下面的[如何执行命令](#如何执行命令)。<br>

### Git
请确保你的设备中已配置 Git 。<br>
Git是一个版本管理工具...(省略一堆介绍，反正你也知道)...在使用 中文Git 前必须配置 Git 。<br>
运行以下命令以检查：
```bash
git -v
```
如果你看到类似这样的输出则表明你不用管他了：<br>
```
C:\Users\user_name>git -v
git version 2.42.0.windows.1
```
如果你无法运行命令，请[下载Git](https://git-scm.com/downloads)。如果你已下载Git还无法运行命令，请添加Git到环境变量。(看我干嘛，我又没在[官方文档](https://git-scm.com/book/zh/v2)中找到如何配置，上面的 Python 怎么配置的 Git 就怎么配置)
> [!NOTE]
> 此项为必须，即使你使用打包版

## 如何执行命令

一般情况下，你可以使用以下这个命令来使用 中文Git :<br>
```bash
python 中文git.py 命令
```
如果你使用的是打包好的 中文Git ，请用以下命令来使用 中文Git :<br>
```bash
path\to\中文git.exe 命令
```

> [!NOTE]
> 在使用 python 运行 中文Git 时，请确保 中文git.py 的路径正确！可以使用相对路径。<br>
> 在使用 打包后的中文Git.exe 运行时，请使用绝对路径<br>

如果你希望在使用 打包后的中文Git.exe 时不用每次都输入绝对路径，请执行以下代码：<br>
在 PowerShell 中:<br>
```powershell
New-Alias 中文git "中文git.exe的绝对路径"
```
在 cmd 中:<br>
```bash
doskey 中文git="中文git.exe的绝对路径"
```
仅本次会话有效，除非将以上代码添加进配置文件。<br>
PowerShell 的配置文件请在 PowerShell 中运行以下命令打开:<br>
```powershell
notepad $PROFILE
```
如果文件不存在，请在`C:\Users\user_name\Documents\WindowsPowerShell\`中创建一个叫`Microsoft.PowerShell_profile.ps1`的文件，然后再试一次(文件夹也不存在的也是新建)。<br>
如果出现错误：请参考[[Power by 虚空终端]项目的描述](https://github.com/DuckDuckStudio/power_by_akasha_terminal/blob/main/README.md#if-error)<div id="tp-point"></div>(其实就是懒得再写遍文档)<br>

## 如何更新

把你旧的 中文Git 删掉换成新的 中文Git 就行。<br>

## 可用命令

这些是在 中文Git 中可以使用的命令，如果你需要的 Git 命令在这里没有列出...快点[提交Issues](https://github.com/DuckDuckStudio/Chinese_git/issues)听见没！搞快点！<br>

| 现在叫啥 | 原来长啥样 | 干啥的 |
|-----|-----|-----|
| 拉取 | pull | 从远程仓库拉取源码 |
| 推送 | push | 将本地仓库中的提交推送到远程仓库中 |
| 提交 | commit -m | 提交你的更改 |
| 新建分支 | checkout -b | 创建一个全新的分支 |
| 切换分支 | checkout | 我不在这个分支写了！我要去另一个分支写！ |
| 合并 | merge | 混合在一起~ (可能有问题) |
| 暂存 | add | ~~我就只暂存，就是不提交。欸~就是玩~~ 将你的修改暂时存起来以备提交 |
| 查看状态 | status | 让我看看！看看你是什么状态！ |
| 查看日志 | log | 让我看看！看看你之前都提交了什么玩意 |
| 删除分支 | branch -D | 这个家没有你(删除的分支)的位置了！ |
| 远程地址 | remote -v | 你在另一头(远程)叫什么，住哪里(链接) |
查看远程分支 | branch -r | 你在另一头(远程)有谁(哪些分支) |
| 版本 | -v | 如命令所示，显示你使用的 中文Git 版本与 Git 版本 |
| 删除提交 | reset --hard HEAD~n | 我！不！提！交！了！ |

### 示例

```bash
$ python 中文git.py 暂存 所有
$ python 中文git.py 提交 更新README
$ python 中文git.py 推送
```

输出如下：<br>

```
[Power by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 暂存 所有

[Power by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 提交 更新README
[main 11bef48] 更新README
 2 files changed, 200 insertions(+), 1 deletion(-)
 create mode 100644 "\344\270\255\346\226\207git.py"

[Power by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 推送
错误: fatal: unable to access 'https://github.com/DuckDuckStudio/Chinese_git.git/': Failure when receiving data from the peer
```
~~可以看到推送失败了(倒~~<br>

# 中文Git

[![项目展示图](https://duckduckstudio.github.io/yazicbs.github.io/project_photos/Chinese_git.png)](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

项目网站：[[点我前往]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

> [!NOTE]
> 想要贡献更新这些文档以及中文Git项目？请查看[CONTRIBUTING](https://github.com/DuckDuckStudio/Chinese_git/blob/main/CONTRIBUTING.md)文件。感谢您的支持！您的支持是我们持续维护的动力！  
> 项目遵循 GPL-2.0 许可协议。  

## 项目介绍

中文Git是一个简单的工具，旨在使不熟悉英文的用户更轻松地使用Git。  
通过中文Git，您可以使用中文命令执行常见的Git操作，无需再背诵英文指令！  

## 项目依赖

在使用中文Git之前，请确保您满足以下依赖，否则中文Git将无法正常工作。  

### Python

请确保您的系统已配置Python环境，并已将Python添加到系统环境变量中。  
运行以下命令检查Python版本：

```bash
python --version
```

如果输出类似于以下内容，则说明无需进行更改：  

```
C:\Users\user_name>python --version
Python 3.12.0
```

如果无法运行命令，请参考芙芙工具箱文档中的[[Q：我该如何添加Python到系统PATH环境变量]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#add-python-to-path)  

对于实在是不会配置(或者根本就是懒)的人，也有个备选方案，你可以前往仓库发行版下载最新版本的压缩包，里面包含打包好的 中文Git.exe 程序。但在执行命令时可能会不一样，详细请参阅下面的[如何执行命令](#如何执行命令)。  

### Git

请确保您的系统已经配置了Git。  
Git是一个版本管理工具...(省略一大段介绍，您也知道的)...在使用中文Git之前，必须配置好Git。  
运行以下命令检查Git版本：

```bash
git -v
```

如果输出类似于以下内容，则说明无需进行更改：  

```
C:\Users\user_name>git -v
git version 2.42.0.windows.1
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

以下是中文Git支持的命令列表。如果您需要的Git命令不在列表中，请[提交Issues](https://github.com/DuckDuckStudio/Chinese_git/issues)告诉我们！  

| 在中文Git中的命令 | 在Git中的命令    | 用途                               |
| ------------ | ------------------- | ---------------------------------- |
| 拉取         | pull                | 从远程仓库拉取源码                 |
| 推送         | push                | 将本地仓库中的提交推送到远程仓库中 |
| 提交         | commit -m           | 提交您的更改                       |
| 新建分支     | checkout -b         | 创建一个全新的分支                 |
| 切换分支 / 签出到 | checkout        | 切换到另一个分支                   |
| 合并         | merge               | 合并分支（可能会产生冲突）         |
| 暂存         | add                 | 暂存您的修改以备提交               |
| 查看状态     | status              | 查看当前仓库状态                   |
| 查看日志     | log                 | 查看提交日志                       |
| 删除分支 (+确认) | branch -D(-d)   | 删除指定分支(+合并检查)             |
| 远程地址     | remote -v           | 查看远程仓库地址                   |
| 查看远程分支 | branch -r           | 查看远程仓库的分支列表             |
| 版本         | -v                  | 显示中文Git版本和Git版本           |
| 删除提交     | reset --hard HEAD~n | 撤销n次提交                        |
| 克隆         | clone               | 克隆远程仓库到本地                 |
| 配置         | config              | 配置 Git 的命令行工具              |
| 查看图形化日志 | log --graph        | 查看图形化的提交日志                |
| 是否忽略      | check-ignore -v    | 检查文件/文件夹是否被`.gitignore`忽略 |
| 初始化        | init               | 初始化一个新的 Git 仓库             |
| 查看本地分支 (+最新提交 +与上游分支关系) | branch (-v/-vv) | 列出所有本地分支(+最新提交 +与上游分支关系) |
| 强推          | push --force       | 将本地仓库的提交**强制**推送到远程仓库中 |
| 更名分支      | branch -m          | 修改本地仓库分支名                  |
| 更新          | /                  | 更新 中文Git                       |

> [!NOTE]
> 对于`配置`命令，请将配置范围放在第三个参数  
> 对于`提交`命令，如果提交信息带空格请用`"`将提交信息括起来  
> 对于`新建分支`命令，该命令会在新建完分支后自动签出到新分支  
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
[Power by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 暂存 所有

[Power by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 提交 更新README
[main 11bef48] 更新README
 2 files changed, 200 insertions(+), 1 deletion(-)
 create mode 100644 "\344\270\255\346\226\207git.py"

[Power by 虚空终端] PS D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git> python 中文git.py 推送
错误: fatal: unable to access 'https://github.com/DuckDuckStudio/Chinese_git.git/': Failure when receiving data from the peer
```

## 已知问题

以下是 中文Git 目前的已知问题：  
* [在未暂存任何内容时提交 中文Git 会提示错误但不给出任何错误信息 Issues#3](https://github.com/DuckDuckStudio/Chinese_git/issues/3)
* 打包版在 Windows7 上可能无法运行 - 可能的解决方案：使用 Nuitka 打包
* 在非 utf-8 编码的设备上解压版本发行版压缩包可能会出现乱码 - 可能的解决方案：使用 Bandizip 解压
* 在使用 中文Git 执行部分命令时不会有输出，但命令成功执行
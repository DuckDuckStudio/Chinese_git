# 中文Git 用户手册

[![项目展示图](https://duckduckstudio.github.io/yazicbs.github.io/project_photos/Chinese_git.png)](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

项目网站：[[点我前往]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/)  

这是 中文Git 的用户手册，你可以在这里找到一些关于 中文Git 的使用方法。  

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
目前没有版本要求，因为所用的库只有`subprocess`、`sys`、`os`三个标准库。  

运行以下命令以检查:  

```bash
python --version
```

如果输出类似于以下内容，则说明无需进行更改：  

```
C:\Users\user_name>python --version
Python 3.12.0
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
为了使 中文Git 更加易于使用，这边对使用打包后的 中文Git 的用户提出一些优化建议，以防止每次多余的击键。  
你可以使用 PowerShell 中的配置文件来帮你执行一些操作。  
输入以下命令打开 PowerShell 的配置文件：  
```powershell
notepad $PROFILE
```
如果文件不存在，请在`C:\Users\user_name\Documents\WindowsPowerShell\`中创建一个叫`Microsoft.PowerShell_profile.ps1`的文件，然后再试一次(文件夹也不存在的也是新建)。  
然后在配置文件中添加以下代码:  
```powershell
New-Alias 中文git "中文git.exe的绝对路径"
```
请将代码中的`中文git.exe的绝对路径`换成你设备中的 中文Git(打包后的) 的路径。  
路径要具体到文件名，例如`D:\Duckhome\projects\MSVS\Source\Repos\Chinese_git\中文git.exe`就是一个正确的路径。  
这样，你就可以不用在每次执行 中文Git 时都使用完整路径了，您只需使用以下代码即可:  
```powershell
中文git 命令
```
请将`命令`替换为你需要执行的 中文Git 的命令，详细可用命令请查看下方的 [可用命令](#可用命令) 条目  

### 使用源码(中文git.py)的
如果你使用 中文Git 的源码，则你必须按照以下命令格式使用 中文Git :  
```bash
python 中文git.py 命令
```
请将代码中的`中文git.py`替换成你设备中的 中文git(源码) 的路径(完整路径或相对路径均可)。  
请将`命令`替换为你需要执行的 中文Git 的命令，详细可用命令请查看下方的 [可用命令](#可用命令) 条目  

## 可用命令
以下是 中文Git 目前的可用命令，如需添加更多命令请提交 Issues 或者 PR  
关于如何贡献，请查看[CONTRIBUTING](https://github.com/DuckDuckStudio/Chinese_git/blob/main/CONTRIBUTING.md)文件。  

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
| 克隆         | clone               | 克隆远程仓库到本地                 |
| 配置         | config              | 配置 Git 的命令行工具              |
| 查看图形化日志 | log --graph        | 查看图形化的提交日志                |
| 是否忽略      | check-ignore -v    | 检查文件/文件夹是否被`.gitignore`忽略 |
| 初始化        | init               | 初始化一个新的 Git 仓库             |
| 查看本地分支 (+最新提交 +与上游分支关系) | branch (-v/-vv) | 列出所有本地分支(+最新提交 +与上游分支关系) |
| 强推          | push --force       | 将本地仓库的提交**强制**推送到远程仓库中 |
| 更名分支      | branch -m          | 修改本地仓库分支名                  |
| 更新          | /                  | 更新 中文Git                       |
| 还原          | revert             | 新建一个提交来撤销指定提交所做的更改 |

> [!NOTE]
> 对于`配置`命令，请将配置范围放在第三个参数  
> 对于`提交`命令，如果提交信息带空格请用`"`将提交信息括起来  
> 对于`新建分支`命令，该命令会在新建完分支后自动签出到新分支  
> 对于`查看本地分支`命令的参数，示例`$ 中文git 查看本地分支 +最新提交 +与上游分支关系`  
> 对于`删除分支`命令，如果不加参数的话是**强制的**，不管你要删除的分支有没有被合并。如果需要预先检查请执行`$ 中文git 删除分支 branch +确认`  

## 如何更新
- 对于`v1.6`及以下版本:  
  把你旧的 中文Git 删掉换成新的 中文Git 就行。  
- 对于`v1.7`及以上版本:  
  运行命令`中文git 更新`。  
  *(请将`中文git`替换为`中文Git.exe`的路径或`python 中文Git.py`)*  

## 已知问题
以下是 中文Git 的已知问题，等待修复中...  
* [在未暂存任何内容时提交 中文Git 会提示错误但不给出任何错误信息 Issues#3](https://github.com/DuckDuckStudio/Chinese_git/issues/3)
* 打包版在 Windows7 上可能无法运行 - 可能的解决方案：使用 Nuitka 打包
* 在非 utf-8 编码的设备上解压版本发行版压缩包可能会出现乱码 - 可能的解决方案：使用 Bandizip 解压
* 在使用 中文Git 执行部分命令时不会有输出，但命令成功执行
* [打包版无法使用更新命令更新 #5](https://github.com/DuckDuckStudio/Chinese_git/issues/5)

## 关于编码
中文Git 的所有项目文件源码以及发行版文件均使用 UTF-8 编码，如出现乱码请使用 UTF-8 编码而非简体中文系统默认的 GBK 编码。
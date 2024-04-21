# 中文Git

> [!NOTE]
> 想要贡献更新这些文档以及中文Git项目？请查看[CONTRIBUTING](https://github.com/DuckDuckStudio/Chinese_git/blob/main/CONTRIBUTING.md)文件。感谢您的支持！您的支持是我们持续维护的动力！<br>
> 项目遵循MIT许可协议。<br>

## 项目介绍

中文Git是一个简单的工具，旨在使不熟悉英文的用户更轻松地使用Git。<br>
通过中文Git，您可以使用中文命令执行常见的Git操作，无需再背诵英文指令！<br>

## 项目依赖

在使用中文Git之前，请确保您满足以下依赖，否则中文Git将无法正常工作。<br>

### Python

请确保您的系统已配置Python环境，并已将Python添加到系统环境变量中。<br>
运行以下命令检查Python版本：

```bash
python --version
```

如果输出类似于以下内容，则说明无需进行更改：<br>

```
C:\Users\user_name>python --version
Python 3.12.0
```

如果无法运行命令，请参考芙芙工具箱文档中的[[Q：我该如何添加Python到系统PATH环境变量]](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#add-python-to-path)<br>

对于不了解配置或者懒得配置的用户，我提供了另一种选择。您可以前往仓库的发行版页面下载最新版本的已打包好的中文Git程序。但是请注意，使用打包版时可能需要略微不同的命令，详细信息请参阅[如何执行命令](#如何执行命令)。<br>

### Git

请确保您的系统已经配置了Git。<br>
Git是一个版本管理工具...(省略一大段介绍，您也知道的)...在使用中文Git之前，必须配置好Git。<br>
运行以下命令检查Git版本：

```bash
git -v
```

如果输出类似于以下内容，则说明无需进行更改：<br>

```
C:\Users\user_name>git -v
git version 2.42.0.windows.1
```

如果无法运行命令，请[下载Git](https://git-scm.com/downloads)。如果已经下载了Git但无法运行命令，请将Git添加到环境变量中。（配置方法与Python相同，请参考官方文档[https://git-scm.com/book/zh/v2](https://git-scm.com/book/zh/v2%EF%BC%89)）<br>

> [!NOTE]
> 即使使用打包版，此项也是必须的。

## 如何执行命令

通常情况下，您可以使用以下命令执行中文Git：<br>

```bash
python 中文git.py 命令
```

如果您使用的是已打包好的中文Git，则使用以下命令：<br>

```bash
path\to\中文git.exe 命令
```

> [!NOTE]
> 在使用 python 运行 中文Git 时，请确保 中文git.py 的路径正确！可以使用相对路径。<br>
> 在使用 打包后的中文Git.exe 运行时，请使用绝对路径<br>

## 如何更新

将旧版中文Git替换为新版中文Git即可。<br>

## 可用命令

以下是中文Git支持的命令列表。如果您需要的Git命令不在列表中，请[提交Issues](https://github.com/DuckDuckStudio/Chinese_git/issues)告诉我们！<br>

| 现在叫啥     | 原来长啥样          | 用来干啥                           |
| ------------ | ------------------- | ---------------------------------- |
| 拉取         | pull                | 从远程仓库拉取源码                 |
| 推送         | push                | 将本地仓库中的提交推送到远程仓库中 |
| 提交         | commit -m           | 提交您的更改                       |
| 新建分支     | checkout -b         | 创建一个全新的分支                 |
| 切换分支     | checkout            | 切换到另一个分支                   |
| 合并         | merge               | 合并分支（可能会产生冲突）         |
| 暂存         | add                 | 暂存您的修改以备提交               |
| 查看状态     | status              | 查看当前仓库状态                   |
| 查看日志     | log                 | 查看提交日志                       |
| 删除分支     | branch -D           | 删除指定分支                       |
| 远程地址     | remote -v           | 查看远程仓库地址                   |
| 查看远程分支 | branch -r           | 查看远程仓库的分支列表             |
| 版本         | -v                  | 显示中文Git版本和Git版本           |
| 删除提交     | reset --hard HEAD~n | 撤销n次提交                        |

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
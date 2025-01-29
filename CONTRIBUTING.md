# 中文Git 开发者文档

如果你是开发人员，想要贡献中文Git，这个开发者文档会告诉你如何开始。

## 项目结构

中文Git项目的结构如下：

```
中文Git
|   .gitignore
|   ABOUT_TRANSLATION.md
|   config.json
|   CONTRIBUTING.md
|   ico.ico
|   LICENSE
|   README.md
|   README_DEV.md
|   requirements.txt
|   USER_HANDBOOK.md
|   中文git-pack.py
|   中文git.exe
|   中文git.py
|   中文git更新程序.exe
|   中文git更新程序.py
|
+---.auto_script
|       del_old_files.py
|
+---.github
|   |   CODEOWNERS.md
|   |   dependabot.yml
|   |   PULL_REQUEST_TEMPLATE.md
|   |
|   \---ISSUE_TEMPLATE
|           bug_feedback.yml
|           config.yml
|           feature_request.yml
|           new_command_request.yml
|
+---AutoPack
|       AutoPack.py
|       AutoPack_CN.py
|       packinit.iss
|       requirements.txt
|
+---docs
|   \---image
|       \---README
|               1718315176839.png
|
\---zh-tw
        中文git-pack.py
        中文git.py
```

* `zh-tw`: 项目的 繁体中文 翻译
* `.gitignore`: Git 忽略文件
* `中文git-pack.py`: 中文Git的打包版的主要代码文件，包含了中文Git的核心功能。
* `中文git.exe`: 中文Git的主要代码文件的打包版(使用Pyinstaller打包)，包含了中文Git的核心功能。
* `中文git.py`: 中文Git的主要代码文件，包含了中文Git的核心功能。
* `ABOUT_TRANSLATION.md`: 项目的翻译进度展示文件
* `中文git更新程序.py`: 中文Git的打包版的更新代码文件
* `中文git更新程序.exe`: 中文Git的打包版的更新程序(使用Pyinstaller打包)
* `CONTRIBUTING.md`(本文件): 开发者文档，用于开发人员了解项目的内部结构和如何贡献。
* `ico.ico`: 中文Git 项目图标
* `LICENSE`: 开源许可文件(GPL 2.0)
* `README_DEV.md`: 项目的详细用户指南，用于向看不惯`README.md`的用户介绍中文Git
* `README.md`: 项目的直白话用户指南，用于向用户介绍中文Git。
* `USER_HANDBOOK.md`: 项目的用户手册，用于向用户详细介绍如何使用

> _对于新的文件调整待补充说明_  

## 如何开始贡献

欢迎各种形式的贡献，无论是提交bug报告、提出改进建议还是直接提交代码修复问题。以下是贡献步骤：

1. fork 本项目
2. 克隆项目到本地
3. 在新仓库上进行修改
4. 提交你的更改
5. 提交Pull Request，描述你的修改并等待审核

### 你可以贡献什么
1. 添加新的可用命令  
   这非常简单，如果您不想做错误处理，直接在`git_command(command, *args)`函数中添加命令匹配即可。  
2. 对现有的可用命令的处理进行改进
   您可以在`git_command(command, *args)`函数中的`if git_command:`后看到对于各个命令的处理，每个命令在一个`if`中，您可以添加新的处理，或者优化现有处理。在添加新的处理时请使用`elif`而不是另外的`if`。
3. 文档
   说实话，当初为了好玩把这几个文档弄得这么奇葩...唉，总之，如果您可以帮忙整合/理文档，我非常感谢。  
   他们几乎都是相同的内容，计划将他们合并成一个文档，但我始终下不了手。  
4. 自动流
   目前此软件包还是我自己手动通过[命令](#如何打包)打包的，如果您能帮忙编写有关Linux/Macos系统上的发布流那就太好了！我没有用这两个系统的设备，我对他们几乎一无所知。

## 报告问题和提出建议

如果你发现了bug或者有任何改进建议，欢迎在GitHub上提交Issues。在提交Issue时，请提供清晰的描述以及复现步骤。建议使用Issue模板提交您的问题。  

## 项目许可

中文Git采用 GPL 2.0 许可证，详情请参阅[LICENSE](https://github.com/DuckDuckStudio/Chinese_git/blob/main/LICENSE)文件。

感谢您的支持和贡献！

## 如何打包

> [!NOTE]
> 打包前请安装依赖！  

本项目有三种从py到exe的打包方式:  
  
1. pyinstaller  
打包命令为:  
```bash
pyinstaller --onefile -i ico.ico --distpath=. --name="中文git.exe" "中文git-pack.py"
pyinstaller --onefile -i ico.ico --distpath=. --name="中文git更新程序.exe" "中文git更新程序.py"
```
2. Nuitka  
打包命令为:  
```bash
python -m nuitka --output-dir=. --show-progress --windows-icon-from-ico=ico.ico --onefile --remove-output "中文git-pack.py"
python -m nuitka --output-dir=. --show-progress --windows-icon-from-ico=ico.ico --onefile --remove-output "中文git更新程序.py"
```
3. 使用AutoPack工具
```bash
python "AutoPack\AutoPack.py"
```

## 关于winget包请求
如果你发现最新发行版在winget包中不可用，请向[microsoft/winget](https://github.com/microsoft/winget-pkgs)提交程序清单。  
在提交时还请 @DuckDuckStudio / @Luna-Grace ，感谢。  
使用`winget show --id DuckStudio.ChineseGit --source winget --exact --versions`来查找可用版本。  
你可以直接提交拉取请求，也可以创建议题让我们添加清单。  

## 关于翻译
如果你希协助 中文Git 进行 繁体中文 本地化，请将您的翻译结果提交到文件夹 `zh-tw` 内。  
对于翻译的要求：  
1. 翻译必须遵循 简体中文 的翻译，除非 简体中文 的翻译出错
2. 翻译完成后请提交 PR
3. 在翻译时也请同时翻译`README_DEV.md`与`USER_HANDBOOK.md`

## 已知问题

请见[Issues页](https://github.com/DuckDuckStudio/Chinese_git/issues)。

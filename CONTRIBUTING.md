# 中文Git 开发者文档

如果你是开发人员，想要贡献中文Git，这个开发者文档会告诉你如何开始。

## 项目结构

中文Git项目的结构如下：

```
中文Git/
├── README.md
├── README_DEV.md
├── 中文git.py
├── 中文git.exe
├── .gitignore
├── ico.ico
└── CONTRIBUTING.md
```

* `README.md`: 项目的直白话用户指南，用于向用户介绍如何使用中文Git。
* `README_DEV.md`: 项目的详细用户指南，用于向看不惯`README.md`的用户介绍如何使用中文Git
* `中文git.py`: 中文Git的主要代码文件，包含了中文Git的核心功能。
* `中文git.exe`: 中文Git的主要代码文件的打包版(使用Nuitka打包)，包含了中文Git的核心功能。
* `CONTRIBUTING.md`(本文件): 开发者文档，用于开发人员了解项目的内部结构和如何贡献。
* `ico.ico`: 中文Git 项目*临时*图标

本程序**按原样**提供。<br>

## 如何开始贡献

欢迎各种形式的贡献，无论是提交bug报告、提出改进建议还是直接提交代码修复问题。以下是贡献步骤：

1. fork 本项目

2. 克隆项目到本地：

```bash
git clone https://github.com/Your_Github_name/Chinese_git.git
```

3. 在新仓库上进行修改和开发。
4. 提交你的更改：

```bash
git add .
git commit -m "描述你的修改"
git push
```

5. 提交Pull Request，描述你的修改并等待审核。

## 报告问题和提出建议

如果你发现了bug或者有任何改进建议，欢迎在GitHub上提交Issues。在提交Issue时，请提供清晰的描述以及复现步骤。

## 项目许可

中文Git采用 GPL 2.0 许可证，详情请参阅[LICENSE](https://github.com/DuckDuckStudio/Chinese_git/blob/main/LICENSE)文件。

感谢您的支持和贡献！

## 如何打包

本项目有两种从py到exe的打包方式：<br>
1. pyinstaller<br>
打包命令为:<br>
```bash
pyinstaller --onefile -i "D:\path\to\Chinese_git\ico.ico" --distpath=. 中文git-pack.py
```
2. Nuitka<br>
打包命令为:<br>
```bash
python311 -m nuitka --output-dir=. --show-progress --windows-icon-from-ico="D:\path\to\Chinese_git\ico.ico" --onefile --remove-output 中文git-pack.py
```

## 已知问题

以下是 中文Git 目前的已知问题：<br>
* [在未暂存任何内容时提交 中文Git 会提示错误但不给出任何错误信息 Issues#3](https://github.com/DuckDuckStudio/Chinese_git/issues/3)
* 打包版在 Windows7 上可能无法运行 - 可能的解决方案：使用 Nuitka 打包
* 在非 utf-8 编码的设备上解压版本发行版压缩包可能会出现乱码 - 可能的解决方案：使用 Bandizip 解压
* 在使用 中文Git 执行部分命令时不会有输出，但命令成功执行

## 关于翻译
如果你希协助 中文Git 进行更多语言的本地化，你可以将新的本地化语言放在 other_language 中。<br>
对于新语言的要求：<br>
1. 可以为非中文语言，但请不要使用英语，这是 Git 所使用的语言。
2. 新语言的翻译必须遵循 简体中文 的翻译，除非 简体中文 的翻译出错
3. 翻译完成后请提交 PR 而非新建仓库另外分发
4. 在翻译时也请同时翻译`README_DEV.md`与`USER_HANDBOOK.md`

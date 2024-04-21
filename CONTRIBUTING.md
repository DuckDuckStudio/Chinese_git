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
└── CONTRIBUTING.md
```

* `README.md`: 项目的直白话用户指南，用于向用户介绍如何使用中文Git。
* `README_DEV.md`: 项目的详细用户指南，用于向看不惯`README.md`的用户介绍如何使用中文Git
* `中文git.py`: 中文Git的主要代码文件，包含了中文Git的核心功能。
* `中文git.exe`: 中文Git的主要代码文件的打包版(使用Nuitka打包)，包含了中文Git的核心功能。
* `CONTRIBUTING.md`(本文件): 开发者文档，用于开发人员了解项目的内部结构和如何贡献。

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

中文Git采用MIT许可证，详情请参阅[LICENSE](https://github.com/DuckDuckStudio/Chinese_git/blob/main/LICENSE)文件。

感谢您的支持和贡献！

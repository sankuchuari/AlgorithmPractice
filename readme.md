# **AlgorithmPractice**

Personal repository for algorithm practice and competitive programming records.

## 🎯 Platforms
- **Codeforces**
- **Luogu**
- **AtCoder / LeetCode**

## 🛠️ Tech Stack
- **Language**: `C++20`
- **Environment**: macOS
- **Tools**: CMake, GCC

# AlgorithmPractice

个人算法竞赛（ICPC / Codeforces / AtCoder）题解与刷题代码仓库，包含 C++17 题解源码、自动题面抓取渲染工具及双语题面归档。

## 📂 仓库结构

```text
AlgorithmPractice/
├── problems/               # 按 OJ 平台与比赛场次分类的题解与题面
│   └── codeforces/
│       └── <contest_id>/
│           ├── A.cpp        # C++17 题解代码
│           ├── A.md         # 英文题面（暗色主题渲染）
│           └── A_zh.md      # 中文题面（自动翻译渲染）
├── fetch_cf.py             # Codeforces / Gym 题面自动抓取与双语渲染脚本
├── FETCH_CF_README.md      # fetch_cf.py 详细使用说明与 CLion 全屏工作流配置
└── requirements.txt        # Python 自动化脚本依赖清单
```

## 🛠️ 自动化刷题工具 (`fetch_cf.py`)

内置基于 Playwright 与本地离线神经网络的题面抓取脚本，支持在 CLion 中一键拉取题面并分屏全屏做题：

- **双语渲染**：自动转换 LaTeX 数学公式并输出适配暗色 IDE 的 `<index>.md` 与 `<index>_zh.md`。
- **全平台代理调度**：自动读取 Windows / macOS / Linux 系统代理，直连受阻时无缝切换。
- **跨平台离线翻译**：优先使用在线翻译接口，无代理或离线环境下自动降级为本地推理（Apple Silicon M 系列芯片使用原生 `MLX` 加速，其他平台自动切换 `Argos Translate`）。

> 详细安装步骤、命令行用法及 CLion 快捷键配置请查阅：[fetch_cf.py 使用指南](./FETCH_CF_README.md)（请按实际文件名修改链接）。

## ⚡ 快速开始

```bash
# 1. 安装脚本依赖
pip install -r requirements.txt
playwright install chromium

# 2. 拉取指定题目（例如 Codeforces 2290 E）
python fetch_cf.py 2290 E
```


个人算法竞赛（ICPC / Codeforces / AtCoder）题解与刷题代码仓库，包含 C++20 题解源码、自动题面抓取渲染工具及双语题面归档。

## 📂 仓库结构

```text
AlgorithmPractice/
├── problems/               # 按 OJ 平台与比赛场次分类的题解与题面
│   └── codeforces/
│       └── <contest_id>/
│           ├── A.cpp        # C++17 题解代码
│           ├── A.md         # 英文题面（暗色主题渲染）
│           └── A_zh.md      # 中文题面（自动翻译渲染）
├── fetch_cf.py             # Codeforces / Gym 题面自动抓取与双语渲染脚本
├── FETCH_CF_README.md      # fetch_cf.py 详细使用说明与 CLion 全屏工作流配置
└── requirements.txt        # Python 自动化脚本依赖清单
```

## 🛠️ 自动化题面抓取翻译工具 (`fetch_cf.py`)

内置基于 Playwright 与本地离线神经网络的题面抓取脚本，支持在 CLion 中一键拉取题面并分屏全屏做题：

- **双语渲染**：自动转换 LaTeX 数学公式并输出适配暗色 IDE 的 `<index>.md` 与 `<index>_zh.md`。
- **全平台代理调度**：自动读取 Windows / macOS / Linux 系统代理，直连受阻时无缝切换。
- **跨平台离线翻译**：优先使用在线翻译接口，无代理或离线环境下自动降级为本地推理（Apple Silicon M 系列芯片使用原生 `MLX` 加速，其他平台自动切换 `Argos Translate`）。

> 详细安装步骤、命令行用法及 CLion 快捷键配置请查阅：[fetch_cf.py 使用指南](./FETCH_CF_README.md)（请按实际文件名修改链接）。

## ⚡ 快速开始

```bash
# 1. 安装脚本依赖
pip install -r requirements.txt
playwright install chromium

# 2. 拉取指定题目（例如 Codeforces 2290 E）
python fetch_cf.py 2290 E
```

# Codeforces 题面自动抓取与双语渲染工具 (`fetch_cf.py`)

一个专为本地 IDE 刷题设计的 Codeforces / Gym 题面抓取脚本。支持自动解析 LaTeX 数学公式、暗色主题 HTML 排版，并通过**在线 + 本地离线神经网络双通道**自动生成中英双语 Markdown 题面。

## ✨ 核心特性

- **双语对照输出**：每次抓取自动在 `problems/codeforces/<contest_id>/` 下生成英文原版（`<index>.md`）与中文翻译版（`<index>_zh.md`）。
- **智能网络调度**：默认优先直连 Codeforces（3 次快速重试），直连受阻时自动读取系统 HTTP/SOCKS 代理无缝切换。
- **跨平台离线神经网络翻译**：
    - 优先尝试 Google 翻译接口；
    - 无代理或离线环境下自动降级为本地神经网络推理：**Apple Silicon (M 系列芯片)** 调用原生 `MLX` (`Qwen2.5-3B-Instruct-4bit`) 加速推理；**其他平台 (Windows / Linux / Intel Mac)** 自动切换 `Argos Translate` 离线模型，全程精准保留公式与样式占位符。
- **专为暗色 IDE 定制的排版**：内置暗色主题高对比度配色，自动转换上下标与希腊字母等常用 LaTeX 符号，高亮输入输出样例及 `YES/NO`、`Alice/Bob` 等博弈关键词。

---

## 🛠️ 环境安装

1. **安装 Python 依赖**：
   ```bash
   pip install -r requirements.txt
   ```
2. **安装 Playwright 浏览器内核**：
   ```bash
   playwright install chromium
   ```
3. **（非 M 系列芯片可选）安装 Argos 离线英中语言包**：
   ```bash
   python -c "import argostranslate.package; argostranslate.package.update_package_index(); pkgs = argostranslate.package.get_available_packages(); pkg = next(p for p in pkgs if p.from_code == 'en' and p.to_code == 'zh'); argostranslate.package.install_from_path(pkg.download())"
   ```

---

## 🚀 命令行用法

```bash
# 抓取指定比赛的单道题目（如 2290 E）
python fetch_cf.py 2290 E

# 抓取整场比赛的所有题目（如 2290）
python fetch_cf.py 2290

# 支持 Gym 场次（比赛编号 >= 100000 自动识别为 Gym）
python fetch_cf.py 104857 A
```

---

## 💻 CLion 无缝集成工作流

把脚本接入 CLion 后，不需要切出 IDE 即可拉取题面并全屏做题：

### 1. 绑定为 CLion External Tool
- 打开设置（macOS 按 `Cmd + ,`），进入 **Tools | External Tools**，点击 `+` 号。
- **Program** 填入你的 Python 解释器路径（如 `/usr/local/bin/python3` 或虚拟环境路径）。
- **Arguments** 填入 `$ProjectFileDir$/fetch_cf.py $Prompt$`。
- **Working directory** 填入 `$ProjectFileDir$`。
- 保存后，在 CLion 里通过右键菜单 **External Tools** 运行它，会弹出一个输入框，直接输入 `2278 A` 回车，几秒内就会生成对应的 `A.md`。

### 2. 绑定快捷触发键（推荐）
如果你经常拉取题面，绑定快捷键比每次点菜单快得多：
1. 打开 CLion 设置（macOS 按 `Cmd + ,`）。
2. 进入 **Keymap（按键映射）**。
3. 在右侧搜索框输入你刚创建的工具名字（如 `fetch_cf`），展开 **External Tools**。
4. 右键点击它，选择 **Add Keyboard Shortcut**，按下一个顺手的组合键（例如 `Option + F` 或 `Cmd + Shift + M`）并保存。
5. 以后无论在哪个页面，按下这个快捷键就会直接弹出题号输入框，生成后在右侧目录 `problems/codeforces/2290/` 下就会立刻出现对应的 `E.md`。

### 3. 配置纯净的“纯预览”全屏界面
- 打开生成的 `A.md`，点击编辑器右上角的 **Preview Only（仅预览）** 图标，隐藏掉左侧的 Markdown 源码，只保留渲染后的题面。
- 右键点击 `A.md` 标签页，选择 **Split Right（向右分屏）**，把 `A.cpp` 放在一侧，`A.md` 纯预览放在另一侧。
- 进入 **View | Appearance | Enter Full Screen**（macOS 快捷键 `Ctrl + Cmd + F`），即可在完全脱离浏览器的全屏环境下对照题面写代码。
- **优化预览字体大小（可选）**：如果全屏时觉得字体偏小，可以进入 **Settings | Languages & Frameworks | Markdown**，直接调大 **Preview font size**，或者在 **Custom CSS** 中自定义行距和背景色，让它完全融入你的 CLion 主题配色。

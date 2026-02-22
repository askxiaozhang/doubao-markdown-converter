# 豆包 Markdown 转换器 (Doubao Markdown Converter)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Faskxiaozhang%2Fdoubao-markdown-converter)

一个轻量级的 Web 工具，专门用于将豆包（Doubao）导出的 Markdown 内容转换为标准 Markdown 格式，特别是针对数学公式的规范化处理。

## 🚀 核心功能

- **智能公式转换**：
  - **独立行公式**：将 `\( ... \)` 自动提升为标准块级公式 `$$ ... $$`。
  - **行内公式降级**：检测嵌入在文字中的 `$$ ... $$`（豆包常用格式），自动转换为标准行内公式 `$ ... $`，确保在 GitHub、Obsidian 等工具中完美预览。
- **实时转换**：无需点击按钮，输入即所得。
- **暗黑系 UI**：基于现代审美设计的沉浸式交互界面。
- **统计功能**：实时显示字符变更和转换处数。

## 🛠️ 技术栈

- **前端**：HTML5, Vanilla CSS (Custom Properties), Javascript (ES6+)
- **后端**：Python, Flask (部署于 Vercel 无服务函数)
- **部署**：Vercel

## 📖 转换规则示例

### 1. 独立行处理
**输入 (豆包):**
```text
\(E = mc^2\)
```
**输出 (标准):**
```text
$$E = mc^2$$
```

### 2. 行内处理
**输入 (豆包):**
```text
已知 $$P(A)$$ 的概率...
```
**输出 (标准):**
```text
已知 $P(A)$ 的概率...
```

## 💻 本地开发

1. **环境准备**：
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install flask
   ```

2. **启动服务**：
   ```bash
   vercel dev
   # 或者
   python api/index.py
   ```

## ☁️ 部署到 Vercel

本项目适配 Vercel Python Runtime。只需推送代码到 GitHub 并关联 Vercel 即可一键部署。

---
Created by [askxiaozhang](https://github.com/askxiaozhang)

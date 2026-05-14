# 章节说明 / Chapters

本目录维护每一章的统一结构、命名规范与材料约定，确保课程内容可复用、可检索、可持续迭代。
This folder defines the standard structure and naming rules for each chapter.

## 命名规范 / Naming
- 统一采用 `chNN-english-slug`，NN 为两位数便于排序（例如：`ch01-python-setup`、`ch20-ai-for-science`）。
- 不使用中文目录名；标题写在 `README.md` 与 `chapters.yml` 中。

Use `chNN-english-slug` with two-digit NN for sorting (e.g., `ch01-python-setup`).
Do not use Chinese folder names; put titles in `README.md` and `chapters.yml`.

## 章节结构 / Structure
每章固定结构如下：

```
chapters/
  chXX-.../
    slides/      # PPTX / PDF
    tutorial/    # Notebooks / Markdown / code / small data
    README.md    # 章节概览与学习目标
```

Each chapter includes:
- `slides/` (PPTX/PDF)
- `tutorial/` (notebooks, step-by-step notes, code, small datasets)
- `README.md` (overview, outcomes, prerequisites)

## README 要求 / README Checklist
包含以下条目（中英双语）：
- 概览 / Summary
- 学习目标 / Learning Outcomes（3-5 条）
- 前置知识 / Prerequisites
- 预计时长 / Time Estimate
- 材料 / Materials（指向 `slides/` 与 `tutorial/`）
- 练习 / Exercises
- 注意事项 / Notes
- 延伸阅读 / Further Reading

## Slides 规范 / Slides
- 统一放入 `slides/`，支持 `pptx` 与导出的 `pdf`。

## Tutorial 规范 / Tutorials
- Notebook 以“最小可运行示例 → 逐步扩展”的方式组织。
- 代码必须可运行，注释清晰、逐步推进。
- 小型数据文件（如 `.txt`、`.json`）放入 `tutorial/`。
- 大型数据集请在 Notebook 中给出下载指引与缓存说明。

## 章节索引 / Index
新增或调整章节后：
1. 更新 `chapters.yml` 中的标题与目录路径。
2. 更新总目录 `README.md` 的章节表格链接。

## 新建章节 / Add a Chapter
1. 复制 `chapters/_template` 到新的 `chNN-...` 目录。
2. 完善该章 `README.md` 与材料。
3. 在 `chapters.yml` 中注册章节信息。

## 完整性检查 / Validation
运行章节完整性检查脚本：
```powershell
./scripts/check_chapters.ps1
```
如果系统禁用了脚本执行，可用：
```powershell
powershell -ExecutionPolicy Bypass -File ./scripts/check_chapters.ps1
```

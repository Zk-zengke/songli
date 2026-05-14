# 第13章：代码生成 / Chapter 13: Code Generation

## 概览 / Summary
本章构建一个最小代码生成工作台：模型自动选择与回退、任务与测试集、prompt、代码抽取、语法检查、自动执行、self-refine 与 pass@k 估计。

## 学习目标 / Learning Outcomes
- 构建代码生成任务与可执行测试集
- 设计提示词并进行代码抽取/清洗
- 使用自动测试与反馈迭代修复生成代码
- 估计 pass@k 并理解评测差异
- 进行示例代码审阅

## 前置知识 / Prerequisites
- Python 基础与单元测试思维
- 语言模型生成原理

## 关键内容 / Key Topics
- 模型候选与回退策略
- 任务与测试集构建
- One-shot 与 Self-Refine
- pass@k 估计与代码审阅

## 预计时长 / Time Estimate
- 90–120 分钟 / 90–120 minutes

## 材料 / Materials
- Slides: `slides/`
- Tutorial: `tutorial/code_generation_workbench.ipynb`

## 练习 / Exercises
- 新增 1–2 个编程任务并补充测试
- 引入静态检查（如 `ast`）作为反馈
- 调整 prompt 与解码策略并比较 pass@k

## 运行提示 / Notes
- 默认候选模型：`bigcode/tiny_starcoder_py`，回退到 `Salesforce/codegen-350M-mono` 或 `gpt2`
- 依赖：`torch` `transformers`

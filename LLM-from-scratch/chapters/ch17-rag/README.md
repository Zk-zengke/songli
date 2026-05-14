# 第17章：RAG（检索增强生成） / Chapter 17: Retrieval-Augmented Generation

## 概览 / Summary
从零构建 RAG：构建语料库、切块、TF-IDF 检索、生成模型、RAG 提示，并对比 direct vs RAG 的效果。

## 学习目标 / Learning Outcomes
- 理解 RAG 的检索与生成协作机制
- 实现文本切块与 TF-IDF 检索
- 设计 RAG prompt 并生成答案
- 评估检索指标（Hit@k）与证据可解释性

## 前置知识 / Prerequisites
- TF-IDF 与余弦相似度
- Seq2Seq 生成基础

## 关键内容 / Key Topics
- 知识库构建与切块
- TF-IDF 检索与排序
- RAG 生成函数与基线对比
- Hit@k 与证据展示

## 预计时长 / Time Estimate
- 90–120 分钟 / 90–120 minutes

## 材料 / Materials
- Slides: `slides/`
- Tutorial: `tutorial/rag_pipeline_from_scratch.ipynb`

## 练习 / Exercises
- 替换为更长文档并调整 chunk 策略
- 用向量检索替换 TF-IDF（可选）
- 改写 RAG prompt 并对比结果

## 运行提示 / Notes
- 生成模型：`google/flan-t5-small`（可改为 `t5-small`）
- 依赖：`torch` `transformers` `scikit-learn`

# 第10章：通用信息抽取（IE）与序列标注 / Chapter 10: Information Extraction and Sequence Labeling

## 概览 / Summary
本章系统讲解信息抽取（IE）的核心任务谱系（NER/RE/文档字段抽取），并以序列标注为主线完成端到端教学实验。
通过最小可运行案例，涵盖数据构造、标签体系、对齐、训练、推理与评估，并扩展到关系抽取与票据场景。

## 学习目标 / Learning Outcomes
- 掌握 BIO/BILOU 标签体系与子词对齐方法
- 训练轻量 NER 模型并计算 F1
- 基于 NER 结果实现规则化 RE
- 在票据/发票文本上完成字段抽取与可视化

## 前置知识 / Prerequisites
- 分词与子词机制
- PyTorch 与分类头基础
- 基本 Transformer 结构理解

## 教学结构 / Notebook Outline
1. 环境准备
2. 构造最小 IE 数据
3. BIO/BILOU 标签体系
4. Dataset 组装与标签映射
5. Tokenization 与标签对齐
6. 轻量 NER 训练与评估
7. 推理与结果可视化
8. 基于 NER 的关系抽取（RE）
9. 票据/发票字段抽取
10. 报告与练习

## 预计时长 / Time Estimate
- 90–120 分钟 / 90–120 minutes

## 材料 / Materials
- Slides: `slides/`
- Tutorial: `tutorial/ie_sequence_labeling.ipynb`

## 练习 / Exercises
- 将标签体系改为 BILOU 并比较 F1
- 替换为自定义实体类型与样例
- 设计一条新的 RE 规则并评估
- 在自定义票据文本上做字段抽取并可视化

## 运行提示 / Notes
- 默认模型：`prajjwal1/bert-tiny`，CPU 可运行
- 依赖：`torch` `transformers` `datasets` `seqeval`
- 真实项目需扩展数据规模并引入严格评测

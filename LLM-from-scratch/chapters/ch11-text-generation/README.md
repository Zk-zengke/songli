# 第11章：文本生成任务：机器翻译、问答等 / Chapter 11: Text Generation (MT + QA)

## 概览 / Summary
本章以机器翻译与问答为主线，构建统一的生成接口，比较 greedy 与 sampling，并使用 BLEU/EM/F1 进行评估。

## 学习目标 / Learning Outcomes
- 搭建统一的生成函数并控制解码策略
- 在 MT/QA 任务上进行提示与输出对比
- 计算 BLEU 与 EM/Token-F1
- 构建简单的任务路由器（task router）

## 前置知识 / Prerequisites
- Seq2Seq 模型与生成基础
- Python 文本处理

## 关键内容 / Key Topics
- 翻译模型 + QA 模型加载
- 统一生成函数与解码策略
- MT 任务与 BLEU 评估
- QA 任务与 EM/F1 评估
- 统一任务路由

## 预计时长 / Time Estimate
- 90–120 分钟 / 90–120 minutes

## 材料 / Materials
- Slides: `slides/`
- Tutorial: `tutorial/text_generation_mt_qa.ipynb`

## 练习 / Exercises
- 增加摘要任务并复用 `gen`
- 对比不同 `temperature/top_p` 的输出差异
- 引入更多 QA 样本并重新评估

## 运行提示 / Notes
- 翻译模型：`Helsinki-NLP/opus-mt-en-zh`
- 问答模型：`t5-small`
- 依赖：`torch` `transformers` `sacrebleu` `sentencepiece`

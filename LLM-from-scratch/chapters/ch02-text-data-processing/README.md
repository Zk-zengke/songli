# 第2章：文本数据处理 / Chapter 2: Text Data Processing

## 概览 / Summary
· 原始文本如何被切分成 token，并进一步转成可训练的 ID 与向量表示。  
· 重点覆盖分词与词表、滑动窗口构造训练样本、批处理，以及词元嵌入与位置嵌入的组合方式。  

## 学习目标 / Learning Outcomes
· 能把文本转换为 Token ID，并构造可训练的输入-目标序列。  
· 能理解并使用词元嵌入与位置嵌入，得到模型输入表示。  

## 关键内容 / Key Topics
· 词表与映射：token↔id，encode/decode 的最小分词器接口。  
· 特殊词元：未知词与文档分隔符等基本处理。  
· BPE 子词编码：减少未见词问题，理解现代大模型常用分词思路。  
· 滑动窗口：用 context_length 与 stride 切片，形成 next-token 训练对。  
· 批处理：用 DataLoader 组成 batch，控制序列长度与步幅。  
· 输入嵌入：词元嵌入 + 绝对位置嵌入，生成最终输入向量。  

## 运行提示 / Notes
· 主要依赖 PyTorch（Embedding、DataLoader）与基础文本处理工具。  
· 先按默认参数跑通，再对比不同 stride 与长度设置的差异。  

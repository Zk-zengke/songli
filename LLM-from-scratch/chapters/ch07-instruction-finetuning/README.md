# 第7章：指令微调 / Chapter 7: Instruction Finetuning

## 概览 / Summary
· 本章讲清指令微调的目的：让模型从“续写”转向“按指令完成任务”的交互式输出。  
· 内容覆盖指令数据的结构化格式、训练时的批处理与填充约束、目标右移的自回归训练设置，以及开放式文本任务的评估思路。  

## 学习目标 / Learning Outcomes
· 理解指令微调与纯续写训练在数据形式与训练目标上的差异。  
· 掌握指令数据组织、padding/mask、目标右移与损失屏蔽的关键做法。  

## 关键内容 / Key Topics
· 从“续写”到“交互”：Base model 以补全文本为主，指令微调让模型对齐用户意图并输出任务答案。  
· 指令数据格式（Alpaca 风格）：Instruction（做什么）、Input（给什么上下文）、Output（理想回复）。  
· 工程约束：把变长对话样本整理成定长张量批次，依赖 attention_mask 遮住填充位置。  
· 训练逻辑：目标序列相对输入右移 1 个 token，形成标准 next-token 预测训练。  
· Masking padding：在 labels 里将多余 padding 位置置为 -100，使其不参与 loss；保留一个 50256 作为 EOS，让模型学会在正确位置停止生成。  
· 学习曲线：对比训练 loss 与验证 loss 的趋势，用于判断有效学习与过拟合/欠拟合迹象。  
· 评估特点：指令微调输出为开放式文本，难以用简单对/错准确率衡量，更强调语义质量与可用性评估。  

## 运行提示 / Notes
· 训练前优先检查：input_ids、attention_mask、labels 三者在形状与对齐关系上是否一致。  
· 重点检查两处：padding 是否被 mask 掉，labels 的 padding 是否被置为 -100，同时 EOS 是否保留在合适位置。  


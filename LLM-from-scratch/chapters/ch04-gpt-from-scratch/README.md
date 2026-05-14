# 第4章：从头实现 GPT 模型 / Chapter 4: Implementing GPT from Scratch

## 概览 / Summary
· 本章围绕 GPT（以“预测下一个 token”为目标）的整体架构展开，从输入表示到 Transformer 主干再到输出解码，完整走一遍模型前向计算链路。  
· 重点把 GPT 的核心组件拆开讲清，并在最后把它们组装成可运行的 GPT-2 Small 风格模型，用于自回归文本生成。  

## 学习目标 / Learning Outcomes
· 能描述 GPT 的 Base（输入）、Body（堆叠 Block）、Head（输出）的整体结构与数据流。  
· 能把注意力、前馈网络、归一化与残差连接组装成一个 Transformer Block，并堆叠成完整模型。  

## 关键内容 / Key Topics
· GPT 任务目标：基于上下文预测下一个 token，自回归生成文本。  
· 输入表示：token embedding 与 position embedding 相加，形成模型输入张量表示（形状通常为 [Batch, Seq, Hidden]）。  
· 层归一化（LayerNorm）：稳定深层网络的激活分布，提升训练与推理稳定性。  
· 激活函数：从 ReLU 到 GELU，理解 GELU 在大模型中的常用原因。  
· 前馈网络（FFN）：逐 token 的非线性变换，常见“扩张→激活→收缩”的结构。  
· 残差连接（Residual）：通过 x + Layer(x) 提供梯度直达路径，缓解深层训练困难。  
· 组装 Transformer Block：LayerNorm + 注意力 + FFN + 残差，输入输出维度保持一致，便于堆叠。  
· 完整 GPT-2 Small 结构：Base + 12 个 Block + 最终归一化 + 线性投影到词表维度，输出 logits。  
· 文本生成循环：滑动窗口式自回归，把新生成 token 追加回上下文并重复推理。  
· 解码：从 logits 到概率分布（Softmax），再用 greedy 等策略选择 token 并还原为文本。  

## 运行提示 / Notes
· 建议先单独验证各模块的张量形状与数值范围，再做整模型串联，最后再加入生成循环。  
· 生成时需使用因果约束（mask）保证不能看到未来 token，否则会破坏自回归假设。  
· 先用 greedy 跑通端到端生成，再逐步加入 sampling 等策略，便于定位差异来源。  

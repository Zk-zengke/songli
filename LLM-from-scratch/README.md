# 大模型基础教程 / LLM Foundations Course

从零学习大模型（LLM）的分章节课程仓库，覆盖模型训练、对齐、安全、能力涌现、部署与智能体。
每章包含 PPT/讲义（`slides/`）与可运行 Notebook 教程（`tutorial/`）。

A chapter-based curriculum for learning LLMs from scratch, spanning training, alignment, safety, emergence, deployment, and agents.
Each chapter provides slides and executable notebooks.

**Quick Links**: [课程结构](#课程结构--course-structure) · [章节目录](#章节目录--chapter-index) · [运行环境](#运行环境--environment) · [贡献](#贡献--contributing)

---

## 最近更新 / Updates
- 2026-02-05：完善 ch10/ch11/ch13/ch17/ch18 的 Notebook 与章节 README（信息抽取、文本生成、代码生成、RAG、GUI Agent）。

---

## 项目动机 / Motivation
面向工程实践的 LLM 基础课程，强调“可运行的最小实验 + 清晰注释 + 逐步推进”，帮助学习者建立从原理到实践的完整路径。

---

## 适用人群 / Audience
- 具备 Python 基础，希望系统学习大模型技术栈的学习者
- 需要快速构建实验与原型的研究与工程人员

---

## 课程结构 / Course Structure
- 第一阶段 底层实现（ch01–ch06）：Python 环境、文本数据处理、注意力机制、GPT 实现、无标签预训练、分类任务微调。
- 第二阶段 对齐、微调与安全（ch07–ch11）：SFT、RLHF、安全对齐、知识编辑、信息抽取与文本生成。
- 第三阶段 能力涌现与多模态（ch12–ch14）：复杂推理、代码生成、多模态架构。
- 第四阶段 部署、智能体与未来（ch15–ch20）：量化/蒸馏/MoE、RAG、GUI Agent、安全与 AI4S。

---

## 章节目录 / Chapter Index
| 章节 | 主题 | 阶段 | 链接 |
|---|---|---|---|
| ch01 | 设置 Python 环境 | 第一阶段 | [README](chapters/ch01-python-setup/README.md) · [slides](chapters/ch01-python-setup/slides/) · [tutorial](chapters/ch01-python-setup/tutorial/) |
| ch02 | 文本数据处理 | 第一阶段 | [README](chapters/ch02-text-data-processing/README.md) · [slides](chapters/ch02-text-data-processing/slides/) · [tutorial](chapters/ch02-text-data-processing/tutorial/) |
| ch03 | 注意力机制 | 第一阶段 | [README](chapters/ch03-attention-mechanisms/README.md) · [slides](chapters/ch03-attention-mechanisms/slides/) · [tutorial](chapters/ch03-attention-mechanisms/tutorial/) |
| ch04 | 从头实现 GPT 模型 | 第一阶段 | [README](chapters/ch04-gpt-from-scratch/README.md) · [slides](chapters/ch04-gpt-from-scratch/slides/) · [tutorial](chapters/ch04-gpt-from-scratch/tutorial/) |
| ch05 | 在无标签数据上进行预训练 | 第一阶段 | [README](chapters/ch05-pretraining-unlabeled/README.md) · [slides](chapters/ch05-pretraining-unlabeled/slides/) · [tutorial](chapters/ch05-pretraining-unlabeled/tutorial/) |
| ch06 | 针对分类任务的微调 | 第一阶段 | [README](chapters/ch06-classification-finetuning/README.md) · [slides](chapters/ch06-classification-finetuning/slides/) · [tutorial](chapters/ch06-classification-finetuning/tutorial/) |
| ch07 | 指令微调 | 第二阶段 | [README](chapters/ch07-instruction-finetuning/README.md) · [slides](chapters/ch07-instruction-finetuning/slides/) · [tutorial](chapters/ch07-instruction-finetuning/tutorial/) |
| ch08 | RLHF 与安全对齐 | 第二阶段 | [README](chapters/ch08-rlhf-safety/README.md) · [slides](chapters/ch08-rlhf-safety/slides/) · [tutorial](chapters/ch08-rlhf-safety/tutorial/) |
| ch09 | 知识编辑与模型鲁棒性 | 第二阶段 | [README](chapters/ch09-knowledge-editing/README.md) · [slides](chapters/ch09-knowledge-editing/slides/) · [tutorial](chapters/ch09-knowledge-editing/tutorial/) |
| ch10 | 通用信息抽取（IE）与序列标注 | 第二阶段 | [README](chapters/ch10-information-extraction/README.md) · [slides](chapters/ch10-information-extraction/slides/) · [tutorial](chapters/ch10-information-extraction/tutorial/) |
| ch11 | 文本生成任务：机器翻译、问答等 | 第二阶段 | [README](chapters/ch11-text-generation/README.md) · [slides](chapters/ch11-text-generation/slides/) · [tutorial](chapters/ch11-text-generation/tutorial/) |
| ch12 | 复杂推理：思维链（CoT）与数学能力 | 第三阶段 | [README](chapters/ch12-reasoning-cot/README.md) · [slides](chapters/ch12-reasoning-cot/slides/) · [tutorial](chapters/ch12-reasoning-cot/tutorial/) |
| ch13 | 代码生成 | 第三阶段 | [README](chapters/ch13-code-generation/README.md) · [slides](chapters/ch13-code-generation/slides/) · [tutorial](chapters/ch13-code-generation/tutorial/) |
| ch14 | 多模态大模型（M-LLM）架构 | 第三阶段 | [README](chapters/ch14-multimodal-llm/README.md) · [slides](chapters/ch14-multimodal-llm/slides/) · [tutorial](chapters/ch14-multimodal-llm/tutorial/) |
| ch15 | 模型量化、蒸馏与高效部署 | 第四阶段 | [README](chapters/ch15-efficient-deployment/README.md) · [slides](chapters/ch15-efficient-deployment/slides/) · [tutorial](chapters/ch15-efficient-deployment/tutorial/) |
| ch16 | MoE（Mixture of Experts）与可扩展训练/推理系统 | 第四阶段 | [README](chapters/ch16-moe-systems/README.md) · [slides](chapters/ch16-moe-systems/slides/) · [tutorial](chapters/ch16-moe-systems/tutorial/) |
| ch17 | RAG（检索增强生成） | 第四阶段 | [README](chapters/ch17-rag/README.md) · [slides](chapters/ch17-rag/slides/) · [tutorial](chapters/ch17-rag/tutorial/) |
| ch18 | GUI 智能体（Agent）与工具调用 | 第四阶段 | [README](chapters/ch18-gui-agents/README.md) · [slides](chapters/ch18-gui-agents/slides/) · [tutorial](chapters/ch18-gui-agents/tutorial/) |
| ch19 | 智能体安全与伦理展望 | 第四阶段 | [README](chapters/ch19-agent-safety/README.md) · [slides](chapters/ch19-agent-safety/slides/) · [tutorial](chapters/ch19-agent-safety/tutorial/) |
| ch20 | AI for Science | 第四阶段 | [README](chapters/ch20-ai-for-science/README.md) · [slides](chapters/ch20-ai-for-science/slides/) · [tutorial](chapters/ch20-ai-for-science/tutorial/) |

---

## 运行环境 / Environment
- Python 3.10+（CPU 可运行，GPU 可加速）
- 常用依赖：`torch`, `transformers`, `datasets`, `seqeval`, `sacrebleu`, `scikit-learn`, `sentencepiece`, `accelerate`
- 若离线运行，请提前缓存模型权重

---

## 快速开始 / Quick Start
1. 查看章节索引 `chapters.yml` 与结构说明 `chapters/README.md`。
2. 进入章节目录，阅读该章 `README.md`。
3. 按 `tutorial/` 中 Notebook 顺序运行。

---

## 学术引用 / Citation
如需学术引用，可添加 `CITATION.cff` 并注明课程版本与作者信息。

---

## 贡献 / Contributing
贡献流程见 `CONTRIBUTING.md`。

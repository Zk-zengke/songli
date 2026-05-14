# 第18章：GUI 智能体（Agent）与工具调用 / Chapter 18: GUI Agents and Tool Use

## 概览 / Summary
本章以教学版 GUI Agent 为例，覆盖工具定义与安全约束、ReAct 规划、动作解析与执行、主循环与安全拦截。

## 学习目标 / Learning Outcomes
- 建模工具 schema 与参数约束
- 实现安全可控的工具执行器
- 构建 ReAct 规划与主循环
- 识别越权/注入并进行拦截

## 前置知识 / Prerequisites
- Python 基础
- 状态机/流程控制
- 基本安全概念

## 关键内容 / Key Topics
- 工具与安全策略定义
- GUI 状态与动作执行
- ReAct 规划器与主循环
- 两个 Demo 场景与安全演示

## 预计时长 / Time Estimate
- 60–90 分钟 / 60–90 minutes

## 材料 / Materials
- Slides: `slides/`
- Tutorial: `tutorial/gui_agent_tool_calling.ipynb`

## 练习 / Exercises
- 新增一个 GUI 工具并接入主循环
- 添加审计日志与敏感操作提示
- 设计更严格的参数校验策略

## 运行提示 / Notes
- 仅使用标准库，可直接运行

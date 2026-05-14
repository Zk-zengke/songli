# 第1章：设置 Python 环境 / Chapter 1: Python Environment Setup 

## 概览 / Summary
· 本章聚焦于课程运行环境的统一配置。  
· 目标是在进入后续模型与实验内容之前，完成 Python 安装、虚拟环境隔离、依赖安装与 JupyterLab 启动的全流程。  
· 通过这一章，你将得到一套可复现的实验环境，用于运行后续所有章节。  

## 学习目标 / Learning Outcomes
· 能在终端确认 Python 是否可用，并检查版本信息。  
· 能使用 uv 创建项目级虚拟环境，并完成激活与停用。  
· 能在虚拟环境中通过 requirements.txt 安装课程依赖。  
· 能启动 JupyterLab 并进入交互式开发环境开始运行后续内容。  
· 了解 Conda/Miniforge 作为替代方案的基本流程与适用场景。  

## 关键内容 / Key Topics
· Python 安装与版本检查；按系统选择安装路径（Linux、macOS、Windows）。  
· uv 路线：安装 uv、创建 `.venv`、在不同系统下完成环境激活。  
· 依赖安装：安装单个包与批量安装 requirements.txt。  
· JupyterLab 启动：正常方式启动；当命令不可用时使用虚拟环境内可执行文件启动。  
· Conda 路线：安装 Miniforge、创建环境、安装 JupyterLab 与深度学习框架，并说明版本兼容性原则。  

## 运行提示 / Notes
· 重新打开终端后需要再次激活虚拟环境，这是正常流程。  
· Windows 如遇依赖兼容问题，可回退到更常规的安装方式以保证流程可继续。  
· 当 `jupyter lab` 不在 PATH 中时，优先使用虚拟环境内的 jupyter 可执行文件启动。  
· 可选工具与在线环境：VS Code、PyCharm、Jupyter Notebook、Colab、Kaggle、GitHub Codespaces。  

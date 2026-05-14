## 第1章 ： 设置Python环境

写在本教程开始之前，此教程目的是为了帮助同学了解大模型的基本原理实现与应用。
前七章参考SEBASTIAN RASCHKA的《Build a Large Language Model (From Scratch)》教程内容，并结合个人理解进行讲解，旨在帮助同学们更方便地理解原理与快速地跑通代码。
教程中部分示意图和代码参考自原教程，特此说明与致谢。
原教程Github仓库：https://github.com/rasbt/LLMs-from-scratch

首先我们需要安装 Python 和一些必要的包来运行代码。 本章节将介绍如何安装和设置 Python 环境。

安装 Python 和设置计算环境有多种方法。 下面介绍两种常用的方法，您可以根据自己的喜好选择其中之一。

### 选项 1：使用 uv

可以通过 `uv` 的 `uv pip` 接口进行 Python 设置和包安装。

#### （1） 安装 Python（如果尚未安装）

如果之前没有在系统上手动安装过 Python，强烈建议进行安装，这有助于防止与操作系统内置的 Python 安装发生潜在冲突，从而避免引发问题。
即使之前已经安装了 Python，也请检查是否安装了较新的版本，请在终端中执行以下代码：

```bash
python --version
```

注意： 如果 python --version 显示未安装 Python 版本，也可以尝试检查 python3 --version，因为您的系统可能配置为使用 python3 命令。

如果未安装 Python 或版本较旧，您可以按照以下说明为您的操作系统进行安装。

**Linux (Ubuntu/Debian)** 

```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev
```

**macOS**

如果使用 Homebrew，请使用以下命令安装 Python：

```bash
brew install python@3.13
```
或者，从官方网站下载并运行安装程序：https://www.python.org/downloads/

**Windows**

请从官方网站下载并运行安装程序：https://www.python.org/downloads/


### (2) 创建虚拟环境

建议在独立的虚拟环境中安装 Python 包，以避免修改您的操作系统可能依赖的系统级包。要在当前文件夹中创建虚拟环境，请按照以下三个步骤操作。

（1） 安装uv

```bash
pip install uv. # pip3 install uv
```



（2） 创建虚拟环境

```bash
uv venv --python=python3.13
```

（3） 激活虚拟环境

```bash
source .venv/bin/activate
```
注意： 如果你使用的是 Windows系统，可能需要将上面的命令替换为 `source .venv/Scripts/activate` 或 `.venv/Scripts/activate`

请注意，每次启动新的终端会话时，都需要激活虚拟环境。
例如，如果重启了终端或计算机，并希望第二天继续处理项目，只需在项目文件夹中运行 source .venv/bin/activate 即可重新激活虚拟环境。

进入项目文件的方法为在终端输入：

```bash
cd path/to/your/project/folder # 文件的路径
```

注：可以直接将文件拖进终端查看路径。

以及，可以执行 deactivate 命令来停用环境。

### （3）安装包

在激活虚拟环境后，可以使用 uv pip 安装所需的包。例如，要安装 numpy 和 pandas，可以运行以下命令：

```bash
uv pip install numpy pandas
```

如果要从 requirements.txt 文件安装所有必需的包，请运行以下命令（假设该文件位于您终端会话的同一目录中）：

```bash
uv pip install -r requirements.txt 
```

或 

```bash
uv pip install #your file path 
```

也可以从官方教程仓库中安装最新的依赖项目：

uv pip install -r [https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/requirements.txt](https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/requirements.txt)

注意： 如果使用windows系统，可能会因某些依赖项而在执行上述命令时遇到问题，可以回退到使用常规的 pip方式进行安装。

### （4）开始写代码

设置好一切后，您就可以开始使用代码文件了。例如，运行以下命令启动 JupyterLab：

```bash
jupyter lab
```

如果遇到 jupyter lab 命令的问题，也可以使用虚拟环境中的完整路径启动它。
在 Linux/macOS 上使用 .venv/bin/jupyter lab，或在 Windows 上使用 .venv\Scripts\jupyter-lab。

### 选项 2：使用 Conda

另一种流行的设置 Python 环境的方法是使用 Conda 包管理器和环境管理器。 

#### （1）下载并安装Miniforge
 
从 GitHub 仓库下载 miniforge：https://github.com/conda-forge/miniforge

根据的操作系统，这应该会下载 .sh (macOS, Linux) 或 .exe 文件 (Windows)。

对于 .sh 文件，打开您的命令行终端并执行以下命令：

```bash
sh ~/Desktop/Miniforge3-MacOSX-arm64.sh
```
其中 Desktop/ 是 Miniforge 安装程序下载到的文件夹，在不同的设备上，替换成对应的路径即可。

#### （2）创建 Conda 环境

安装成功完成后，建议创建一个名为 LLMs 的新虚拟环境，您可以执行以下命令：

```bash
conda create -n LLMs python=3.10
```

许多科学计算库不会立即支持最新版本的 Python。因此，在安装 PyTorch 时，建议使用比最新版旧一到两个版本的 Python。
例如，如果 Python 的最新版本是 3.13，建议使用 Python 3.10 或 3.11。

接下来，激活新虚拟环境（每次打开新的终端窗口或标签页时都必须执行此操作）：

```bash
conda activate LLMs
```

#### （3）安装新的Python库

要安装新的 Python 库，现在可以使用 conda 包安装程序。例如，可以按如下方式安装 JupyterLab 和 watermark：

```bash
conda install jupyterlab watermark
```

仍然可以使用 pip 来安装库。默认情况下，pip 应该链接到新的 LLMs conda 环境。

#### （4）安装 PyTorch  

PyTorch 可以像任何其他 Python 库或包一样使用 pip 安装。

```bash
pip install torch
```


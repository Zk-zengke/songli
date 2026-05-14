import json
import math
import random
from pathlib import Path

import numpy as np


TEXT = """
网络工程学习需要理解协议、地址、路由、DNS 和 HTTP。
生成式人工智能可以帮助我们解释概念、生成代码、整理排查流程。
但是 AI 的回答必须经过人工验证，尤其是网络故障分析和命令结果。
字符级语言模型的目标是根据前面的字符预测下一个字符。
训练过程包括编码文本、计算 loss、反向传播更新参数和生成新文本。
"""


def make_dataset(text):
    chars = sorted(set(text))
    stoi = {ch: i for i, ch in enumerate(chars)}
    itos = {i: ch for ch, i in stoi.items()}
    data = np.array([stoi[ch] for ch in text], dtype=np.int64)
    return chars, stoi, itos, data


def softmax(x):
    x = x - np.max(x, axis=1, keepdims=True)
    exp = np.exp(x)
    return exp / np.sum(exp, axis=1, keepdims=True)


def sample_batch(data, batch_size, rng):
    ix = rng.integers(0, len(data) - 1, size=batch_size)
    x = data[ix]
    y = data[ix + 1]
    return x, y


def train_bigram(data, vocab_size, batch_size=16, max_iters=300, learning_rate=1.0, seed=7):
    rng = np.random.default_rng(seed)
    weights = rng.normal(0, 0.01, size=(vocab_size, vocab_size))
    losses = []
    checkpoints = {0, 1, 10, 50, 100, max_iters - 1}

    for step in range(max_iters):
        x, y = sample_batch(data, batch_size, rng)
        logits = weights[x]
        probs = softmax(logits)
        loss = -np.log(probs[np.arange(batch_size), y] + 1e-12).mean()

        grad_logits = probs
        grad_logits[np.arange(batch_size), y] -= 1
        grad_logits /= batch_size
        grad_w = np.zeros_like(weights)
        np.add.at(grad_w, x, grad_logits)
        weights -= learning_rate * grad_w

        if step in checkpoints:
            losses.append({"step": int(step), "loss": round(float(loss), 4)})

    return weights, losses


def generate(weights, stoi, itos, start="网", max_new_chars=80, temperature=0.9, seed=11):
    rng = np.random.default_rng(seed)
    idx = stoi.get(start, 0)
    out = [itos[idx]]
    for _ in range(max_new_chars):
        logits = weights[idx] / temperature
        probs = softmax(logits.reshape(1, -1))[0]
        idx = int(rng.choice(len(probs), p=probs))
        out.append(itos[idx])
    return "".join(out)


def experiment(label, data, stoi, itos, batch_size, max_iters, learning_rate):
    weights, losses = train_bigram(
        data,
        vocab_size=len(stoi),
        batch_size=batch_size,
        max_iters=max_iters,
        learning_rate=learning_rate,
    )
    return {
        "label": label,
        "params": {
            "batch_size": batch_size,
            "max_iters": max_iters,
            "learning_rate": learning_rate,
            "vocab_size": len(stoi),
        },
        "losses": losses,
        "generated_text": generate(weights, stoi, itos),
    }


def main():
    random.seed(7)
    chars, stoi, itos, data = make_dataset(TEXT)
    results = [
        experiment("baseline", data, stoi, itos, batch_size=16, max_iters=300, learning_rate=1.0),
        experiment("modified_learning_rate", data, stoi, itos, batch_size=16, max_iters=300, learning_rate=0.35),
    ]
    output = {
        "dataset_chars": int(len(data)),
        "vocab_size": int(len(chars)),
        "concepts": {
            "token": "本实验把每一个中文字符、英文字符或标点看作一个 token。",
            "loss": "loss 表示模型预测下一个字符时的平均错误程度，越低说明模型越适应训练文本。",
            "next_token_prediction": "给定当前字符，模型输出下一个字符的概率分布，并从中采样生成文本。",
        },
        "results": results,
    }
    Path("作业一_字符级语言模型运行结果.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

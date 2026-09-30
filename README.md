# Transformer 
This is a **Transformer** based **Large Language Model (LLM)** training demo with only _~240 lines of code_.

Inspired by [nanoGPT](https://github.com/karpathy/nanoGPT), I wrote this demo to show how to train a LLM from scratch using PyTorch. 
The code is very simple and easy to understand. It's a good start point for beginners to learn how to train a LLM.

The demo is trained on a 450Kb [sample textbook](https://huggingface.co/datasets/goendalf666/sales-textbook_for_convincing_and_selling/raw/main/sales_textbook.txt) dataset, and the model size is about 51M. 
I trained on a single i7 CPU, and the training time takes about 20 minutes, result in approximately ~1.3M parameters.


# Get Started

1. Install dependencies

```
pip install numpy requests torch tiktoken
```
2. Run model.py

First time when you run it, the program will download the dataset and save to `data` folder.
Then the model will start training on the dataset. 
 
The training loss will decrease as the training goes on. After 5000 iterations, the training will stop and the losses are down to around `2.807`. The model will be saved under name `model-ckpt.pt`.

3. Step-by-step Jupyter Notebook

A step-by-step Jupyter Notebook `step-by-step.ipynb` to help you understand the architecture logic. To run this, you also need to insall:

```
pip install matplotlib pandas
```

This notebook prints out the intermediate results of each step followed by Transformer architecture from original paper, but only the **Decoder** part (Since GPT only use the decoder). So you can see how the model is trained each single step. For examples:


### References

- [Transformer Architecture: LLM From Zero-to-Hero](https://medium.com/@waylandzhang/transformer-architecture-llms-zero-to-hero-98b1ee51a838) - 
- [nanoGPT](https://github.com/karpathy/nanoGPT) Andrej Karpathy's famous video tutorial on how to build a GPT model from scratch.
- [Transformers from Scratch](https://blog.matdmiller.com/posts/2023-06-10_transformers/notebook.html) A clear and easy implementation of Andrej's video contents by Mat Miller.
- [Attention is all you need](https://arxiv.org/abs/1706.03762) The original paper of Transformer architecture.

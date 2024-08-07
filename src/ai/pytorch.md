# PyTorch
## Installation
### 根据OS和cuda选择适配的torch版本
https://pytorch.org/get-started/previous-versions/
### pip 
#### 安装最新版
```shell
pip install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple
```
#### 指定版本(preffered)
创建名为pytorch310的虚拟环境
```shell
conda create -n pytorch310 python==3.10
```
激活环境
```shell
conda activate pytorch310
```
设置清华源，加速安装
```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
指定版本安装
```shell
pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```
### conda
添加清华镜像源
```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```
#### 安装最新版
```shell
conda install pytorch torchvision torchaudio cudatoolkit=10.2
```
#### 指定版本
```shell
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4 cudatoolkit=10.2
```

## Tutorial
- [pytorch examples](https://github.com/pytorch/examples)
- [pytorch tutorials](https://github.com/pytorch/tutorials)
- pytorch模型性能分析和优化: [weixin](https://mp.weixin.qq.com/s/lxJthBk1L2nYOyQyLbqqEw)
- pytorch handbook: [[Github:zh-cn](https://github.com/zergtant/pytorch-handbook)]
- datawhale/thorough-pytorch: [[Github:zh-cn](https://github.com/datawhalechina/thorough-pytorch)]
- 杂七杂八的收集DL相关的东西： [[Github:en](https://github.com/aymericdamien/TopDeepLearning)]

## Framework
- [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning): Pretrain, finetune and deploy AI models on multiple GPUs, TPUs with zero code changes.

## Visualization
- [wandb](https://github.com/wandb/wandb): 🔥 A tool for visualizing and tracking your machine learning experiments. This repo contains the CLI and Python API.
- [PyTorch tensorboard](https://pytorch.org/docs/stable/tensorboard.html): How to use tensorboard in PyTorch.
- [SwanLab](https://github.com/SwanHubX/SwanLab): ⚡️SwanLab: track and visualize all the pieces of your machine learning pipeline. 跟踪与可视化你的机器学习全流程

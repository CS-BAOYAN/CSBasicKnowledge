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
# 若不含有`~/.condarc`，生成它
ls ~/.condarc || conda config --set show_channel_urls yes

# 之后配置镜像源（南科大提供的额外软件包镜像可以加速安装CUDA版Pytorch）
tee ~/.condarc > /dev/null << EOF
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  nvidia: https://mirrors.sustech.edu.cn/anaconda-extra/cloud
  
envs_dirs:
  - your-path/anaconda3/envs # 替换为您的路径（另外，若安装的是miniconda3，请自行替换），不设置此项有可能安装在`~/.conda/envs`中
EOF
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

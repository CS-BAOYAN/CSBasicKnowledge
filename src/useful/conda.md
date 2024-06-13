# Conda

- miniconda环境配置以及jupyter notebook使用指南: [[zhihu](https://zhuanlan.zhihu.com/p/449750184)]
- micromamba: miniconda 的平替，同时依赖解析等基础操作更快: [[GitHub](https://github.com/mamba-org/mamba)]
- [清华大学开源镜像站-miniconda的下载](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/)
  ```shell
  # 下载安装脚本
  wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh  
  
  # 修改权限
  chmod 777 Miniconda3-latest-Linux-x86_64.sh  
  
  # 执行安装脚本
  bash Miniconda3-latest-Linux-x86_64.sh
  
  # 删除安装脚本
  rm Miniconda3-latest-Linux-x86_64.sh  
  
  # 刷新环境变量
  source ~/.bashrc
  ```

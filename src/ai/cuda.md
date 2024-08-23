# CUDA & Nvidia

- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html): The programming guide to the CUDA model and interface.
- [NVIDIA/CUDALibrarySamples](https://github.com/NVIDIA/CUDALibrarySamples): The CUDA Library Samples are released by NVIDIA Corporation as Open Source software under the 3-clause "New" BSD license.
- [pybind11 documentation](https://pybind11.readthedocs.io/en/stable/basics.html)
- [Using pybind11](https://people.duke.edu/~ccc14/sta-663-2016/18G_C++_Python_pybind11.html)
- [Use pybind11 for a detailed but simple example](https://iamsorush.com/posts/pybind11-robot/)
- 查看你的显卡的情况:
  - nvitop: [[Github](https://github.com/XuehaiPan/nvitop)]
  - gpustat: [[Github](https://github.com/wookayin/gpustat)]
  - nvidia-smi
- - 切换CUDA版本步骤
  - 删除软连接
    ```shell
    cd /usr/local
    ls -l cuda #查看cuda的软链接
    sudo rm -rf cuda
    sudo ln -s /usr/local/cuda-10.0 /usr/local/cuda # 更换为对应的cuda
    ```
  - 添加环境变量
    ```shell
    # 假设你使用的是bash，那么你需要打开.bashrc
    export PATH="/usr/local/cuda-10.0/bin:$PATH"
    export LD_LIBRARY_PATH="/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH"
    export CUDA_HOME=/usr/local/cuda
    ```
    在完成上述步骤后，你需要 source ~/.bashrc

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
    ls -l cuda # 查看cuda的软链接
    sudo rm -rf cuda
    sudo ln -s /usr/local/cuda-10.0 /usr/local/cuda # 更换为对应的cuda
    ```
  - 添加环境变量
    ```shell
    # 修改`/etc/profile`以做到多用户、多Shell解释器通用
    sudo tee -a /etc/profile > /dev/null << 'EOF'
    # CUDA
    export PATH=${PATH}:/usr/local/cuda/bin
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda/lib64
    export CUDA_HOME=/usr/local/cuda # 通过设置软链接`/usr/local/cuda`，可以做到多版本CUDA共存
    EOF
    ```
    在完成上述步骤后，你需要`source /etc/profile`刷新环境变量或者`reboot`重启

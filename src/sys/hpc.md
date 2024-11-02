# HPC

* 高性能计算学习路线：[[Github: zh-cn](https://heptagonhust.github.io/HPC-roadmap/)]
* [高等数值分析（高性能计算，并行计算）](https://math.ecnu.edu.cn/~jypan/Teaching/ParaComp/): 华东师范大学高等数值分析（高性能计算，并行计算）
* 超算习堂：[[zh-cn](https://www.easyhpc.net/)]
* 并行计算课程：
  * CMU15-418 并行计算架构及编程：[[Bilibili](https://www.bilibili.com/video/BV1Xz4y1p7ZN)] [[课程主页](http://15418.courses.cs.cmu.edu/spring2016/lectures)]
  * 伯克利CS267 并行计算应用：[[Bilibili: en](https://www.bilibili.com/video/BV1qV411q7RS)] [[课程主页](https://sites.google.com/lbl.gov/cs267-spr2018/home)]
  * MIT6.172 软件系统性能优化：[[Bilibili](https://www.bilibili.com/video/BV1wA411h7N7)] [[课程主页](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/)]
* Labs：
  * CS149 并行计算(该课程与15-418一致) Lab：[[Github](https://github.com/stanford-cs149/asst1)]
  * HPC101 Lab：[[主页](https://www.zjusct.io/HPC101-Labs-2022/)]
* 其他资源：
  * [Rolf Rabenseifner拓扑算子的一种仿真实现](https://github.com/Justjustifyjudge/repo4mpi.git)，根据Optimization of Collective Reduction Operations给出的拓扑图完成的不同逻辑拓扑的Allreduce算子。
### OpenMPI的安装
> 更多内容可以查看：https://docs.open-mpi.org/en/v5.0.x/installing-open-mpi/quickstart.html
1. OpenMPI的下载及解压: 在[OpenMPI官方主页](https://www-lb.open-mpi.org/software/ompi/v5.0/)找到合适版本的OpenMPI下载并解压
   ```shell
   wget https://download.open-mpi.org/release/open-mpi/v5.0/openmpi-5.0.5.tar.gz
   tar xf openmpi-5.0.5.tar.gz
   cd openmpi-5.0.5
   ```
2. 配置安装路径，编译并安装，安装路径自定义
   ```shell
   ./configure --prefix=/usr/local/openmpi
   make -j $(nproc) all
   make install
   ```
3. 设置环境变量，路径为自己安装的路径
   ```shell
   MPI_HOME=/usr/local/openmpi
   export PATH=$MPI_HOME/bin:$PATH
   export LD_LIBRARY_PATH=$MPI_HOME/lib:$LD_LIBRARY_PATH
   export MANPATH=${MPI_HOME}/share/man:$MANPATH
   ```

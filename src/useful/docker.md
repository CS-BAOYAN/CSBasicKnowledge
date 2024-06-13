# Docker

- Docker-从入门到实践: [[zh-cn](https://docker-practice.github.io/zh-cn/)]
- How to Install PyTorch on the GPU with Docker: [[en](https://saturncloud.io/blog/how-to-install-pytorch-on-the-gpu-with-docker/)]
- Vscode连接远程服务器中的docker容器进行开发: [[CSDN](https://blog.csdn.net/qq_19716143/article/details/132310200?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-132310200-blog-125781144.235%5Ev38%5Epc_relevant_sort&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-132310200-blog-125781144.235%5Ev38%5Epc_relevant_sort&utm_relevant_index=1)]
- docker权限问题：[[CSDN](https://blog.csdn.net/weixin_44583856/article/details/120757864)]
- 如何临时退出一个正在交互的容器的终端，而不终止它？
  按 Ctrl-p Ctrl-q。如果按 Ctrl-c 往往会让容器内应用进程终止，进而会终止容器，如果没有在IDE里面没有成功，请去除IDE对应的快捷键。
- docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
  1. https://github.com/NVIDIA/nvidia-docker/issues/1238
  2. https://github.com/NVIDIA/nvidia-docker/issues/1243
- Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock:
  ```shell
  sudo chmod 666 /var/run/docker.sock
  ```
  

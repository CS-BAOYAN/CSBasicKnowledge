# CSBasicKnowledge

本仓库记录CS的一些基础知识，补全计算机专业缺少的一课。期待有缘人可以一起维护！

## CS

- CS 自学指南: [[zh-cn](https://github.com/PKUFlyingPig/cs-self-learning)] [[en](https://github.com/PKUFlyingPig/Self-learning-Computer-Science)]
- OI Wiki(ACMer必备): [[zh-cn](https://oi-wiki.org/)] 
- The Missing Semester of Your CS Education: [[en](https://missing.csail.mit.edu/)] [[zh-cn](https://missing-semester-cn.github.io/)]
- CS免费编程书籍：\[[Github](https://github.com/yinhonggen/free-programming-books-zh_CN)\]
- Crash Course Computer Science(个人觉得值得观看的计算机知识速成科普课程): [[Origin_YouTube](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulI)] [[CN_Bilibili](BV1EW411u7th)] [[CN_Source](https://github.com/1c7/crash-course-computer-science-chinese)]
- 在有用和没用之间徘徊的速查网站：\[[zh-cn](https://quickref.cn/)\]

## AI

### PyTorch

### HuggingFace

- 高速下载 huggingface 的超大体积的模型和数据集:
  - [Github: huggingface-go](https://github.com/xieincz/huggingface-go)
  - [AI快站](https://aifasthub.com/): 10MB/S下载的带宽资源
  - [国内huggingface加速镜像站](https://hf-mirror.com)

### Tutorials

- 一些国内的广为人知的视频教程，适合边睡边看：
  - 跟李沐学AI（bilibili）
  - 耿直哥（bilibili）
- 一篇不太专业的如何读论文的小文档：\[[pdf](./论文粗读攻略.md)\]
- paper with code：[[page](https://paperswithcode.com/)]
- 算法知识应知应会：[[Github](https://github.com/nosuggest/Reflection_Summary)]
- Microsoft AI-EDU: [[zh-cn](https://microsoft.github.io/ai-edu/index.html)]
- 机器学习入门指南: [[zh-cn](https://tjxj.github.io/)]
- CS229机器学习技巧和秘诀速查表: [[zh-cn](https://stanford.edu/~shervine/l/zh/teaching/cs-229/cheatsheet-machine-learning-tips-and-tricks#)]
- 科学空间(苏剑林): [[zh-cn](https://spaces.ac.cn/)]
- 深度学习500问: [[Github: zh-cn](https://github.com/scutan90/DeepLearning-500-questions)]
- awesome-ai-tools: [[Github: en](https://github.com/NoFish-528/awesome-ai-tools)]
- Learning Research: [[Github: zh-cn](https://github.com/pengsida/learning_research)]
- Stanford HowToReadpaper: [[page](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)] [[pdf](./HowtoReadPaper.pdf)]

### prompts

- ChatGPT 中文调教指南: [[Github: zh-cn](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)]
- Awesome ChatGPT Prompts: [[Github: en](https://github.com/f/awesome-chatgpt-prompts)]

## Shell

- Linux命令搜索:[[zh-cn](https://jaywcjlove.gitee.io/linux-command/)]
- explainshell: [[page](https://explainshell.com/)]
- Bash scripting cheatsheet: [[en](https://devhints.io/bash)]
- The art of command line: [[Github: zh-cn](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)]

## Vim

- `vimtutor` 关于 vim 最基础的教程，安装 vim 之后自带的命令
- 聪明地学习 vim: [[GitHub: en](https://github.com/iggredible/Learn-Vim)]/[[GitHub: zh-cn](https://github.com/wsdjeg/Learn-Vim_zh_cn/tree/88c823118735d1a39c3e04451304c1c2c91a5ac3)]

## Git & Github

- Learn Git Branching(强推): [[zh-cn](https://learngitbranching.js.org/?locale=zh_CN)]
- Pro Git 中文版：[[zh](https://www.progit.cn/)]
- 约定式提交，或许可以规范你的Github提交：\[[zh-cn](https://www.conventionalcommits.org/zh-hans/v1.0.0/)\]
- Commit message 和 Change log 编写指南：[[zh-cn](https://ruanyifeng.com/blog/2016/01/commit_message_change_log.html)]
- commitizen/cz-cli: [[Github](https://github.com/commitizen/cz-cli)]
- 第一次参与开源项目，如何提交pr: [[Github: zh-cn](https://github.com/firstcontributions/first-contributions/blob/main/translations/README.zh-cn.md)]

## How to Debug

### pdb

- 10分钟教程掌握Python调试器pdb: [[zhihu](https://zhuanlan.zhihu.com/p/37294138)]

### debugpy

- vscode python设置debug: [[zhihu](https://www.zhihu.com/question/35022733/answer/3178874019)]

### vscode debug setting

## Linux常用指令

- 中科大 LUG 基础 Linux 教程: [[zh-cn](https://101.lug.ustc.edu.cn/)]

## Conda & Docker

### Conda

- miniconda环境配置以及jupyter notebook使用指南: [[zhihu](https://zhuanlan.zhihu.com/p/449750184)]
- micromamba: miniconda 的平替，同时依赖解析等基础操作更快: [[GitHub](https://github.com/mamba-org/mamba)]

### Docker

- Docker-从入门到实践: [[zh-cn](https://docker-practice.github.io/zh-cn/)]
- How to Install PyTorch on the GPU with Docker: [[en](https://saturncloud.io/blog/how-to-install-pytorch-on-the-gpu-with-docker/)]
- 如何临时退出一个正在交互的容器的终端，而不终止它？
  
  按 `Ctrl-p Ctrl-q`。如果按 `Ctrl-c` 往往会让容器内应用进程终止，进而会终止容器，如果没有在IDE里面没有成功，请去除IDE对应的快捷键。

## CUDA & Nvidia

- 切换CUDA版本步骤: [[CSDN](https://blog.csdn.net/u013905398/article/details/103799621)]
- 查看你的显卡的情况:
  - nvitop: [[Github](https://github.com/XuehaiPan/nvitop)]
  - gpustat: [[Github](https://github.com/wookayin/gpustat)]
  - nvidia-smi

## CV & Resume

- Awesome Resume for Chinese: [[Github: zh-cn](https://github.com/dyweb/awesome-resume-for-chinese)]
- cv_emuluate: Academic CVs that you can (hopefully) emulate: [[Github](https://github.com/hongtaoh/cv_emulate)]

## System

- 机器学习系统：设计和实现: [[page](https://openmlsys.github.io/)] [[Github: zh-cn](https://github.com/openmlsys/openmlsys-zh)]
- 机器学习编译：[[Page](https://mlc.ai/summer22-zh/)] [[Bilibili](https://www.bilibili.com/video/BV15v4y1g7EU/)] [[Notes](https://mlc.ai/zh/)] 

## LaTeX & Markdown

- latex codebook: [[Github: zh-cn](https://github.com/xinychen/latex-cookbook)]
- LaTeX教程，篇幅较大，但是好用：\[[官网](https://ctan.org/tex-archive/info/lshort/chinese)\]\[[镜像](http://mirrors.cqu.edu.cn/CTAN/info/lshort/chinese/lshort-zh-cn.pdf)\]\[[Github](https://github.com/CTeX-org/lshort-zh-cn)\]
- Latex公式识别：[[网站](https://www.simpletex.cn/ai/latex_ocr)]
- Overleaf（在线Latex编辑器）：[[网站](https://www.overleaf.com/)]

## Academic

- 谷歌学术：Google Scholar [[en](https://scholar.google.com)]
- 计算机科学文献数据库：DBLP [[en](https://dblp.org/)]
- SCI期刊查询和scihub各种科研导航: [[Page](https://www.ablesci.com/journal )]
- ACM数字图书馆：ACM Digital Library [[en](https://dl.acm.org/)]
- IEEE学术数据库：IEEE Xplore [[en](https://ieeexplore.ieee.org/)]
- SCI论文检索：Web of Science [[en](https://www.webofscience.com/)]
- EI论文检索：Engineering Village [[en](https://www.engineeringvillage.com/)]
- 中文文献检索：中国知网 [[zh-cn](https://www.cnki.net/)]
- 中国计算机学会（CCF）推荐国际学术会议和期刊目录（2022版）[[pdf](./CCF_Recommended_List.pdf)]
- CCF会议投稿截止时间汇总：[[zh-cn](https://ccfddl.github.io/)]
- 清华大学计算机学科推荐学术会议和期刊列表 (TH-CPL) [[Github](https://github.com/bugaosuni59/TH-CPL)]
- CSRankings: Computer Science Rankings [[en](https://csrankings.org/)]

## MISC

- 如何设置代理: [[PDF](./如何设置代理.pdf)]
- 耗时很长的程序忘加nohup就运行了怎么办？: [[zhihu](https://www.zhihu.com/question/586298694/answer/2991647868)]
- linux 多线程下载工具-aria2c: [[zhihu.com](https://zhuanlan.zhihu.com/p/637294044)]
- 你的指法真的标准吗？打字练习一下：\[[zh-cn](https://qwerty.kaiyi.cool/)\]
- 利用学生身份可以享受到的相关学生优惠权益: [[Github](https://github.com/ivmm/Student-resources)]
- 论文常用词汇i.e.，e.g.，etc.，viz.，et al.的前世今生: [[zhihu](https://zhuanlan.zhihu.com/p/63640148)]
- 图吧工具箱: [[page](http://www.tbtool.cn/)]
- 文献管理软件Zotero安装设置教程及各插件配置（知网支持、影响因子、被引数: [[zh-cn](https://www.starryfk.com/tec/zotero-settings-and-plugins-for-literature-management-software.html)]
- 阿里巴巴矢量图标库: [[page](https://www.iconfont.cn/)]
- 程序员延寿指南: [[Github: zh-cn](https://github.com/geekan/HowToLiveLonger)]
- 程序员做菜指南: [[Github: zh-cn](https://github.com/Anduin2017/HowToCook)]

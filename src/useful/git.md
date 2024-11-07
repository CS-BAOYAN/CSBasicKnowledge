# Git & Github

- Learn Git Branching(强推): [[zh-cn](https://learngitbranching.js.org/?locale=zh_CN)]
- [Pro Git 中文版](https://www.progit.cn/)
- [Git lfs install](https://github.com/git-lfs/git-lfs/wiki/Installation#ubuntu)
- Gitchat: [[zh](https://wkevin.github.io/GitChat/gitchat.html#round-1-%E8%B5%B7%E6%AD%A5)]
- Git规范化提交
  - 约定式提交，或许可以规范你的Github提交：\[[zh-cn](https://www.conventionalcommits.org/zh-hans/v1.0.0/)\]
  - Commit message 和 Change log 编写指南：[[zh-cn](https://ruanyifeng.com/blog/2016/01/commit_message_change_log.html)]
  - commitizen/cz-cli: [[Github](https://github.com/commitizen/cz-cli)]
- 第一次参与开源项目，如何提交pr: [[Github: zh-cn](https://github.com/firstcontributions/first-contributions/blob/main/translations/README.zh-cn.md)] | [[mmcv contribution](https://mmcv.readthedocs.io/zh-cn/latest/community/contributing.html)]
- [给 Github Desktop 设置代理](https://xieincz.github.io/post/gei-github-desktop-she-zhi-dai-li/)
- clone远程仓库的指定分支
  ```bash
  git clone -b + 要clone的分支名 + 仓库地址 
  # eg: git clone -b dev git@github.com:CS-BAOYAN/CSBasicKnowledge.git
  ``` 
- SSH key的生成：
  - 检查SSH key是否存在：
    ```bash
    ls -al ~/.ssh
    # Lists the files in your .ssh directory, if they exist
    ``` 
  - 生成SSH key, 会在/your_home_path/.ssh/生成id_rsa和id_rsa.pub
    ```bash
    ssh-keygen -t rsa -C "your_email@example.com"
    # Creates a new ssh key using the provided email
    Generating public/private rsa key pair.
    Enter file in which to save the key (/your_home_path/.ssh/id_rsa):
    ```
- 下拉/提交远程仓库
  - 查看远程仓库的信息：
  ```bash
  git remote -v
  ```
  可以看到远程仓库的名字和地址。
  - 查看当前分支名：
  ```bash
  git branch
  ```
  可以看到当前代码分支的名字
  - 从远程仓库下拉：
  ```bash
  git pull <远程仓库的名字/地址> <代码的分支名>
  ```
  - 冲突处理（苯人的笨方法）
  ```bash
  git pull <远程仓库的名字/地址> <代码的分支名> --allow-unrelated-histories
  ```
  然后使用
  ```bash
  git status
  ```
  查看冲突文件，手动解决冲突。
  - 提交本地代码到远程仓库：
  ```bash
  git push <远程仓库的名字/地址> <代码的分支名>
  ```
  - 强制推送(苯人的笨方法，高风险，慎用)：
  ```bash
  git push -f <远程仓库的名字/地址> <代码的分支名>
  ```
  - 推送tags到远程仓库：
  ```bash
  git push --tags
  ```
  - 删除远程分支：
  ```bash
  git push origin --delete <分支名>
  ```
  - 同步本地分支到远程仓库：
  ```bash
  git push origin <本地分支名>:<远程分支名>
  ```
  - 同步远程分支到本地仓库：
  ```bash
  git checkout -b <本地分支名> <远程分支名>
  ```


### 1
- 新学的git命令顺序：
- git status 看有什么文件不同
- git add 可以加入文件的track（一般使用git add .）
- git commit -m '提交的注释'将管理的文件提交
- git pull 拉取最新的远程版本
- git push origin master 推送最新的远程版本
### 2
- mysql 在 centos上面的部署（颇有点折磨），临时密码：/L2y7kGaez-i
- 启动数据库：systemctl start mysqld
- 首次登陆方式：grep 'temporary password' /var/log/mysqld.log查到临时密码
- 登陆数据库：mysql -u root -p
- 使用ALTER USER USER() IDENTIFIED BY '自己的密码';  才能查看数据库
- 关闭数据库：systemctl stop mysql
- 使用 ps aux | grep mysql 来查看mysql的使用情况
- 使用 vim /etc/my.cnf 来用vim修改mysql的配置
### 3
- user表创建完成，里面只放了一条密码为姓名md5加密，用户名为admin，id为1的用户数据
- mysql远程登陆的用户：create user 'zhanyiqidong'@'%' identified by 's17S!&zhanyi_linyifan';
- grant select on users.* to 'zhanyiqidong'@'%'; 为远程账户赋予查看某database的权限
- flush privileges; 刷新权限（权限更改之后的操作）
- 即使远程机关闭了防火墙，也要用腾讯云管理端口，不然用不了端口3306，可恶
- 创建了一个新用户，admin，密码是Admin123!@#
### 4
- 经典重要命名规则：大写字母开头的是类，小写字母开头的是方法或者变量，方法使用驼峰或者蛇形命名（但是要选一个写到底），凡哥在这里吃了点亏
- 尽量不要用双下划线或者单下划线开头的命名：双下划线留给Python库，单下划线用来标识类内私有，类外无法访问的方法。
- 虚拟环境的重要性！！！不然项目多了很容易出现包冲突
- 使用pip freeze > /route/requirements.txt 来保存当前虚拟环境的配置
### 5
- from pymysql.cursors import DictCursor 可以返回字典形式
- pymysql中的cursors可以帮忙完成对mysql数据库的访问。
### 6
- Vue是即将于JavaScript的。（天生异步）
- Vue是数据驱动的，具有生命周期（需要知道在什么情况下执行什么样的东西）
- 打开要创建Vue项目的文件夹，cmd使用Vue create 自命名 来创建项目，然后选择配置，凡哥选的是ESLint+Prettier的语法，配置选择In dedicated config files，保存在各自的配置文件中。
- 使用npm init vue@latest 来创建vue项目。
- 使用npm install安装依赖。
- 使用npm run serve 来运行vue项目。
- index.html是html入口文件，初始化用的，据说所有的代码都要在这个文件中运行。
### 7
- 环境中可以使用pip3 freeze requirements.txt来生成当前环境的依赖文本。
### 8
- 修改登陆后界面的工作栏可以在AppAside.vue处进行修改
### 9
- 当前进展：正在完成登陆后的第一个界面的五个按钮的设计，规划route已完成，按钮格式还没设计好，具体的.vue文件还没有完成。
- 已完成五个按钮的设计和大小调整，需要完成点击各个按钮时的动作的route规划，既要搞后端flask的逻辑还要搞前端显示和交互的逻辑。
### 10
- 当前进展：在昨晚已经将所有的接口调试完成，接下来只需完成跑模型生成图片的嵌入。
- 2024年3月7日15:37:54，现在跑后端没有正常的反应，没法显示结果图。
- 已修复
### 11
- 2024年3月7日16:47:39，完成了卓文哥的模型功能的嵌入，还有很多问题没有修改，但是不管了。
- 这个项目就到这里吧，一年的时间，后期属实折磨我这个负责人。
### 如何使用git上拉下的Python项目

- 在电脑上创建一个虚拟环境
- 进入自己的虚拟环境
- pip install -r requirements.txt

### 一点感悟
- Python的特点：万物一类。不管是什么东西，先考虑给它建个类，后面把各种东西封装好了从类的表面来调接口。
- 永远不要指望只跟着一个教程一站式完成自己的功能点。永远要带有怀疑，要多方查找资料，而且要学会查找资料。
- 永远不要指望队友提供封装好的接口，甚至不要预期有可运行的代码。任何时候都要留下可以自己单挑完成项目的时间余地。

### 一点抱怨
- 软著项目前端参考了仓库https://github.com/Vegemo-bear/Vue3-LiteAI。没有很多自己的东西。任务分配的时候是写前端的，最后还是要前后端包打，还要从最基础的模型开始读起，队友的代码里面注释很少，连地址也是硬链接写在代码里的（简直可以把运维逼疯的那种），没有调用的函数接口，运行逻辑写在__main__()里面，没有裸露的画图的接口。。。偏偏我Python底子还很一般。模型的代码里还不知道有多少东西是原创的，感觉既惭愧又绝望，目前不知道要怎么写完了，每次写一会就逃避去打LeetCode，去刷视频。
- 自己太菜了，又菜又绝望，快过年了还没有时间去陶瓷，也没有时间出去玩，天天就是盯着这个项目等时间到了吃饭下班，偏偏这个项目进展完全卡住。
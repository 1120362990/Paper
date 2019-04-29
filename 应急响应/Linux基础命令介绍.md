# Linux基础命令介绍

## 账户权限管理

    用户名和 UID 被保存在/etc/passwd文件中，文件权限 (-rw-r--r--)  
    组和GID 被保存在 /etc/group文件中，文件权限(-r--------)  
    用户口令(密码)被保存在 /etc/shadow文件中  ，文件权限(-rw-r--r-- )  
    组口令被保存在 /etc/gshadow文件中 ，文件权限 (-r--------)  

1. 口令文件 /etc/passwd
    每个用户一条记录，七个字段组成
    字段|说明
    -|-
    name|用户名
    password|在此文件中的口令是X，这表示用户的口令是被/etc/shadow文件保护的
    uid|用户的识别号，是一个数字。每个用户的uid都是唯一的
    gid|用户的组的识别号，也是一个数字，每个用户账户在建立好后都会有一个主组。主组相同的账户其GID相同
    description|用户的个人资料
    home|用户的主目录，通常在/home下，目录名和账户名相同
    shell|用户登陆后启动的shell，默认是/bin/bash

2. 口令文件（密码） /etc/shadow
    每个用户一条记录，九个字段组成
    字段|说明
    -|-
    用户名|用户登陆名
    口令|用户的密码，是加密过的（MD5，SHA512等）。星号代表账户被禁用，双叹号表示这个密码被锁定
    最后一次修改的时间|从1970年1月1日起，到用户最后一次更改密码的天数
    最小时间间隔|从1970年1月1日起，到用户应该更改密码的天数
    最大时间间隔|从1970年1月1日起，到用户必须更改密码的天数
    警告时间|在用户密码过期之前多少天提醒用户更新
    不活动时间|在用户密码过期之后到禁用账户的天数
    失效时间|从1970年1月1日起，到用户被禁的天数
    标志|保留位

3. 组账号文件 /etc/group
    每一个组一条记录，每条记录4个字段组成
    字段|说明
    -|-
    组名|这是用户登陆系统时的默认组名，它在系统中是唯一的
    口令|组口令，由于安全性原因，已不使用该字段保存口令，用X占位
    组内用户列表|属于该组的所有用户名表，列表中多个用户间用，分割

4. 组口令文件 /etc/gshadow
    每一个组一条记录，每条记录4个字段组成
    字段|说明
    -|-
    组名|组名称，该字段于group文件中的组名称对应
    加密的组口令|用于保存已加密的口令
    组的管理员账户|管理员有权对该组添加删除账户
    组内用户列表|属于该组的用户成员列表，列表中多个用户间用，分割

## 文件权限

1. i 不可修改权限
    chattr +I filename    给文件添加不可修改权限  
    chattr -I filename    将文件的不可修改权限去掉  
    lsattr filename    查看文件是否设置了相关权限  
    如果设置了该参数，则无论任何人想要删除改文件均需要将此权限去掉  
2. a 只追加权限
    chattr +a filename    给文件添加只追加权限  
    chattr -a filename    将文件的只追加权限去掉  
    lsattr filename     查看文件的相关权限设置  
    这个权限让目标只能追加，不能删除，而且不能通过编辑器追加  

## 计划任务 - crontab

1. 创建计划任务  
    crontab -e 新建或编辑已有的计划任务。选择一个可用的编辑器，vim就好。然后编写需要执行的命令。  
    使用这个命令创建计划任务后，会在 /var/spool/cron/crontabs 目录下创建一个以用户名为名的文件，这个文件中就保存了这个用户需要运行的计划任务

    crontab 命令格式说明：  
    分钟|小时|几号|月份|星期几|要执行的命令  
    -|-|-|-|-|-
    0-59|0-23|1-31|1-12|0-7|各种命令，可以是脚本或wget这种系统命令

    例子：  
    如下是每分钟执行一次的命令  
    `*/1 * * * * wget http://192.168.3.150:8000/1.txt`  
    `*/1 * * * * /root/test/1.sh`  
    每小时的第3和第15分钟执行  
    `3,15 * * * * command`  
    在上午8点到11点的第3和第15分钟执行  
    `3,15 8-11 * * * command`  
    每隔两天的上午8点到11点的第3和第15分钟执行  
    `3,15 8-11 */2 * * command`  
    每个星期一的上午8点到11点的第3和第15分钟执行  
    `3,15 8-11 * * 1 command`  
    每天18 : 00至23 : 00之间每隔30分钟重启smb  
    `0,30 18-23 * * * /etc/init.d/smb restart`  
    每小时执行/etc/cron.hourly目录内的脚本  
    `01 * * * * root run-parts /etc/cron.hourly`  

2. 删除计划任务  
    crontab -r  
    或删除 /var/spool/cron/crontabs 目录下对用用户名的文件。  

3. 查看当前存在的计划任务  
    crontab -l  
    在 /var/spool/cron/crontabs 这个目录中查找也可以。

4. 系统任务调度配置文件  
    /etc/crontab  
    第一行SHELL变量指定了系统要使用哪个shell，这里是bash，第二行PATH变量指定了系统执行 命令的路径  

    ```shell
    root@kali:/etc# cat crontab
    # /etc/crontab: system-wide crontab
    # Unlike any other crontab you don't have to run the `crontab'
    # command to install the new version when you edit this file
    # and files in /etc/cron.d. These files also have username fields,
    # that none of the other crontabs do.

    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed
    17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
    25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
    ```

## 查看文件

1. 查看文件的头5行  
    cat crontab | head -n 5  
# git和github某些操作指南

## git提交文件时自动忽略某些文件-设置.gitignore

1. 桌面版github  Repository  ->   Repository settings  ->  ignored files  即可创建

    ```txt
    格式类似如下
    *.pyc
    *.xml
    *.iml
    ```

2. 对于已经同步到github的文件，如上配置后也是没有用的，需要用如下命令将目标文件清除,然后再同步即可
    > `git rm --cached F:\GitHub\vulnerability-list\zabbix_vuln\__pycache__\*`

### 参考

1. https://help.github.com/en/articles/ignoring-files
2. https://github.com/github/gitignore

## 如何配置git账户及邮箱

1. 配置账户 `git config --global user.name "rpkr"`
2. 配置邮箱 `git config --global user.email "13591644403@139.com"`
3. 查看当前账户 `git config --global user.name`
4. 查看当前邮箱 `git config --global user.email`

## 配置ssh公钥

1. 使用该命令生成公钥 `ssh-keygen -t rsa -b 4096 -C "13591644403@139.com"`
2. 将 /root/.ssh/id_rsa.pub 中的内容复制到github的ssh中
3. 运行`ssh -T git@github.com`命令，测试连接是否成功。注意，此处如有询问，输入`yes`即可。

### 最后向github同步文件的时候会需要输入账户密码
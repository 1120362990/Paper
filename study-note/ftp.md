# ftp

搭建ftp环境 `docker run --privileged   -d -p 4321:21 -p 20:20 -p 21100-21110:21100-21110 -v /data/docker/ftpserver/ftpFile:/home/vsftpd -e FTP_USER=user -e FTP_PASS=pssword -e PASV_ADDRESS=192.168.3.35 -e PASV_MIN_PORT=21100 -e PASV_MAX_PORT=21110 --name vsftpd --restart=always fauria/vsftpd`

windows下连接ftp，`open 192.168.3.123 5555`,然后分别输入用户名和密码即可登陆到ftp服务器中。
`ls`即可查看ftp中的文件。

最好使用 FileZilla 。

hydra `hydra -L FTP-user.txt -P FTP-passwd.txt -V -s 4321 192.168.3.35 ftp`
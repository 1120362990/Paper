# 文件上传

这里以 upload-labs 为测试例子

## 第一关/第二关

1. 第一关是前端js认证  
2. 第二关检测 MIME ，即 `Content-Type`  

上传一个这种名字的木马 `lic.php.jpg` ，burp抓包将 `.jpg` 去掉即可。

## 第三关

php3、php4、php5、pht和phtml 也会被apache认为是php文件，实际测试失败，黑名单禁止php文件时尝试绕过
没成功

## 第四关

前提，  支持  .htaccess  文件解析。  
首先上传  .htaccess  文件：

```txt
<FilesMatch "03.jpg">
SetHandler application/x-httpd-php
</FilesMatch>
```

再上传 03.jpg （php木马） ，然后访问03.jpg 即可得到shell

## 第五关

提示可以 phP  绕过后缀检查   没成功

## 第六关

后尾加空格，上传后访问404，失败   没成功

## 第七关

针对windows特性的绕过，后尾加个.。   没成功

## 第八关

针对windows特性的绕过，后尾加  ::$DATA  。  没成功

## 第十关

双写绕过  pphphp 。  成功

## 第十一关

说是00截断，看提示不像，没成功。  
00截断解读：http://www.admintony.com/关于上传中的00截断分析.html  
00截断url，cookie中可直接%00 ，在post包中需要编码hex  00

## 第十二关

00截断  没成功







# Django

## **新建APP**-Django-test1

通过如下方式进入命令行界面  
> Tools > Run manage.pt Task...

如上进入命令行，执行如下命令创建APP
> startapp message

右键，新建目录static，用来存放静态文件。css、图片  
新建log目录，用来存放日志。  
新建media，用来存放用户的上传文件夹  
将 APP mark为Sources Root，可以直接引用 views，得的输入路径

- 新建的APP需要注册到setting当中-INSTALLED_APPS

---

## 数据库相关操作-modules

生成默认的数据表
> makemigrations  
migrate

针对某个app生成数据表，实际上是此APP的modules定义的
> makemigrations messages  (Tips: messages is a apps)  
migrate message

## **models**-Django-test2

1. 要扩展默认的数据表，首先要在modules中引入如下包
    > from django.contrib.auth.models import AbstractUser

2. 扩展原有的models-users
    1. 继承原有的usermodule
    2. 并扩展其内容后
    3. 完成app的注册后，还要加上下面这一行
        > ROOT_URLCONF = 'Django_test2.urls'  
        - Django_test2为项目名

3. 接下来就可以创建相应的数据表了
    > makemigrations  app_name  
    > migrate
- 如果出现表冲突的情况，比如之前存在表，又migrate了一下，就会出现 migrate 失败的情况。可以把所有的表都删除，然后再migrate回来，即可解决

### 循环引用

在设计中要避免出现循环引用的情况
这里的问题主要是针对那些可能出现紧密联系的数据表，相对独立的功能不会出现这样的问题

- django app编写，分层结构
- users models.py 编写
- courses.py 编写
- organization models.py 编写
- operation models.py 编写  记录用户相关的操作

```
                  operation                        #上层app，可以import下层app，避免循环引用
     course     orgainization     users            #下层app

# _*_ coding:utf-8 _*_
from django.db import models


# django 常用的类型
# models.ForeignKey  #外键
# models.DateTimeField  #时间
# models.IntegerField   #整形
# models.IPAddressField  #IP地址
# models.FileField    #文件类型
# models.ImageField    #图像类型

class UserMessage(models.Model):
    #不设置主键的话，django生成数据表的时候，会默认自动生成一个。也可以像下面这样自己定义一个主键
    object_id = models.CharField(max_length=50,default="",primary_key=True,verbose_name=u"主键")
    name = models.CharField(max_length=20,verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100,verbose_name=u"联系地址")
    message = models.CharField(max_length=500,verbose_name=u"留言信息")
    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name
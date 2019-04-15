"""DjangoTTT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#配置目录的访问时需要先把相应的方法import进来
from message.views import getform

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'index/', getform,name='go_form'),  #使用namegoform给url起一个别名，后期好管理.html页面中也需要做相应的更改.这样可以随意该目录，而不用改其它部分

]

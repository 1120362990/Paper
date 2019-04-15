# _*_ coding:utf-8 _*_
from django.shortcuts import render

#要使用module来查询数据库中的数据，首先要把相关的module import进来
from .models import UserMessage

# Create your views here.

#创建目录访问后的返回方法
def getform(request):
    all_messages = UserMessage.objects.all()   #将数据库中的所有记录返回。结果支持for循环,查询
    filter_message = UserMessage.objects.filter(name='22',address='jh')   #数据表的条件查询
    for messages in all_messages:
        print(messages.name) #在这里可以按列名来取值

    #做一下判断，是否取出了数据
    message = None
    all_messages = UserMessage.objects.filter(name='bbb')
    if all_messages:
        message = all_messages[0]
    #可以像下面正这样向html页面返回一个数组
    # return render(request,'message_form.html',{
    #     "my_message":message
    # })

    # 向数据库中存储数据
    # user_message = UserMessage()
    # user_message.name = 'asdsad'
    # user_message.message = 'adwadw'
    # user_message.address = 'asdasdasdsa'
    # user_message.email = '7777tg@.com'
    # user_message.object_id = 2333
    # user_message.save()   #向数据库中存储数据

    #获取客户端提交过来的数据
    if  request.method == "POST":
        name = request.POST.get('name','')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
    try:
        print(name,message,email,address)
    except:
        print('无表单')

    #删除被查询出来的项目
    del_messages = UserMessage.objects.filter(name='sdas',address='sadasd')
    for message in del_messages:
        message.delete()

    return render(request, 'message_index.html',{
        "my_message":message
    })
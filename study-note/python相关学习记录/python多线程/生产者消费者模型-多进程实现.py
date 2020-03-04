# -*- coding: utf-8 -*-
import multiprocessing
from time import ctime

#q是一种队列
def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        #处理项
        item = input_q.get()  #从队列里拿出一个东西出来
        print("pull",item,"out of q") #此处替换为有用的工作
        input_q.task_done() #发出信号，通知任务完成
    print("Out of consumer:",ctime()) #此行未执行，因为q.join()收集到四个task_done()信号后，主进程启动，未等到print此句完成

def producer(sequence,output_q):   #sequence  准备放到q里面的商品
    print("Into producer:",ctime())
    for item in sequence:
        output_q.put(item)  #将生产的东西放进队列中
        print("put",item,"into q")
    print("Out of producer:",ctime())

#建立进程
if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    cons_p = multiprocessing.Process(target = consumer,args = (q,))
    cons_p.deamon = True
    cons_p.start()

    #生产多个项，sequence代表要发送给消费者的项序列
    #在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)
    #等待所有项被处理
    q.join()
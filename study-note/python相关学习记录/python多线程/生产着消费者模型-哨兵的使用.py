# -*- coding: utf-8 -*-
import multiprocessing
from time import ctime

#设置哨兵问题
def consumer(input_q):
    print("Into producer:",ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull",item,"out of q")
    print("Out of consumer:",ctime()) #从句执行完成，再转入主进程

def producer(sequence,output_q):
    print("Into procuder:",ctime())
    for item in sequence:
        output_q.put(item)
        print("put",item,"into q")
    print("Out of producer:",ctime())

if __name__ == "__main__":
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target = consumer,args = (q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence,q)

    #这里存在的问题是，如果有多个消费者，只放一个哨兵，那面只有一个消费者会退出，其他的还会在继续等待取值
    q.put(None)
    cons_p.join()

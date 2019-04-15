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
    cons_p1 = multiprocessing.Process(target = consumer,args = (q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target = consumer,args = (q,))
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence,q)

    #有几个消费者就放几个哨兵，每个哨兵可以用来关闭一个消费者
    q.put(None)
    q.put(None)
    cons_p1.join()
    cons_p2.join()

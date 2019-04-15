# -*- coding: utf-8 -*-
import threading
import time
import queue
#python2
#from Queue import Queue

#queue 队列学习   生产者消费者模型，消息对列  数据产生的速度和消费的速度不对等    

#生产者函数
class Producer(threading.Thread):
    def run(self):
        # global q
        count = 0
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '生成产品'+str(count)
                    q.put(msg)
                    print(msg)
            time.sleep(0.5)

#消费者函数
class Consumer(threading.Thread):
    def run(self):
        # global q
        while True:
            if q.qsize() > 100:
                for i in range(3):
                    lock.acquire()
                    msg = self.name + '消费了'+q.get()
                    print(msg)
                    print(q.qsize())
                    lock.release()
                time.sleep(1)

if __name__ == "__main__":
    q = queue.Queue()
    lock = threading.Lock()
    for i in range(5000):
        q.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()


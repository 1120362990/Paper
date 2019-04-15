# -*- coding: utf-8 -*-
import threading,queue,sys
import requests
requests.packages.urllib3.disable_warnings()   #移除报错
class RedisUN(threading.Thread):
    def __init__(self,queue1):
        threading.Thread.__init__(self)
        self._queue = queue1
    def run(self):
        while True:
            if self._queue.empty():
                break
            #实际工作的代码区域
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
            url = self._queue.get(timeout=0.5)
            try:
                response = requests.get(url,headers=headers,timeout=15,verify=False).status_code
                lock.acquire()
                print(url +'	'+str(response))
                f2.write('\n'+url +'	'+str(response))
                lock.release()
            except:
                lock.acquire()
                print(url +'	'+'Time out or some Error!')
                f2.write('\n'+url +'	'+'Time out or some Error!')
                lock.release()
def main():
    global f2
    f2 = open('test.txt','w+')
    xujiancedeURL = open("daijianURL.txt","r") #读取所要检测的url列表。就是提供给核心代码区域的参数
    thread_count = 1000  #线程数
    threads = []
    global lock
    lock = threading.Lock()
    queue1 = queue.LifoQueue()
    for line in xujiancedeURL:
        line = line.strip('\n').strip('\ufeff')   #读取每一行
        queue1.put(line)
    for i in range(thread_count):
        threads.append(RedisUN(queue1))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    xujiancedeURL.close()
    f2.close()
if __name__ == '__main__':
    main()
    print('all done')




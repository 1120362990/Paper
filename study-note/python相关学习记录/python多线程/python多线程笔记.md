# 多线程笔记
## threading的使用
- 声明一个线程，target是函数名，没有括号。参数放在args里面。一个参数的形式如下，没有参数也需要占位
> t = threading.Thread(target=xxx,args=(xxx,))     
- 启动多线程
> t.start()  
- 等待加入join的线程执行完成后，再执行接下来的线程。
> t.join()  
## 守护线程-daemon  
- 设置守护线程
> t1.setDaemon(True)
- 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
- 一般认为，守护线程不重要，或者不允许离开主线程独立运行
- 守护线程案例能否有效跟环境有关
## 线程常用属性
>- threading.currentThread  返回当前线程变量
>- threading.enumerate  返回一个包含正在运行的线程的list
>- threading.activeCount 返回正在运行的线程数量
>- thr.setName  给线程设置名字    t1.setName("name1")
>- thr.getName  得到线程的名字
## 直接继承自 threading.Thread 进行多线程操作
- 直接继承Thread
- 重写run函数
- 类实例可以直接运行
## 共享变量：当多个线程同时访问一个变量的时候，会产生共享变量的问题
- 锁（Lock） 可以理解成是一个令牌，只有拿到了令牌的线程才可以访问共享资源
    - 使用前需要先生成一个锁的实例
    > lock = threading.Lock()
    - 加锁 
    >lock.acquire()
    - 设置锁的超时时间
    >lock_1.acquire(timeout=4) 
    - 取消所，释放锁
    >lock.release()
    - 锁什么 哪个资源需要多个资源共享，锁哪个
    - 死锁问题
## 线程安全问题
    - 如果一个资源/变量，他对于多线程来讲，不用加锁也不会引起任何问题，则成为线程安全
    - 线程不安全变量类型： list set dict
    - 线程安全变量类型： queue
## 生产者消费者问题  消息队列 解决数据产生和消费不对等的问题
- 一个模型，可以用来搭建消息队列
- queue 是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
    > 用法  q =queue.Queue()     q.qsize()  
    > q.qsiae() 返回queue内容长度  
    > q.put()   向queue中放入一个值  
    > q.get()   从queue里面取一个值  
    > q.queue() 返回整个队列
- semphore 允许一个资源最多有几个线程同时使用
    > semaphore = threading.Semaphore(3)  申请  
    > semaphore.acquire()    加上上限的限制  
    > semaquire.release()    释放限制
- threading.Timer
    - 在启动后，6秒钟后再执行调用的函数
    > t = threading.Timer(6,func)  
    > t.start()
    - Timer是利用多线程，在指定时间后启动一个功能
- 可重入锁   lock = threading.RLock()
    - 一个锁，可以被一个线程多次申请
    - 主要解决递归调用的时候，需要申请锁的情况
# 线程替代方案
- subprocess
    - 完全逃过线程，使用进程
    - 是派生的主要替代方案
    - python2.4后引入
- multiprocessiong
    - 使用threading接口派生，使用子进程
    - 允许为多核或多cpu派生线程，接口跟threading非常相似
    - python2.6后引入
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2后引入
# 多进程
- 进程间通讯（InterprocessCommunication，IPC）
- 进程之间无任何共享状态
- 进程的创建
    - 直接生成Process实例对象
    - 派生子类
# 生产者消费者模型
- JoinableQueue
- 哨兵的使用
    - 在队列中先放入有效的数据，有效数据导入完成后，在队列的最后添加一个标记值，在消费者提取商品时，先判断一下是不是这个标记值，如果是，那么证明已经完成，break或其他处理即可。
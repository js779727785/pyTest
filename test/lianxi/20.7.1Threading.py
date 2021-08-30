# https://www.jianshu.com/p/87ddc009731d
import time,threading
"""
线程
from threading import Thread
t1=Thread(target=fun,args=xxx)
t1.start()
t1.getName()
"""
# import time,threading
# def foo(something):#定义每个线程要运行的函数
#     for i in range(3):
#         time.sleep(1)#休眠1s来模拟CPU处理很多事情
#         print('CPU正在执行:'+something)
# def bar(something):
#     for i in range(5):
#         time.sleep(1)
#         print('CPU正在执行:'+something)
# t1=threading.Thread(target=foo,args=['看电影'])#生成一个线程实例
# t2=threading.Thread(target=bar,args=['听音乐'])
# t1.start()#启动线程实例
# t2.start()
# #总共3个进程：一个主线程(该python文件)+2个子线程
# print(t1.getName())#获取线程名
# print(t2.getName())
# print(threading.main_thread().getName())
"""
阻塞线程join
主线程等待子线程结束后再运行
"""
# import time,threading
# def foo(something):#定义每个线程要运行的函数
#     for i in range(3):
#         time.sleep(1)#休眠1s来模拟CPU处理很多事情
#         print('CPU正在执行:'+something)
# def bar(something):
#     for i in range(5):
#         time.sleep(1)
#         print('CPU正在执行:'+something)
# t1=threading.Thread(target=foo,args=['看电影'])#生成一个线程实例
# t2=threading.Thread(target=bar,args=['听音乐'])
# t1.start()#启动线程实例
# t2.start()
# t1.join()#阻塞主线程,检查t1线程是否执行结束
# print(t1.getName())
# print(t2.getName())
"""
守护线程（setDaemon）
放在start()之前，
使用场景：主线程完成后,不管子线程是否完成都要和主线程一起退出
"""

# import time,threading
# def foo():
#     while True:
#         time.sleep(1)
#         print('听音乐')
# t1=threading.Thread(target=foo)
# t1.setDaemon(True)#守护线程:主线程结束子线程也结束
# t1.start()
# for i in  range(3):
#     time.sleep(1)
#     print('看电影')
# print('电影放映结束!')

#########################################################################################################
#########################################################################################################
#########################################################################################################
"""
https://www.jianshu.com/p/88828eba1cbf
1）多线程并发优点：在执行IO密集型任务时,某个任务阻塞的时候CPU会切换到其他任务就大大提高了CPU的使用效率。
2）多线程并发缺点：在执行计算密集型任务时,CPU一直在计算没有休息。因此python多线程并发并不能显著提高效率,但是使用多进程执行效率有所提升。
"""
"""
原始IO密集运算和多线程运行
"""
#原始IO密集运算较慢
# import time,threading
# begin_time=time.time()
# def foo(something):
#     print(something)
#     time.sleep(2)
# #串行执行IO型密集任务
# foo('磁盘接收100M数据')
# foo('CPU执行其他任务!')
# end_time=time.time()
# #打印主线程运行时间
# print('共计消耗时长为:',end_time-begin_time)#4s

#多线程并发执行IO型密集任务
# import time,threading
# begin_time=time.time()
# def foo(something):
#     print(something)
#     time.sleep(2)
# #串行执行IO型密集任务
# t1=threading.Thread(target=foo,args=['磁盘接收100M数据'])
# t2=threading.Thread(target=foo,args=['CPU执行其他任务!'])
# t1.start()
# t2.start()
# #必须用join，防止还线程还没运行完，主线程就算出时间
# t1.join()
# t2.join()
# end_time=time.time()
# #打印主线程运行时间
# print('共计消耗时长为:',end_time-begin_time)#2s

#多进程并发执行IO型密集任务
# import time
# from multiprocessing import Process
# begin_time=time.time()
# def foo(something):
#     print(something)
#     time.sleep(2)
# #多进程并发执行IO型密集任务
# if __name__ == '__main__':
#     t1=Process(target=foo,args=('磁盘接收100M数据',))
#     t2=Process(target=foo,args=('CPU执行其他任务!',))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end_time=time.time()
#     print('共计消耗时长为:',end_time-begin_time)#2.20212s
#
"""
线程安全问题1：没有加正当的互斥锁，导致计算错误，在多线程并发操作金额的交易中出现
互斥锁（Lock）Lock每次只能锁定一次,其余的锁请求,需等待锁释放后才能获取
r=threading.Lock()
上锁：r.acquire()
释放：r.release()
"""
# import time,threading
# account_balance=500
# r=threading.Lock()#一把锁
# def option_num(num):
#     global account_balance
#     r.acquire()#上锁
#     balance=account_balance
#     time.sleep(1)
#     balance+=num
#     account_balance=balance
#     r.release()#解锁
# t1=threading.Thread(target=option_num,args=(-300,))
# t2=threading.Thread(target=option_num,args=(10000,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('账户余额为:',account_balance)#10200
"""
线程安全问题2：死锁，两个锁互相依赖等待造成
递归锁（Reentrant Lock）
RLock 内部维护着一个 Lock 和一个 counter 变量,counter 记录了 acquire 的次数,从而使得资源可以被多次 acquire。直到一个线程所有的 acquire 都被 release,其他的线程才能获得资源。
r=threading.RLock()
r.acquire()
r.release()
"""

"""
互斥锁是简单的线程同步机制,对于复杂线程同步问题的支持，引入条件同步变量。
Condition除了能提供RLock()和Lock()的方法外,还提供了 wait()、notify()、notifyAll()方法
原理：线程首先acquire一个条件变量,然后判断一些条件。如果条件不满足则wait ; 如果条件满足,进行一些处理改变条件后通过notify方法通知其他线程 ; 其他处于wait状态线程接到通知后会重新判断条件
调用方式：cond =threading.Condition(Lock/RLock);不传默认RLock

例子：
早点铺的师傅必须蒸好包子,消费者才能把包子买来吃掉。即：
生产者可以不断生产商品直到仓库装满然后告知消费者消费;
消费者也可以判断仓库是否满从而告知生产者继续生产商品。
"""
# import threading,time,random
# lock_con=threading.Condition()#条件锁对象
# num_list=[]#创建一个空列表
# def producer():
#     global num_list#引用全局变量
#     while True:#模拟不停的生产包子
#         if lock_con.acquire():#上锁
#             num_list.append(1)
#             print('生产者:','生产了一个包子',num_list)
#             lock_con.notifyAll()#通知等待池激活所有线程
#             lock_con.release()#解锁
#             time.sleep(random.randint(0,10)*0.1)#模拟包子端上桌的时间
# def consumer():
#     global num_list
#     while True:#模拟不停的吃掉包子
#         if lock_con.acquire():#上锁
#             if len(num_list)==0:
#                 print('包子已卖完,请等待包子生产中!!!')
#                 lock_con.wait()#线程释放锁进入等待,被唤起重新加锁
#             num_list.remove(num_list[0])#去掉第一个元素
#             print('消费者:','吃掉了一个包子',num_list)
#             time.sleep(random.randint(0,10)*0.2)#模拟吃掉包子的时间
#             lock_con.notifyAll()
#             lock_con.release()#解锁
# t1=threading.Thread(target=producer)
# t2=threading.Thread(target=consumer)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
"""
信号量是用来控制线程并发数的。
threading.BoundedSemaphore/Semaphore(value);值默认1
BoundedSemaphore和Semaphore区别：前者将在调用release()时检查计数器的值是否超过了计数器的初始值,如果超过将抛出一个异常
"""
# import threading,time,random
# semaphore=threading.Semaphore(3)#同一时间只能有3个线程处于运行状态
# def run (ii):
#     semaphore.acquire() # 获得信号量:信号量减一
#     print(ii,'号车可以进入')
#     time.sleep(random.randint(0,10)*1)
#     print(ii,'号停车位释放')
#     semaphore.release()# 释放信号量:信号量加一
# for i in range(5):#创建5个线程
#     t=threading.Thread(target=run,args=(i,))
#     t.start()
"""
sys.argv
re=os.popen(cmd)
0==os.system(cmd)
"""
import  sys,os
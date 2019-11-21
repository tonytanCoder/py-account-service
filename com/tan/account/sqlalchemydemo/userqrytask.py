import time, threading
from userqry import UserQryService


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        userqryservice= UserQryService();
        users=userqryservice.qryAllUser();

        for i in range(len(users)):
            print('thread %s >>> %s' % (threading.current_thread().name,users[i].user_name))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
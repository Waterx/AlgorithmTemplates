import threading

class PrintNumberThread(threading.Thread):
    def __init__(self, number, lock, condition):
        threading.Thread.__init__(self)
        self.number = number
        self.lock = lock
        self.condition = condition

    def run(self):
        while self.number <= 10:
            with self.lock:
                print(self.number)
                self.number += 2
                self.condition.notify()  # 通知等待的线程
                if self.number <= 10:
                    self.condition.wait()  # 等待条件满足
                else:
                    self.condition.notify_all()  # 唤醒所有等待的线程

# 创建锁对象和条件变量
lock = threading.Lock()
condition = threading.Condition(lock)

# 创建两个线程，一个打印奇数，一个打印偶数
odd_thread = PrintNumberThread(1, lock, condition)
even_thread = PrintNumberThread(2, lock, condition)

# 启动线程
odd_thread.start()
even_thread.start()

# 等待两个线程结束
odd_thread.join()
even_thread.join()

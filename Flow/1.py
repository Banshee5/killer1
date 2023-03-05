import time
from threading import Thread


def napominalocha():
    message=input()
    sec=int(input())
    time.sleep(sec)
    print(message)

t1=Thread(target=napominalocha)
t1.start()
time.sleep(10)
print('Программа завершается')

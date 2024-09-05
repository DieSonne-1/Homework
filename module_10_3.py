import threading
from random import randint
from threading import Lock, Thread
from time import sleep


class Bank(Thread):
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            ran_num = randint(50, 500)
            self.balance += ran_num
            print(f'Пополнение: {ran_num}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            ran_numb = randint(50, 500)
            print(f'Запрос на {ran_numb}.')
            if ran_numb <= self.balance:
                self.balance -= ran_numb
                print(f'Снятие: {ran_numb}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
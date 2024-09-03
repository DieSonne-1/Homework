from threading import Thread
from time import sleep

class Knight(Thread):
  def __init__(self, name, power):
    super().__init__()
    self.name = name
    self.power = power
    self.enemies = 100

  def run(self):
    print(f'{self.name}, на нас напали!')
    days_fighting = 0
    while self.enemies > 0:
      self.enemies -= self.power
      days_fighting += 1
      print(f'{self.name} сражается {days_fighting}..., осталось {self.enemies} воинов.')
      sleep(1)
    print(f'{self.name} одержал победу спустя {days_fighting} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

threads = [first_knight, second_knight]
for knight in threads:
    knight.start()

for knight in threads:
    knight.join()

print("Все битвы закончились!")
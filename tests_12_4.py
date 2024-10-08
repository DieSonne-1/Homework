import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            a = Runner('Nick',-5)
            for walk in range(10):
                a.walk()
            self.assertEqual(a.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as ex:
            logging.warning("Неверная скорость для Runner", exe_info=ex)

    def test_run(self):
        try:
            b = Runner(2)
            for run in range(10):
                b.run()
            self.assertEqual(b.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as ex:
            logging.warning("Неверный тип данных для объекта Runner", exe_info=ex)

    def test_challenge(self):
        c = Runner('Leon')
        d = Runner('Dave')
        for run in range(10):
            d.run()
            c.walk()
        self.assertNotEqual(c.distance, d.distance)

if __name__ == "__main__":
    unittest.main()


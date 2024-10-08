import module_12_1 as md, module_12_2 as mod #Импортирую модули с предыдущими кодами по условиям задачи, в моём PyCharm
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        a = md.Runner('Nick')
        for walk in range(10):
            a.walk()
        self.assertEqual(a.distance, 50 )

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        b = md.Runner('Tom')
        for run in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        c = md.Runner('Leon')
        for walk in range(10):
            c.walk()
        d = md.Runner('Dave')
        for run in range(10):
            d.run()
        self.assertNotEqual(c.distance, d.distance)

if __name__ == "__main__":
    unittest.main()

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.first = mod.Runner('Усэйн', 10)
        self.second = mod.Runner('Андрей', 9)
        self.third = mod.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = mod.Tournament(90, self.first, self.third)
        result = tournament.start()
        self.all_results['1'] = result
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = mod.Tournament(90, self.second, self.third)
        result = tournament.start()
        self.all_results['2'] = result
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = mod.Tournament(90, self.first, self.second, self.third)
        result = tournament.start()
        self.all_results['3'] = result
        self.assertTrue(result[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')


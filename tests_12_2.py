import module_12_2 as md #Импортирую модуль в котором записан код из задачи в моём PyCharm
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = md.Runner('Усэйн', 10)
        self.second = md.Runner('Андрей', 9)
        self.third = md.Runner('Ник', 3)

    def test_first_tournament(self):
        tournament = md.Tournament(90, self.first, self.third)
        result = tournament.start()
        self.all_results['1'] = result
        self.assertTrue(result[2] == 'Ник')

    def test_second_tournament(self):
        tournament = md.Tournament(90, self.second, self.third)
        result = tournament.start()
        self.all_results['2'] = result
        self.assertTrue(result[2] == 'Ник')

    def test_third_tournament(self):
        tournament = md.Tournament(90, self.first, self.second, self.third)
        result = tournament.start()
        self.all_results['3'] = result
        self.assertTrue(result[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for k,v in cls.all_results.items():
            print(f'{k}:{v}')




import module_12_1 as md
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = md.Runner('Nick')
        for walk in range(10):
            a.walk()
        self.assertEqual(a.distance, 50 )
    def test_run(self):
        b = md.Runner('Tom')
        for run in range(10):
            b.run()
        self.assertEqual(b.distance, 100)
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
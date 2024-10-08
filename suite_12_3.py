import unittest
import tests_12_3

suit_TS = unittest.TestSuite()
suit_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suit_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suit_TS)


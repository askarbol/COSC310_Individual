import unittest
from Interface import phraseinput as pi
from Interface import reponse as res


class TestSum(unittest.TestCase):
    
    def testStem(self):
        self.assertEqual(pi.psStem("Marcus decided he wasn\'t going to come"), "marcu decid he wasn't go to come " , "Expected: marcu decid he wasn\'t go to come")

    def testPOS(self):
        self.assertEqual(pi.getPOS("Marcus"), 'NN', "Expected: NN")

    def testName(self):
        self.assertEqual(pi.interpolate(2, "Marcus"), "1Robert: Marcus? That's a good name!\n" , "Expected: 1Robert: Marcus? That's a good name!\n")


if __name__ == '__main__':
    unittest.main()
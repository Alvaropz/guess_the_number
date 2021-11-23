import unittest
import random
import re
from guess_the_number import Find

class TestCases(unittest.TestCase):
    def test_game_auto(self):
        name = random.choice(["Mike", "Alice", "Lucio", "James", "Sarah", "Becca", "Derek", "Tom", "Matt", "Mariam"])
        test = True
        g = Find(name=name, test=test)
        g.guess_the_number()
        self.assertEqual(g.i_number, g.r_number)

    def test_game_writing_names_scores(self):
        name = random.choice(["Mike", "Alice", "Lucio", "James", "Sarah", "Becca", "Derek", "Tom", "Matt", "Mariam"])
        test = True
        g = Find(name=name, test=test)
        g.guess_the_number()
        with open("scores.txt", "r") as myfile:
            lines = myfile.readlines()
            last_name = re.findall(r"(.*?)\:", lines[-1:][0])[0]
            last_score = re.findall(r"[0-9]+", lines[-1:][0])[0]
        self.assertEqual(g.player_name, last_name)
        self.assertEqual(g.score, int(last_score))

    def test_game_op_test(self):
        name = random.choice(["Mike", "Alice", "Lucio", "James", "Sarah", "Becca", "Derek", "Tom", "Matt", "Mariam"])
        g = Find(name=name)
        g.guess_the_number()
        self.assertEqual(g.i_number, g.r_number)

    def test_game_op_name(self):
        test = True
        g = Find(test=test)
        g.guess_the_number()
        self.assertEqual(g.i_number, g.r_number)

if __name__ == "__main__":
    unittest.main(verbosity=2)
import unittest
import part1

class TestDay11(unittest.TestCase):

  def test(self):
    self.assertEqual(part1.get_location("ne,ne,ne"), (6, 3))
    self.assertEqual(part1.get_location("ne,ne,sw,sw"), (0, 0))
    self.assertEqual(part1.get_location("ne,ne,s,s"), (4, -2))
    self.assertEqual(part1.get_location("se,sw,se,sw,sw"), (-2, -5))

    self.assertEqual(part1.get_answer("ne,ne,ne"), 3)
    self.assertEqual(part1.get_answer("ne,ne,sw,sw"), 0)
    self.assertEqual(part1.get_answer("ne,ne,s,s"), 2)
    self.assertEqual(part1.get_answer("se,sw,se,sw,sw"), 3)
    
    


if __name__ == '__main__':
    unittest.main()

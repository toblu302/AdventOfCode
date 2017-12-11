import unittest
import part1
import part2

class TestDay5(unittest.TestCase):

  def test_jumps(self):
    self.assertEqual(part1.get_answer([0, 3, 0, 1, -3]), 5)
    self.assertEqual(part1.get_answer([0]), 2)
    self.assertEqual(part2.get_answer([0, 3, 0, 1, -3]), 10)

if __name__ == '__main__':
    unittest.main()

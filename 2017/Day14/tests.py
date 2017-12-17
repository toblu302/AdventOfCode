import unittest
import part1
import part2

class TestDay14(unittest.TestCase):

  def test_part1(self):
    self.assertEqual(part1.get_answer("flqrgnkx"), 8108)

  def test_part2(self):
    self.assertEqual(part2.get_answer("flqrgnkx"), 1242)


if __name__ == '__main__':
    unittest.main()

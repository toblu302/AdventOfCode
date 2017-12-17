import unittest
import part1
import part2

class TestDay13(unittest.TestCase):

  def test_part1(self):
    data=["0: 3",
          "1: 2",
          "4: 4",
          "6: 4"]

    self.assertEqual(part1.get_answer(data), 24)

  def test_part2(self):
    data=["0: 3",
          "1: 2",
          "4: 4",
          "6: 4"]

    self.assertEqual(part2.get_answer(data), 10)

if __name__ == '__main__':
    unittest.main()

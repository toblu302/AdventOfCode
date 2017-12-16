import unittest
import part1
import part2

class TestDay10(unittest.TestCase):

  def test(self):
    self.assertEqual(part1.get_answer([3, 4, 1, 5], 5), 12)

  def test_part_2(self):
    self.assertEqual(part2.get_list("1,2,3"), [49,44,50,44,51,17,31,73,47,23])

    self.assertEqual(part2.get_answer("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
    self.assertEqual(part2.get_answer("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")
    self.assertEqual(part2.get_answer("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
    self.assertEqual(part2.get_answer(""), "a2582a3a0e66e6e86e3812dcb672a272")
    
    


if __name__ == '__main__':
    unittest.main()

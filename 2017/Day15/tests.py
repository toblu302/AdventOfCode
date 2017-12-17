import unittest
import part1
import part2

class TestDay15(unittest.TestCase):

  def test_part1(self):
    self.assertEqual(part1.lowest_16_bits_are_equal(245556042, 1431495498), True)
    self.assertEqual(part1.lowest_16_bits_are_equal(1092455, 430625591), False)
    self.assertEqual(part1.get_answer(65, 8921), 588)

  def test_part2(self):
    self.assertEqual(part2.get_answer(65, 8921), 309)


if __name__ == '__main__':
    unittest.main()

import unittest
import part1
import part2

class TestDay6(unittest.TestCase):

  def test_part1(self):
    self.assertEqual(part1.perform_redistribution([0,2,7,0]), [2,4,1,2])
    self.assertEqual(part1.perform_redistribution([2,4,1,2]), [3,1,2,3])
    self.assertEqual(part1.perform_redistribution([3,1,2,3]), [0,2,3,4])
    self.assertEqual(part1.perform_redistribution([0,2,3,4]), [1,3,4,1])
    self.assertEqual(part1.perform_redistribution([1,3,4,1]), [2,4,1,2])

    self.assertEqual(part1.get_answer([0,2,7,0]), 5)
    self.assertEqual(part1.get_answer([1,3,4,1]), 4)

  def test_part2(self):
    a = [0,2,7,0]
    part2.perform_redistribution(a)
    self.assertEqual(a, [2,4,1,2])

    self.assertEqual(part2.get_answer([0,2,7,0]), 4)


if __name__ == '__main__':
    unittest.main()

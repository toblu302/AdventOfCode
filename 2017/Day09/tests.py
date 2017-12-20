import unittest
import part1
import part2

class TestDay9(unittest.TestCase):

  def test(self):
    self.assertEqual(part1.get_answer("{}"), 1)
    self.assertEqual(part1.get_answer("{{{}}}"), 6)
    self.assertEqual(part1.get_answer("{{{},{},{{}}}}"), 16)
    self.assertEqual(part1.get_answer("{<a>,<a>,<a>,<a>}"), 1)
    self.assertEqual(part1.get_answer("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
    self.assertEqual(part1.get_answer("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
    self.assertEqual(part1.get_answer("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)
    self.assertEqual(part1.get_answer("{{<a!>},{<a!>},{<a!>},{<ab>}}{{<a!>},{<a!>},{<a!>},{<ab>}}"), 6)
    self.assertEqual(part1.get_answer("{{<!>},{<!>},{<!>},{<a>}}"), 3)

    self.assertEqual(part2.get_answer("<>"), 0)
    self.assertEqual(part2.get_answer("<random characters>"), 17)
    self.assertEqual(part2.get_answer("<<<<>"), 3)
    self.assertEqual(part2.get_answer("<{!>}>"), 2)
    self.assertEqual(part2.get_answer("<!!>"), 0)
    self.assertEqual(part2.get_answer("<!!!>>"), 0)
    self.assertEqual(part2.get_answer("<{o\"i!a,<{i<a>"), 10)
    self.assertEqual(part2.get_answer("{{<a>},{<a>},{<a>},{<a>}}"), 4)




if __name__ == '__main__':
    unittest.main()

import unittest
import part1

class TestDay16(unittest.TestCase):

  def test_part1(self):
    self.assertEqual(part1.do_move(['a','b','c','d','e'], "s3"), ['c','d','e','a','b'])
    self.assertEqual(part1.do_move(['a','b','c','d','e'], "s1"), ['e','a','b','c','d'])
    self.assertEqual(part1.do_move(['e','a','b','c','d'], "x3/4"), ['e','a','b','d','c'])
    self.assertEqual(part1.do_move(['e','a','b','d','c'], "pe/b"), ['b','a','e','d','c'])
    self.assertEqual(part1.get_answer(['s1', 'x3/4', 'pe/b'], "abcde"), 'baedc' )


if __name__ == '__main__':
    unittest.main()

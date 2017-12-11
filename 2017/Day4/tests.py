import unittest
import part2

class TestPasswordMethods(unittest.TestCase):

  def test_passwords(self):
    self.assertEqual(part2.is_valid("abcde fghij"), True)
    self.assertEqual(part2.is_valid("abcde xyz ecdab"), False)
    self.assertEqual(part2.is_valid("a ab abc abd abf abj"), True)
    self.assertEqual(part2.is_valid("iiii oiii ooii oooi oooo"), True)
    self.assertEqual(part2.is_valid("oiii ioii iioi iiio"), False)

if __name__ == '__main__':
    unittest.main()

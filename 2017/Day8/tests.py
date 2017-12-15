import unittest
import part1
import part2

class TestDay8(unittest.TestCase):

  def test(self):
    self.assertEqual(part1.get_register("js inc 257 if wn < 9"), "js")
    self.assertEqual(part1.get_sign("js inc 257 if wn < 9"), 1)
    self.assertEqual(part1.get_sign("js dec 257 if wn < 9"), -1)
    self.assertEqual(part1.get_value("js dec 257 if wn < 9"), 257)
    self.assertEqual(part1.get_conditional_register("js dec 257 if wn < 9"), "wn")
    self.assertEqual(part1.get_conditional("js dec 257 if wn < 9"), "< 9")

    in_data =["b inc 5 if a > 1",
              "a inc 1 if b < 5",
              "c dec -10 if a >= 1",
              "c inc -20 if c == 10"]
    self.assertEqual(part1.get_answer(in_data), 1)
    self.assertEqual(part2.get_answer(in_data), 10)

if __name__ == '__main__':
    unittest.main()

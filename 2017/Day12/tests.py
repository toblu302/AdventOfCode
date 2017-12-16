import unittest
import part1
import part2

class TestDay12(unittest.TestCase):

  def test_part1(self):
    data=["0 <-> 2",
          "1 <-> 1",
          "2 <-> 0, 3, 4",
          "3 <-> 2, 4",
          "4 <-> 2, 3, 6",
          "5 <-> 6",
          "6 <-> 4, 5"]

    graph = part1.get_graph(data)

    self.assertEqual(part1.get_answer(data), 6)
    self.assertEqual(len(part1.get_reachable_from(graph, '1')), 1)

  def test_part2(self):
      data=["0 <-> 2",
            "1 <-> 1",
            "2 <-> 0, 3, 4",
            "3 <-> 2, 4",
            "4 <-> 2, 3, 6",
            "5 <-> 6",
            "6 <-> 4, 5"]

      self.assertEqual(part2.get_answer(data), 2)


if __name__ == '__main__':
    unittest.main()

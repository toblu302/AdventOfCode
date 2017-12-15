import unittest
import part1

class TestDay7(unittest.TestCase):

  def test_line_splits(self):
    self.assertEqual(part1.get_parent("qhvca (428) -> odttvb, ymehff, ymyzbqc, jtdtmsi, wciuyuh"), "qhvca")
    self.assertEqual(part1.get_children("nwtkz (304) -> eykks, rxivjye"), ["eykks", "rxivjye"])
    self.assertEqual(part1.get_children("nwtkz (304)"), [])

  def test_index(self):
    indices = part1.get_node_indices(["a (1) -> b", "b (2) -> c", "c (3)"])
    self.assertEqual( indices['a'], 0 ) 
    self.assertEqual( indices['b'], 1 ) 
    self.assertEqual( indices['c'], 2 ) 
    indices = part1.get_node_indices(["b (2) -> c", "c (3)", "a (1) -> b"])
    self.assertEqual( indices['b'], 0 ) 
    self.assertEqual( indices['c'], 1 ) 
    self.assertEqual( indices['a'], 2 ) 

    self.assertEqual( part1.get_index_name(indices, 1), 'c' )

  def test_adj_matrix_part1(self):
    matrix = part1.get_adj_matrix(["a (1) -> b, d", "b (2) -> c", "c (3)", "d (4)"])
    self.assertEqual( matrix[0], [1,1,0,1] ) 
    self.assertEqual( matrix[1], [0,1,1,0] ) 
    self.assertEqual( matrix[2], [0,0,1,0] ) 
    self.assertEqual( matrix[3], [0,0,0,1] ) 


  def test_get_answer_part1(self):
    data=["pbga (66)",
          "xhth (57)",
          "ebii (61)",
          "havc (66)",
          "ktlj (57)",
          "fwft (72) -> ktlj, cntj, xhth",
          "qoyq (66)",
          "padx (45) -> pbga, havc, qoyq",
          "tknk (41) -> ugml, padx, fwft",
          "jptl (61)",
          "ugml (68) -> gyxo, ebii, jptl",
          "gyxo (61)",
          "cntj (57)"]

    self.assertEqual( part1.get_answer(data), "tknk" )


if __name__ == '__main__':
    unittest.main()

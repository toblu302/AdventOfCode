import unittest
import part1

class TestDay21(unittest.TestCase):

  def test(self):
    self.assertEqual(part1.get_tuple(".#/.#"), ((".","#"),(".","#")) )
    self.assertEqual(part1.get_tuple("../.#"), ((".","."),(".","#")) )
    self.assertEqual(part1.get_tuple("..#/.#./###"), ((".",".","#"),(".","#","."),("#","#","#")) )

    self.assertEqual(part1.get_flipped_h(((".","."),(".","#"))), ((".","."),("#",".")) )
    self.assertEqual(part1.get_flipped_h( ((".",".","#"),(".","#","."),("#","#",".")) ), (("#",".","."),(".","#","."),(".","#","#")) )

    self.assertEqual(part1.get_flipped_v(((".","."),(".","#"))), ((".","#"),(".",".")) )
    self.assertEqual(part1.get_flipped_v( ((".",".","#"),(".","#","."),("#","#",".")) ), (("#","#","."),(".","#","."),(".",".","#")) )

    self.assertEqual(part1.get_rotated(((".","#"),(".","#"))), ((".","."),("#","#")) )
    self.assertEqual(part1.get_rotated( ((".",".","#"),(".","#","."),("#","#",".")) ), (("#",".","."),("#","#","."),(".",".","#")) )
    self.assertEqual(part1.get_rotated( ((".","#","#"),(".","#","."),("#","#",".")) ), (("#",".","."),("#","#","#"),(".",".","#")) )

    self.assertEqual(list(part1.get_all_lhs(((".","."),(".",".")))), [((".","."),(".","."))] )
    self.assertEqual(part1.get_all_lhs(((".","#"),(".","."))), set([((".","#"),(".",".")), ((".","."),(".","#")), ((".","."),("#",".")), (("#","."),(".","."))]) )
    
    


if __name__ == '__main__':
    unittest.main()

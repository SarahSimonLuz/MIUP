import unittest
from RockMeNot import possivel
from RockMeNot import count
from RockMeNot import rock
from RockMeNot import matriz

class Testrock(unittest.TestCase):
        
        def test_rock(self):
                self.assertEqual(rock('teste1.txt'),True)
                self.assertEqual(rock('teste2.txt'),True)

        def test_possivel(self):
                self.assertEqual(possivel((['.','.','.'],['.','.','.'],['.','.','.']),1,1,2,2),True)
                self.assertEqual(possivel((['.','.'],['#','#']),0,0,1,1),False)

        def test_count(self):
                self.assertEqual(count((['.','.','.'],['.','.','.'],['.','.','.']),3,3),5)
                self.assertEqual(count((['.','.'],['.','#']),2,2),1)

        def test_matriz(self):
                self.assertEqual(matriz(['3 3\n', '...\n', '...\n', '...']),([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']], 3, 3))

if __name__=='__main__':
        unittest.main()






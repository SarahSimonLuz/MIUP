import unittest
import StringIO
import sys
#from eccentrics import criar_camadas
#from eccentrics import print_camadas
from eccentrics import mover_bolas

class ElectionTests(unittest.TestCase):
'''
	def criar_camadas(self):
		n_camadas = 3
		max_linhas = 6

		self.assertEqual(criar_camadas(n_camadas, max_linhas), ([[9, -1, -1, -1, -1, -1],
				   [1, -1, -1, -1, -1, -1],
				   [8, 7, -1, -1, -1, -1],
				   [5, -1, -1, -1, -1, -1],
				   [2, 3, -1, -1, -1, -1],
				   [4, 10, 11, -1, -1, -1]],10))

	def test_print_camadas(self):
		max_linhas = 6
		camadas = [[9, -1, -1, -1, -1, -1],
				   [1, -1, -1, -1, -1, -1],
				   [8, 7, -1, -1, -1, -1],
				   [5, -1, -1, -1, -1, -1],
				   [2, 3, -1, -1, -1, -1],
				   [4, 10, 11, -1, -1, -1]]

		capturedOutput = StringIO.StringIO()
		sys.stdout = capturedOutput
		print_camadas(camadas, max_linhas)
		sys.stdout=sys.__stdout__
		print(capturedOutput.getvalue())
'''
	def test_mover_bolas(self):
		n_camadas = 3
		max_linhas = 6
		camadas = [[9, -1, -1, -1, -1, -1],
				   [1, -1, -1, -1, -1, -1],
				   [8, 7, -1, -1, -1, -1],
				   [5, -1, -1, -1, -1, -1],
				   [2, 3, -1, -1, -1, -1],
				   [4, 10, 11, -1, -1, -1]]
		l = 0
		c = 0
		primeiro = 0

		rslt_mover_bolas = mover_bolas(camadas, max_linhas, n_camadas, l, c, primeiro)
		self.assertEqual(None, rslt_mover_bolas)

if __name__=='__main__':
        unittest.main()

		



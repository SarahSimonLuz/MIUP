#Teste para The Modern Feud of the Capulets and Montagues

import unittest
from main import main1 
class TesteUm(unittest.TestCase):
	
	def selfUp(self):
		pass

	def testeum(self):
	
		self.assertEqual(main1("input.txt"), 2)

if __name__=="__main__":
	unittest.main()
import unittest
from code import * 

class Advent2a(unittest.TestCase):

	def testFirstCase(self):
		self.assertEqual(checksum('1'), 12)

if __name__ == '__main__':
    unittest.main()
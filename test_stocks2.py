#test_stocks2.py

import unittest
from stocks1 import Stocks

class StocksTest(unittest.TestCase):
	def test_buy_one_company(self):
		stks = Stocks()
		stks.buy('Hon', 100, 132.0)
		self.assertEqual(stks.cost_basis(), 13200.0)

if __name__ == '__main__':
        unittest.main()
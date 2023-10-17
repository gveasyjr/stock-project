import unittest
from stocks1 import Stocks

class StocksTest(unittest.TestCase):
    def test_buy_one_company(self):
        stks = Stocks()
        stks.buy('Hon', 100, 132.0)
        self.assertEqual(stks.cost_basis(), 13200.0)
        
    def test_sell_small(self):
        stks = Stocks()
        stks.buy("CompanyA", 100, 50)
        stks.buy("CompanyB", 200, 30)
        stks.sell("CompanyA", 5)
        self.assertEqual(stks.stocks, [['CompanyA', 95, 50], ['CompanyB', 200, 30]])
        
    def test_sell_big(self):
        stks = Stocks()
        stks.buy("CompanyX", 1000, 200)
        stks.sell("CompanyX", 800) 
        self.assertEqual(stks.stocks, [['CompanyX', 200, 200]])
    
    def test_sell_float(self):
        stks = Stocks()
        stks.buy("CompanyY", 500, 55.5)
        stks.sell("CompanyY", 100.5)
        self.assertEqual(stks.stocks, [['CompanyY', 399.5, 55.5]])


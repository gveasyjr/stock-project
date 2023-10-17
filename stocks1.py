# stocks1.py is a simple application to motivate unit testing.
# stock trading application has an in mem rep of stocks acquired
# represented as a list of lists where each element is a purchased stock

class Stocks(object):
    """An in mem stock portfolio"""

    def __init__(self):
        # stocks is a list of lists where each element
        # is a list of company name, num shares purchased
        # and the price per share
        self.stocks = []

    def buy(self, company, num_shares, unit_price):
        """Buy `num_shares` in 'company' at `unit_price` per share"""
        self.stocks.append([company, num_shares, unit_price])

    def cost_basis(self):
        """Calculate the cost basis for the stocks acquired"""
        basis = 0.0
        for company, shares, unit_price in self.stocks:
            basis += shares * unit_price
        return basis

    def cost_basis_company(self, company):
        pass

    def sell(self, company, num_shares):
        pass

    def print_portfolio(self):
        print('Company,', 'Number Shares,', 'Share Price')
        for company, num_shares, unit_price in self.stocks:
            print(company, num_shares, unit_price)
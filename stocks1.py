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
        """
        >>> stocks = Stocks()
        >>> stocks.buy("CompanyA", 150, 55)  # Buying 150 shares of CompanyA at $55 per share
        >>> stocks.buy("CompanyB", 250, 40)  # Buying 250 shares of CompanyB at $40 per share

        >>> stocks.sell("CompanyA", 50)  # Selling 50 shares of CompanyA
        Sold 50 shares of CompanyA at $55 per share.
        >>> stocks.stocks
        [['CompanyA', 100, 55], ['CompanyB', 250, 40]]

        >>> stocks.sell("CompanyB", 150)  # Selling 150 shares of CompanyB
        Sold 150 shares of CompanyB at $40 per share.
        >>> stocks.stocks
        [['CompanyA', 100, 55], ['CompanyB', 100, 40]]

        >>> stocks.sell("CompanyA", 70)  # Selling 70 shares of CompanyA
        Sold 70 shares of CompanyA at $55 per share.
        >>> stocks.stocks
        [['CompanyA', 30, 55], ['CompanyB', 100, 40]]
        """
        for stock in self.stocks:
            if stock[0] == company:
                # If there are enough shares to sell, update the shares count
                if stock[1] >= num_shares:
                    stock[1] -= num_shares
                    print(f"Sold {num_shares} shares of {company} at ${stock[2]} per share.")
                else:
                    print(f"Error: Not enough shares of {company} to sell.")
                    # Optionally, you can raise an exception here
                break
        else:
            print(f"Error: {company} not found in the portfolio.")


    def print_portfolio(self):
        print('Company,', 'Number Shares,', 'Share Price')
        for company, num_shares, unit_price in self.stocks:
            print(company, num_shares, unit_price)
        return
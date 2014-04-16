from fin.bond.flattermstructure.bondpricing import BondPricing

'''A 3 year bond with a face value of $100 makes annual coupon payments of 10%. The current interest rate
(with annual compounding) is 9%.'''

cashflows = [(1,10),(2,10),(3,110)]
'''note the first cashflow is at time 1 and not zero'''

price = BondPricing().bond_price_discrete(0.09, cashflows)
print price

ytm = BondPricing().bond_yield_to_maturity_discrete(cashflows, price)
print ytm

duration = BondPricing().bond_duration_discrete(cashflows, 0.09)
print duration


import fin.timevalueofmoney.presentvalue
from fin.timevalueofmoney.irr_bisection import IRRBiSection
from fin.timevalueofmoney.irr_newton import IRRNewton

cashflows = [(0,-100),(1,75),(2,75)]
pv = fin.timevalueofmoney.presentvalue.PresentValue(0.1,cashflows)
print pv.discretepv()

'''
Nominal Price 100.0. Market Price 104.5. Interest Paid every six months (twice yearly).
Term to redemption 3 years(n)Coupon rate 10% Per annum. The initial estimates
for yield are Low=3%. High=7%.
'''

irrbisection = IRRBiSection(iterations=30, precision=1e-3, lower=0.03, higher=0.07)
print irrbisection.ytm(nominal=100.0, term=2.0, coupon=10, mkt_price=104.5, period=3)

irrnewton = IRRNewton(iterations=30, precision=1e-6, lower=0.05)
print irrnewton.ytm(nominal=100.0, term=2.0, coupon=10, mkt_price=104.5, period=3)

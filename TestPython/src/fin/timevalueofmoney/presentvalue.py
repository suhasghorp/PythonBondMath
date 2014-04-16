'''
Created on Apr 14, 2014

@author: sghorp
'''

class PresentValue(object):
    
    def __init__(self, rate, cashflows):
        
        self.rate = rate
        self.cashflows = cashflows
        
    def discretepv(self):
        pv = 0
        for (t, c) in self.cashflows:
            pv += c/pow(1 + self.rate, t)
        return pv
        
        
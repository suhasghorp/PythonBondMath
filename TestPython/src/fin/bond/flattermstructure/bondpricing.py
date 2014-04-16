'''
Created on Apr 16, 2014

@author: sghorp
'''
from math import fabs

class BondPricing(object):
    
    def __init__(self):
       '''Not sure'''
         
    def bond_price_discrete(self, rate, cashflows):
        pv = 0
        for (t, c) in cashflows:
            pv += c/pow((1 + rate), t)
            
        return pv
        
    def bond_yield_to_maturity_discrete(self, cashflows, bondprice):
        accuracy = 1e-5
        iterations = 200
        lower = 0; higher = 1
        while (self.bond_price_discrete(higher, cashflows) > bondprice):
            higher = higher * 2
           
        r = 0.5 * (higher + lower)
        for i in range(iterations):
            diff = self.bond_price_discrete(r, cashflows) - bondprice
            if (fabs(diff) < accuracy):
                return r
            if (diff > 0):
                lower = r
            else:
                higher = r
            r = 0.5 * (higher + lower)
            
        return r
    
    def bond_duration_discrete(self, cashflows,rate):
        D = 0; B = 0
        for (t, c) in cashflows:
            D += (t * c)/pow(1 + rate, t)
            B += c / pow(1 + rate, t)
        return D/B
            
            
             
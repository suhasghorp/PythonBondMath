'''
Created on Apr 16, 2014

@author: sghorp
'''

from fin.basemath.BaseNewtonRaphson import BaseNewtonRaphson

class IRRNewton(object):
    
    def __init__(self, iterations, precision, lower):
        self.iterations = iterations
        self.precision = precision
        self.lower = lower
                
        '''create new instance of BaseNewtonRaphson passing this object as an argument so that BaseNewtonRaphson can later call
        compute_function of this class'''
        
        self.newtonraphson = BaseNewtonRaphson(self)
        self.newtonraphson.precision = self.precision
        self.newtonraphson.iterations = self.iterations
        
    def newtonroot(self, rootvalue):
        solution =  (self.rate_per_term/rootvalue * (1.0-1.0/(pow(1.0 + rootvalue , self.rate_index))))+(self.nominal / (pow(1.0+ rootvalue, self.rate_index))) - self.mkt_price
        return solution

        
        
    def ytm(self, nominal, term, coupon, mkt_price, period):
        self.rate_per_term = coupon/term
        self.rate_index = period * term
        self.nominal = nominal;
        self.mkt_price = mkt_price
        return self.newtonraphson.newtraph(self.lower)
    
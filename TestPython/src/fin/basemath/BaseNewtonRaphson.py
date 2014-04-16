'''
Created on Apr 15, 2014

@author: sghorp
'''
from fin.basemath.BaseDerivative import BaseDerivative
from math import fabs

class BaseNewtonRaphson(object):
    
    
    def __init__(self, caller):
        self.derivative = BaseDerivative(self);
        self.caller = caller
        self.precision = 0 
        self.iterations = 0
        self.counter = 0
    
    def newtraph(self, lowerbound):        
        self.derivative.h = self.precision
        fx = self.caller.newtonroot(lowerbound)
        Fx = self.derivative.derivation(lowerbound)
        x = (lowerbound - (fx/Fx))
        while(fabs(fabs(x) - fabs(lowerbound)) > self.precision and self.counter < self.iterations):
            lowerbound = x
            self.counter = self.counter + 1     
            self.newtraph(lowerbound)                   
        return x
        
    
    def derive_function(self,inputa): 
        x1 = self.caller.newtonroot(inputa)
        return x1  
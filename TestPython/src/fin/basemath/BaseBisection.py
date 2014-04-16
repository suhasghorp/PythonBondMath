'''
Created on Apr 16, 2014

@author: sghorp
'''

from math import fabs
 
class BaseBisection(object):
     
    def __init__(self, caller):
        self.caller = caller
                
    def evaluate_root(self, lower, higher, iterations, precision):
        midvalue = 0
        fa = self.caller.compute_function(lower)
        fb = self.caller.compute_function(higher)
        if (fa * fb > 0):
            midvalue = 0
        else:
            condition = True
            while condition:
                precvalue = midvalue;
                midvalue=lower+0.5*(higher-lower);
                fc=self.caller.compute_function(midvalue);
                if(fa * fc < 0):
                    higher = midvalue;
                elif (fa * fc > 0):
                    lower = midvalue
                condition = fabs(fc) > precision and 1.0 < float(iterations)
                
        return midvalue
            
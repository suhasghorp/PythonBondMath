'''
Created on Apr 15, 2014

@author: sghorp
'''

class BaseDerivative(object):
    
    def __init__(self, caller):
        self.caller = caller
        self.h = 0
        
    def derivation(self, input_func): 
        x2 = self.caller.derive_function(input_func - self.h)
        x1 = self.caller.derive_function(input_func + self.h) 
        value = (x1-x2)/(2*self.h)
        return value
     
        
from abc import ABC as abstract, abstractmenthod
from numpy import random as rm, size

class Distribution:
    def __init__(self):
        pass

    @staticmethod
    def spit(self):
        pass

class Exponential(Distribution):
    def __init__(self,size):
        self.Model = rm.exponential(size)
    
    def spit(self):
        self.Model()
class Pareto(Distribution):
    def __init__(self,param,size):
        self.Model = rm.pareto(param,size)
    
exp = Exponential()
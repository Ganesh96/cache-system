from abc import ABC as abstract, abstractmethod
from ctypes.wintypes import SIZE
from numpy import random as rm, size

# ExponentialDistribution = None
# ParetoDistribution = None
class Distribution(abstract):
    def __init__(self):
        pass

    @abstractmethod
    def spit(self):
        pass

class Exponential(Distribution):
    def __init__(self,size):
        self.Model = rm.exponential(size)
    
    def spit(self):
        return 0    #self.Model
class Pareto(Distribution):
    def __init__(self,param,size):
        self.Model = rm.pareto(param,size)
    
    def spit(self):
        return 0    #self.Model

def Get_Distribution(distributionType,map):
    if "size" in map.keys():
        SIZE = map["size"]
    if "alpha" in map.keys():
        ALPHA = map["alpha"]
    if distributionType == "exponentialDistribution":
        ExponentialDistribution =1
        return Exponential(SIZE)
    if distributionType == "paretoDistribution":
        return Pareto(ALPHA,SIZE)
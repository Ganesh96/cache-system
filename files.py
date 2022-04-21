# Dependencies
from numpy.random import pareto
from numpy import sum

class Files:
    def __init__(self):
        self.size = pareto(2,1000)
        self.probability = pareto(1,1000)
        self.probability = self.probability/sum(self.probability)
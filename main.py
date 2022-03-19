# @Author: Ganesan Santhanam
# @Name: Cache System
# @Code Birth: March 18th 

from time import time
from file import File
from distribution import Get_Distribution

GlobalTime = time()
FilesDB = list()

def Generate(BigN):
    for i in range(1,BigN+1):
        FilesDB.append(File(i))

if __name__ == "__main__":
    # Create files for the server to access
    Generate(10000)

    #Create lamba using the paretoDistribution
    requestNumber = Get_Distribution("paretoDistribution",{"size":1000,"alpha":10}).spit()


from distribution import Get_Distribution

class File:
    def __init__(self,fileID) -> None:
        self.ID = fileID
        self.Model = Get_Distribution("paretoDistribution",{"size":1024,"alpha":5})
        self.Size = self.RunModel()
    
    def RunModel(self):
        return 0    #self.Model
    
    def GetResponseTime(self):
        return 0    #generate the response time
    

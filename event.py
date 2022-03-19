from abc import ABC as abstract, abstractmenthod
from distribution import exp
import constants

class EventChange():
    pass

class Event(abstract):
    def __init__(self, fileID,eventtime):
        self.FileID = fileID
        self.EventTime = eventtime
        self.Status = constants.New

    @abstractmenthod
    def process(self):
        pass

class NewRequestEvent(Event):
    def __init__(self, fileID,eventtime):
        super().__init__(fileID,eventtime)
        self.existsCache = False
    
    def process(self):
        self.EventTime+= 

#######################
class RequestEvent(Event):
    def __init__(self, fileID,executeTime):
        super().__init__(fileID,executeTime)
    
    def details(self):
        print(self.FileID,self.ExecuteTime,self.Status)
    
    def process(self):
        self.ExecuteTime += 

class ResponseEvent(Event):
    def __init__(self, fileID, executeTime):
        super().__init__(fileID, executeTime)
    
    def process(self):


r= RequestEvent(1,1)
r.details
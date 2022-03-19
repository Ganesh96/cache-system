from abc import ABC as abstract, abstractmethod
from distribution import Get_Distribution
from file import File
import constants

class EventChange():
    pass

class Event(abstract):
    def __init__(self, fileID,eventtime):
        self.File = File()
        self.EventTime = eventtime
        #self.Status = constants.New

    @abstractmethod
    def process(self):
        pass

class RequestEvent(Event):
    def __init__(self, fileID,eventtime):
        super().__init__(fileID,eventtime)
        self.existsCache = False
    
    def process(self):
        if self.existsCache:
            self.EventTime+= self.File.GetResponseTime()

class FileReceivedEvent(Event):
    def __init__(self, fileID,eventtime):
        super().__init__(fileID,eventtime)
        self.existsCache = False
    
    def process(self):
        if self.existsCache:
            self.EventTime+= self.File.GetResponseTime()

class ArriveAtQueueEvent(Event):
    def __init__(self, fileID,eventtime):
        super().__init__(fileID,eventtime)
        self.existsCache = False
    
    def process(self):
        if self.existsCache:
            self.EventTime+= self.File.GetResponseTime()

class DepartQueueEvent(Event):
    def __init__(self, fileID,eventtime):
        super().__init__(fileID,eventtime)
        self.existsCache = False
    
    def process(self):
        if self.existsCache:
            self.EventTime+= self.File.GetResponseTime()


# My Legacy Code

# class RequestEvent(Event):
#     def __init__(self, fileID,executeTime):
#         super().__init__(fileID,executeTime)
    
#     def details(self):
#         print(self.FileID,self.ExecuteTime,self.Status)
    
#     def process(self):
#         self.ExecuteTime += 

# class ResponseEvent(Event):
#     def __init__(self, fileID, executeTime):
#         super().__init__(fileID, executeTime)
    
#     def process(self):


# r= RequestEvent(1,1)
# r.details
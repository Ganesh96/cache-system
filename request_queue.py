# dependencies
import heapq

class Request_Queue():
    def __init__(self):
        self.queued = list()
        
    def pop(self):
        return heapq.heappop(self.queued)[1]
    
    def push(self, event:tuple):
        heapq.heappush(self.queued,event)
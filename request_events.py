# Dependencies
from numpy import argmax
from numpy.random import poisson,multinomial,lognormal

from cache_simulator import *
from request_queue import *
from files import *

class Event:
    def __init__(self, cache_simulator: Cache_Simulator, created_time: int, first:object=None,name=None):
        self.cache_simulator = cache_simulator
        self.created_time = created_time
        self.first = first
        self.finish_time = created_time
        self.name = name
        self.child()

    def __lt__(self,any):
        return True

    def child(self):
        pass

    def execute(self):
        pass
    
    def get_first_request(self):
        node = self
        while(node.first is not None):
            node = node.first
        return node
    
    def __gt__(self,any):
        return True

class New_Request(Event):
    def child(self):
        if(self.name == 'Generate Requests'):
            self.name = 'Generate Requests'
            self.cache_simulator.request_queue.push([self.finish_time,self])
        else:
            self.name = 'New Request'
            self.cache_simulator.number_of_requests = self.cache_simulator.number_of_requests + 1
            self.file_id = argmax(multinomial(1,self.cache_simulator.entire_files.probability))
            self.file_size = self.cache_simulator.entire_files.size[self.file_id]        
            self.cache_simulator.request_queue.push([self.finish_time,self])

    def execute(self):
        if(self.name == 'Generate Requests'):
            reqs_to_handle = poisson(100)
            for i in range(int(reqs_to_handle)):
                New_Request(self.cache_simulator, self.finish_time)
        else:
            if self.cache_simulator.cache_system.file_exists(self.file_id):
                File_Recieved(self.cache_simulator,self.finish_time,self)
            else:
                Arrive_At_Queue(self.cache_simulator,self.finish_time,self)

class Arrive_At_Queue(Event):
    def child(self):
        self.name = 'Arrive at queue'
        self.finish_time = lognormal(0.5,0.4) + self.created_time
        self.cache_simulator.request_queue.push([self.finish_time,self])

    def execute(self):
        self.cache_simulator.fifo.append(self)
        if len(self.cache_simulator.fifo) <= 1:
            Depart_From_Queue(self.cache_simulator,self.finish_time,self)


class Depart_From_Queue(Event):
    def child(self):
        self.name = 'Depart from queue'
        first_request = self.get_first_request()
        self.finish_time = self.created_time + (first_request.file_size/15)
        self.cache_simulator.request_queue.push([self.finish_time,self])

    def execute(self):
        first_request = self.get_first_request()
        self.cache_simulator.cache_system.cache_memory(first_request.file_id)
        File_Recieved(self.cache_simulator,self.finish_time,self)
        self.cache_simulator.fifo.pop(0)
        if len(self.cache_simulator.fifo):
            Depart_From_Queue(self.cache_simulator,self.finish_time,self.cache_simulator.fifo[0])

class File_Recieved(Event):
    def child(self):
        self.name = 'File recieved'
        first_request = self.get_first_request()
        file_size = self.cache_simulator.entire_files.size[first_request.file_id]
        self.finish_time = (file_size/1000) + self.created_time
        self.cache_simulator.request_queue.push([self.finish_time,self])

    def execute(self):
        first_request = self.get_first_request()
        time = [self.finish_time - first_request.created_time, first_request.file_id, first_request.file_size,self]
        self.cache_simulator.completed_requests.append(time)
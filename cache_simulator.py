# Dependencies
from numpy import array

from request_queue import *
from files import *

class Cache_Simulator():
    def __init__(self, Files:Files, Cache):
        self.request_queue = Request_Queue()
        self.number_of_requests = 0
        self.fifo = list()
        self.entire_files = Files
        self.completed_requests = list()
        self.cache_system = Cache
    
    def get_all_requests(self):
        return(array(self.completed_requests)[:,0])
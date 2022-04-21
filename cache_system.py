from cache_simulator import *
from files import *
from request_queue import *

CACHE_MEMORY_SIZE = 100

class Cache_File():
    def __init__(self,file_id,file_size):
        self.score = 0
        self.file_id = file_id
        self.file_size = file_size
        self.next_file = None
        self.previous_file = None
        

class Cache_System():
    def __init__(self,entire_files:Files):
        self.capacity = CACHE_MEMORY_SIZE
        self.memory = dict()
        self.free = CACHE_MEMORY_SIZE
        self.entire_files = entire_files
        self.child()
    
    def child(self):
        pass

    def cache_memory(self,file_id):
        if(file_id not in self.memory):
            if(self.entire_files.size[file_id] < self.free):
                self.free = self.free - self.entire_files.size[file_id]
                self.memory[file_id] = self.entire_files.size[file_id]
                return True
            return False
    
    def file_exists(self,file_id):
        if(file_id not in self.memory):
            return False
        return True

class LPSU(Cache_System):
    
    def child(self):
        pass

    def cache_memory(self,file_id):    
        if(CACHE_MEMORY_SIZE <= self.entire_files.size[file_id] or self.entire_files.size[file_id] > 10):
            return False  
        if(file_id not in self.memory):
            if(self.entire_files.size[file_id] < self.free):
                self.free = self.free - self.entire_files.size[file_id]
                self.memory[file_id] = self.entire_files.size[file_id]*self.entire_files.probability[file_id]
            else:
                while(self.entire_files.size[file_id] >= self.free):
                    fileID = self.get_fileID()
                    self.free = self.free + self.entire_files.size[fileID]
                    del self.memory[fileID]
                self.cache_memory(file_id)
        else:
            self.file_exists(file_id)        
        return True

    def file_exists(self,file_id):
        if(file_id in self.memory):
            self.memory[file_id] = self.memory[file_id] + 0.0625
            return True
        return False
    
    def get_fileID(self):
        fileID = None
        for ID in self.memory:
            if(fileID is None):
                fileID = ID
            else:
                if(self.memory[fileID] > self.memory[ID]):
                    fileID = ID
        return fileID

class LFU(Cache_System):
    
    def child(self):
        pass

    def cache_memory(self,file_id):    
        if(self.entire_files.size[file_id] > CACHE_MEMORY_SIZE or self.entire_files.size[file_id] > 10):
            return False  
        if(file_id not in self.memory):
            if(self.entire_files.size[file_id] < self.free):
                self.free = self.free - self.entire_files.size[file_id]
                self.memory[file_id] = 1
            else:
                while(self.entire_files.size[file_id] >= self.free):
                    ID = self.get_fileID()
                    self.free = self.free + self.entire_files.size[ID]
                    del self.memory[ID]
                self.cache_memory(file_id)
        else:
            self.file_exists(file_id)        
        return True

    def get_fileID(self):
        fileID = None
        for ID in self.memory:
            if(fileID is None):
                fileID = ID
            else:
                if(self.memory[ID] < self.memory[fileID]):
                    fileID = ID
        return fileID
    
    def file_exists(self,file_id):
        if(file_id in self.memory):
            self.memory[file_id] += 1
            return True
        return False
    
class LRU(Cache_System):

    def child(self):
        self.head = None
        self.tail = None
        
    def cache_memory(self,file_id):    
        if(self.entire_files.size[file_id] > CACHE_MEMORY_SIZE or self.entire_files.size[file_id] > 10):
            return False  
        if(file_id not in self.memory):
            file = Cache_File(file_id,self.entire_files.size[file_id]) 
            if(self.entire_files.size[file_id] < self.free):
                if(self.head is None):
                    self.head = file
                if(self.tail is None):
                    self.tail = file
                else:
                    self.tail.next_file = file
                    file.previous_file = self.tail                    
                    self.tail = file
                    self.tail.next_file = None
                file.score = file.score + 1
                self.memory[file.file_id] = file
                self.free = self.free - file.file_size
            else:
                while(self.free <= file.file_size):
                    if(self.head is None):
                        raise Exception('No free memory')                       
                    deleted_file = self.head
                    self.head = deleted_file.next_file
                    if(self.head is None):
                        self.tail = None
                    else:
                        self.head.previous_file = None
                    self.free = self.free + deleted_file.file_size
                    del self.memory[deleted_file.file_id]
                self.cache_memory(file_id)  
        else:
            self.file_exists(file_id)        
        return True
        
    def file_exists(self,file_id):
        if(file_id in self.memory):
            requested_file = self.memory[file_id]
            if(requested_file.next_file is not None and requested_file.previous_file is None):
                self.head = requested_file.next_file
                self.head.previous_file = None
                self.tail.next_file = requested_file
                requested_file.previous_file = self.tail   
                self.tail = requested_file
                self.tail.next_file = None
            elif(requested_file.next_file is not None and requested_file.previous_file is not None):
                requested_file.previous_file.next_file = requested_file.next_file
                requested_file.next_file.previous_file = requested_file.previous_file
                self.tail.next_file = requested_file
                requested_file.previous_file = self.tail   
                self.tail = requested_file
                self.tail.next_file = None
            requested_file.score = requested_file.score + 1
            return True
        return False
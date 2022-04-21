# Cache-System
## Objective
   A cache system is simulated by using probabily dsitribution on file, request events and observing the results of each cache policy for these distributions. Cache policies used are least probabilistically and storage used aka LPSU, least frequently used aka LFU and least recently used aka LRU.

## Requirements
   Use Jupyter notebook if possible as it has built-in installations of these libraries, in that case you would need to open the project folder in the notebook and then copy paste the main.py code onto the notebook and run the cell.
    Alternatively, you can try run the command python3 -m pip install numpy in command line, python3 -m pip install seaborn and then python -m heapq. Then you should be able to execute the main.py using python run command in the terminal specifying the file name main.py. Make sure to close the graph window to continue the execution of the code.
    1. Open Jupyter notebook or other IDE.
    1. Open the folder as project folder.
    1. Execute the main.py or main.ipynb - in case of Jupyter notebook or visual code.
    Alternatively,
    1. Open terminal.
    1. Change to project directory.
    1. PIP install all dependencies like Numpy, Seaborn, matplotlib, heapq.
    1. Type python main.py and view the plot windows, you need to close the window to continue the execution.
    
## Dependencies
   1. IDE: Jupyter Notebook or Visual Studio Code to easily run.
   1. Libraries: Numpy, Seaborn, matplotlib, heapq.
   1. Language: Python 3.9

## Parameters
   1. The number of simulations can be changed by going for loop written for iterations in main.py.
   1. Global time for simulation can be changed by going to main.py in time for loop
   1. Number of request per second can be changed by going to files.py and changing in the process method of the New_Request
   1. Number of files can be changed by going to files.py and changes in the pareto function.
   1. The memory size of cache can be changed by modifying value of CACHE_MEMORY_SIZE in the cache_system.py
   1. File probability and size dsitribution can be changed by going to files.py and entering a parameters for pareto function.
   1. Time taken for round trip in internet can be changed by going constructor of Arrive_At_Queue class in request_events.py.

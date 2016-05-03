# Periscope Data Problem
Coding challenge for Periscope Data

**Language:** Python 2.7

**Running the program**

This is a regular Python program which can be run either using the command line 
```
python roomba.py 
```

or    

by using the Python shell.   

**Prerequisite:**  
The input.txt file should be present in the same folder as the program.  


**Tests**  
The code has it's own test cases which can be run is the same way as the code.  
```
python roomba_test.py
```
The tests modify input.txt to check for different cases.  

**Approach**  

The interesting thing about this problem was to decide on a data structure to represent the dirty patches. The 2 options were to have a 2*2 array with 1 for dirty patch and a 0 for a clean patch. The advantage of this approach is that the access time for checking if a block is dirty or not will be O(1). The disadvantage of this approach is that space complexity is O(n<sup>2</sup>).  

Another approach, the one I took, was to optimize the data structure for a sparse matrix. If the number of dirt patches is much less than the number of clean patches, this approach has a better performance. I represented the dirt patches on each row as a list which is stored as the value in a dictionay with the key as the row number. This saves a lot of space while not having considerable impact on access time.



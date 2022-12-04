from os import popen
file = r"C:\Users\student\Desktop\Project final\LLC\.github\LRU\trace2.txt"
file_pointer = open (file)
for x in file_pointer:
    print(x,end='')

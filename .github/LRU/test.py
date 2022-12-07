from os import popen
file = r"C:\Users\student\Desktop\Project final\LLC\.github\LRU\trace2.txt"
file_pointer = open (file)
#print (x,end='') # to aviode extra lines while priniting from  file
for x in file_pointer:
    trace_lines = x
    trace_lines = trace_lines.strip()
    palli = trace_lines.split(" ")
    print (palli[1])
   

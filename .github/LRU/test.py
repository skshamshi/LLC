from os import popen
import os
txt = ".txt"
basepath = r"C:\Users\student\Downloads\Archive"
path = []
for fname in os.listdir(basepath):
    if os.path.isdir(fname):
      continue
    path.append(os.path.join(basepath, fname))
    fname = fname+txt
    with open(os.path.join(basepath,fname),'w') as f:
        f.write("hello")



        

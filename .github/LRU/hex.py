import os
basepath = r"C:\Users\student\Downloads\Archive"
fname = "pallibabu.din"
fname1 = ".txt"
fname2 = fname+fname1
f = open(os.path.join(basepath,fname2),'w')
st1 = "hello"
st2 = "bolo"

f.write (st1.rstrip('\n'))
f.write ("hello")
f.write (st2.rstrip('\n'))

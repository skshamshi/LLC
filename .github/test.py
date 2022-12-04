
print ("Welcome to group number2 MSD project")

filename = input ("enter the path from where we need to trace \n")
flag = input ("Enter D if you want debug mode and S for Silent mode\n")
f= open(filename)
n=1
if flag == "S" :
 for line in f:
  print (n,line)
  n += 1
elif flag == "D" :
 for line in f:
  input ("Enter to continue")
  print (n,line)
  n += 1
f.close()  
import pprint
import math
global cache

def evict(row,col):
    cache[row][col]=0x00000000
    #return array

associativity=8
total_lines=6
cache =[['x' for i in range (1,associativity+1)] for k in range(1,total_lines+1)]
#pprint.pprint(cache)
cache[3][6] = 0x000032AC
#pprint.pprint(cache)
pprint.pprint(cache)
addr=0x000032AD
arr = [[[] for i in range(8)] for j in range(6)]
#pprint.pprint(arr)
arr [3][4]=addr
#pprint.pprint(arr)
#arr.insert(([4][1]),0x0000DFE6)
#pprint.pprint(arr)
pprint.pprint('latest cache')
cache =[['x' for i in range (1,associativity+1)] for k in range(1,(2**5)+1)]
way_count= 1
line_count= 1
for line in cache:
  for way in line:
    way_index= line.index(way)
    line_index= cache.index(line)
    cache[line_index][way_index]= (line_count*10) + way_count
    if(way_count==8):
      way_count= 1
    else:
      way_count+=1
  if(line_count==32):
    line_count= 1
  else:
    line_count+=1
    
pprint.pprint(cache)

#evict(line,way)
evict(3,7)
pprint.pprint(cache)

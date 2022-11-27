import pprint
col, row = (5, 5)
arr = [[1]*col]*row
print(arr)

associativity=8
total_lines=6
cache =[['x' for i in range (associativity)] for k in range(total_lines)]
#pprint.pprint(cache)
cache[3][6] = 0x000032AC
pprint.pprint(cache)
addr=0x000032AD
arr = [[[] for i in range(8)] for j in range(6)]
pprint.pprint(arr)
arr [3][4]=addr
pprint.pprint(arr)
#arr.insert(([4][1]),0x0000DFE6)
pprint.pprint(arr)
print('latest cache')
cache =[[0 for p in range (9)] for q in range(2**5)]
pprint.pprint(cache)
cache[6][7]=addr
pprint.pprint(cache)

#eviction 
def eviction(array,row,col):
    import math
    array[row][col]=0x00000000

eviction(cache,6,7)
pprint.pprint(cache)

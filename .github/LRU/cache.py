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

cache.pop(5)
pprint.pprint(cache)
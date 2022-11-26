Sets = 32768
Associative = 8
cache = []
class line:
   def __init__ (self,MESI,TAG):
      self.MESI = MESI
      self.TAG = TAG
class set:
   def __init__(self,LRU,LINE):
      self.LRU = LRU
      self.LINE = LINE
#z= line ([],[])
#print (z.MESI)
#x = set ("lru",z)
#x.LINE.MESI = "HELLO"

for i in range (1,Sets):
   i = set ([],[])
   for j in range (1,Associative):
      j = line ([],[])
      i.LINE.append(j)
cache.append(i)

#cache =[[ for i in range (associativity)] for k in range(total_lines)]
print (cache[Sets[0]])

class line:
   def __init__ (self,MESI,TAG):
      self.MESI = MESI
      self.TAG = TAG
class set:
   def __init__(self,LRU,LINE):
      self.LRU = LRU
      self.LINE = LINE
z= line ([],[])
#print (z.MESI)
x = set ("lru",z)
x.LINE.MESI = "HELLO"

print (x.LINE.MESI)

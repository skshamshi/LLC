class line:
   def __init__ (self,MESI,TAG):
      self.MESI = MESI
      self.TAG = TAG
      self.LINE = [MESI,TAG]

    
class lines:
    def __init__(self):
        self.lines1 = []
        for l1 in range (5):
         self.lines1.append(line([range],[range]))
 
l1 = lines ()
print (l1(line[0]))
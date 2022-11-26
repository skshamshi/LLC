def GetSnoopResult (address):
  import math
  result = "{0:032b}".format(int(address, 16))
  SnoopBits = str(result[30:33])
  print (SnoopBits)
  if SnoopBits == "00":
       return "HIT"
  elif SnoopBits == "01":
       return "NOHIT"
  elif SnoopBits == "10":
       return "HITM"
  else:
   return "NOHIT"
SnoopResult = GetSnoopResult ("1ABCDEF7")
print(SnoopResult)
#import os
#filename1 = "c:\Users\student\Desktop\Project final\LLC\.github\LRU\catche_memory.py"
#filename = input("enter path")
#print (filename)

#(filename)
#print (filename)

#mapping of address 
#commit comment
def address_mapping (address):
  import math
  address = address
# Code to convert hex to binary
  result = "{0:032b}".format(int(address, 16))
  tag_bits = str(result[0:11])
  index = str(result[11:26])
  byte_select_bits = str (result[26:32])
  return tag_bits,index,byte_select_bits

# variables to choose number of sets and aasociativity
Sets = 3
Associative = 8 

#calling address mapping function with random address in trace file
Tag,Index,Byteselect = address_mapping ("1ABCDEF0")
Tag_decimal = int(Tag,2)
Tag_decimal2 = 270
Tag_decimal3 = 271
Tag_decimal4 = 272
Tag_decimal5 = 273
Tag_decimal6 = 274
Tag_decimal7 = 275
Tag_decimal8 = 276
Tag_decimal9 = 277
#Index_decimal = int(Tag,2)
Index_decimal = 1
#commit test
#creating empty cache memory
cache = []

# line class
class line:
   def __init__ (self,MESI,TAG):
      self.MESI = MESI
      self.TAG = TAG
      self.LINE = [MESI,TAG]

# set class
class set:
   def __init__(self,LRU,LINES):
      self.LRU = LRU
      self.LINES = LINES
      self.SET = [LRU,LINES]


#intialsing empty cache arrays
for i in range (1,Sets):
   i = set ([],[])
   for j in range (0,Associative):
      j = line ([],[])
      j.MESI = "0"
      i.LINES.append (j)
   cache.append(i)


def Hit_or_Miss (Index_decimal,Tag_decimal):
   if (Index_decimal > Sets):
      print ("out of cache bound")
   else:
      selected_set = cache [Index_decimal]
      lines_count = 0
      Invalid_lines_count = 0
      for line_obj in (selected_set.LINES):
            lines_count += 1
            if(line_obj.MESI == "0"):
               Invalid_lines_count += 1
               if (line_obj.TAG != Tag_decimal):
                  continue
               line_obj.TAG = Tag_decimal
               line_obj.MESI = "1"
               break
            elif(line_obj.MESI == "1" and line_obj.TAG ==Tag_decimal):
                  print ("HIT")
                  break
            if (lines_count == 8):
               print("calling LRU")


#cache [Index_decimal]
Hit_or_Miss(Index_decimal,Tag_decimal)
Hit_or_Miss(Index_decimal,Tag_decimal)
Hit_or_Miss(Index_decimal,Tag_decimal2)
Hit_or_Miss(Index_decimal,Tag_decimal2)
Hit_or_Miss(Index_decimal,Tag_decimal3)
Hit_or_Miss(Index_decimal,Tag_decimal3)
Hit_or_Miss(Index_decimal,Tag_decimal4)
Hit_or_Miss(Index_decimal,Tag_decimal4)
Hit_or_Miss(Index_decimal,Tag_decimal5)
Hit_or_Miss(Index_decimal,Tag_decimal5)
Hit_or_Miss(Index_decimal,Tag_decimal6)
Hit_or_Miss(Index_decimal,Tag_decimal6)
Hit_or_Miss(Index_decimal,Tag_decimal7)
Hit_or_Miss(Index_decimal,Tag_decimal7)
Hit_or_Miss(Index_decimal,Tag_decimal8)
Hit_or_Miss(Index_decimal,Tag_decimal8)
Hit_or_Miss(Index_decimal,Tag_decimal9)
Hit_or_Miss(Index_decimal,Tag_decimal9)

#print(Tag_decimal)

#mapping of address 
def address_mapping (address):
  import math
  address = address
# Code to convert hex to binary
  result = "{0:032b}".format(int(address, 16))
  tag_bits = str(result[0:11])
  index = str(result[11:26])
  byte_select_bits = str (result[26:32])
  return tag_bits,index,byte_select_bits

# variables to choose numbre of sets and aasociativity
Sets = 3
Associative = 8 

#calling address mapping function with random address in trace file
Tag,Index,Byteselect = address_mapping ("1ABCDEF0")
Tag_decimal = int(Tag,2)
#Index_decimal = int(Tag,2)
Index_decimal = 1

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

#for set_obj in (cache):             #set objects
     #print("first set done")
     #print (set_obj.SET)
     #for line_obj in (set_obj.SET[1]):    #line objest
       #print(line_obj.LINE)
   #print (obj)
def Hit_or_Miss (Index_decimal):
   if (Index_decimal > Sets):
      print ("out of cache bound")
   else:
      selected_set = cache [Index_decimal]
      print (selected_set)
      for line_obj in (selected_set.LINES): 
            #print (line_obj.LINE)
            if(line_obj.MESI == "0"):
               line_obj.TAG = Tag_decimal
               print (line_obj.TAG)
               break
            ###
               #line__wrote = 1

           
               #print (line_obj.TAG)

#cache [Index_decimal]
Hit_or_Miss(Index_decimal)
#print(Tag_decimal)

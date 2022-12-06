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
   i.LRU = 0
   for j in range (0,Associative):
      j = line ([],[])
      j.MESI = 0
      i.LINES.append (j)
   cache.append(i)


def Hit_or_Miss (Index_decimal,Tag_decimal):
   line_count =  0
   empty_lines = 0
   if (Index_decimal > Sets):
      print ("out of cache bound")
   else:
      selected_set = cache [Index_decimal]
      for line_obj in (selected_set.LINES):
            if(line_obj.MESI == 0):
               empty_lines += 1
               line_count += 1
               if (line_count != 8):
                  continue
               else:
                  return 'MISS',empty_lines,line_count
            else:
               if(line_obj.TAG !=Tag_decimal ):
                  line_count += 1
                  if (line_count != 8):
                     continue
                  else:
                     return 'MISS',empty_lines,line_count
               else:
                  line_count += 1
                  return 'HIT',empty_lines,line_count

def catch_fill (Index_decimal,Tag_decimal):
   selected_set = cache [Index_decimal]
   for line_obj in (selected_set.LINES):
      if(line_obj.MESI == 1):
         continue
      else:
       line_obj.TAG = Tag_decimal
       line_obj.MESI = 1
       break
def update_LRU (set,way):
    selected_set = cache [Index_decimal]
    print (set)
    way = "{0:03b}".format(way)
    print (way)
    LRU_list = [str(i) for i in list('{0:07b}'.format(selected_set.LRU))]
    #int(i) for i in list('{0:0b}'.format(test_num))]
    if (way[0] == "0"):
     LRU_list[0] = "0"
     if (way[1] == "0"):
        LRU_list[1] = "0"
        if (way[2] == "0"):
            LRU_list[3] = "0"
        else:
            LRU_list[3] = "1"
     else:
        LRU_list[1] = "1"
        if (way[2] == "0"):
            LRU_list[4] = "0"
        else:
            LRU_list[4] = "1"

    else:
     LRU_list[0] = "1"
     if (way[1] == "0"):
        LRU_list[2] = "0"
        if (way[2] == "0"):
            LRU_list[5] = "0"
        else:
            LRU_list[5] = "1"
     else:
        LRU_list[2] = "1"
        if (way[2] == "0"):
            LRU_list[6] = "0"
        else:
            LRU_list[6] = "1"
    print (LRU_list)
    print(''.join(LRU_list))


def catch_search (Index_decimal,Tag_decimal):
   y,empty_lines,line_count = Hit_or_Miss(Index_decimal,Tag_decimal)
   if (y == "HIT"):
      #print ("HIT")
      #print ("valid data is in way",line_count-1)
      update_LRU (Index_decimal,line_count-1)
      #way_binary = ("{0:03b}".format(line_count-1))
      #print (way_binary[0])
      #print ("calling update LRU function")
   elif (y == "MISS" and empty_lines != 0):
      #print (empty_lines)
      #print ("MISS")
      catch_fill (Index_decimal,Tag_decimal)
   else:
    print ("calling LRU")


catch_search(Index_decimal,Tag_decimal2)
catch_search(Index_decimal,Tag_decimal2)

catch_search(Index_decimal,Tag_decimal)
catch_search(Index_decimal,Tag_decimal)

catch_search(Index_decimal,Tag_decimal3)
catch_search(Index_decimal,Tag_decimal3)
catch_search(Index_decimal,Tag_decimal4)
catch_search(Index_decimal,Tag_decimal4)
catch_search(Index_decimal,Tag_decimal5)
catch_search(Index_decimal,Tag_decimal5)
catch_search(Index_decimal,Tag_decimal6)
catch_search(Index_decimal,Tag_decimal6)
catch_search(Index_decimal,Tag_decimal7)
catch_search(Index_decimal,Tag_decimal7)
catch_search(Index_decimal,Tag_decimal8)
catch_search(Index_decimal,Tag_decimal8)
catch_search(Index_decimal,Tag_decimal9)
catch_search(Index_decimal,Tag_decimal9)

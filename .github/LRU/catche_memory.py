import sys
#mapping of addrees to index, tag and byte select bits
global cache_miss
global cache_hits
global read_count
global write_count
def init_fun():
   global cache_miss
   global cache_hits
   global read_count
   global write_count
   global hit
   hit = 0
   cache_miss = 0
   cache_hits = 0
   read_count = 0
   write_count = 0


def address_mapping (address):
  import math
  address = address
  # Code to convert hex to binary
  result = "{0:032b}".format(int(address, 16))
  tag_bits = str(result[0:11])
  index = str(result[11:26])
  byte_select_bits = str (result[26:32])
  return tag_bits,index,byte_select_bits
def valid_address(address):
  
  try:
   Hex=int(address, 16)
   return True
  except ValueError:
   #print("Ivalid address\n")
   return False
      
def GetSnoopResult (byte_select_bits):
  import math
  SnoopBits = str(byte_select_bits[4:6])
  if SnoopBits == "00":
       return "HIT"
  elif SnoopBits == "01":
       return "HITM"
  elif SnoopBits == "10":
       return "NOHIT"
  else:
   return "NOHIT"


# variables to choose number of sets and aasociativity
Sets = 32768
Associative = 8 
Normalmode = 0

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

# update LRU function
def update_LRU (set,way):
    selected_set = cache [Index_decimal]
    way = "{0:03b}".format(way)
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
    selected_set = cache [Index_decimal]
    selected_set.LRU = int(''.join(LRU_list),2)

# Get LRU function
def Get_LRU(Index_decimal):
   #global f
   selected_set = cache [Index_decimal]
   LRU_list = [str(i) for i in list('{0:07b}'.format(selected_set.LRU))]
   way = 0
   way = [str(i) for i in list('{0:03b}'.format(way))]
   if (LRU_list[0] == "0"):
     way[0] = "1"
     if (LRU_list[2] == "0"):
        way[1] = "1"
        if (LRU_list[6] == "0"):
            way[2] = "1"
        else:
            way[2] = "0"
     else:
        way[1] = "0"
        if (LRU_list[5] == "0"):
            way[2] = "1"
        else:
            way[2] = "0"
   else:
     way[0] = "0"
     if (LRU_list[1] == "0"):
        way[1] = "1"
        if (LRU_list[4] == "0"):
            way[2] = "1"
        else:
            way[2] = "0"
     else:
        way[1] = "0"
        if (LRU_list[3] == "0"):
            way[2] = "1"
        else:
            way[2] = "0"
   way = int(''.join(way),2)
   #f.write (way)
   #f.write("LRU called")
   if(selected_set.LINES[0].MESI== 2):
      if(Normalmode):
       #print ("hello")
       print(f)
       f.write("L2:GETLINE\n")
       #
       f.write("BusOp:WRITE Address: ")
       f.write(address)
       f.write("\n")
       f.write("L2:EVICTLINE, way: ")
       f.write(str(way))
       f.write("\n")
       #f.write ("L2:INVALIDATELINE")
      selected_set.LINES[0].MESI = 0
   else:
      if(Normalmode):
       #f.write ("L2:INVALIDATELINE")
        f.write ("L2:EVICTLINE, way: ")
        f.write(str(way))
        f.write("\n")
      selected_set.LINES[0].MESI = 0
   update_LRU (Index_decimal,way)

def catch_search (Index_decimal,Tag_decimal,opcode):
   
   
   #f.write(address)
   y,empty_lines,line_count = Hit_or_Miss(Index_decimal,Tag_decimal)
   selected_set = cache [Index_decimal]
   #f.write ("checking hit or no ",y)
   if (y=="Nothing returned"):
      return
   else:
    if (y == "HIT"):
      global hit 
      hit = 1
      global cache_miss
      global cache_hits
      cache_hits += 1
      update_LRU (Index_decimal,line_count-1)
      if (opcode == "0" or opcode == "2"):
         global write_count
         global read_count
         read_count += 1
         #f.write (MESI_state(selected_set.LINES[line_count-1].MESI))
         #f.write (selected_set.LINES[line_count-1].TAG)
         #f.write (Index_decimal)
         if(Normalmode):
          f.write ("L2: SENDLINE: ")
          f.write(address)
          f.write("\n")
          #f.write (MESI_state(selected_set.LINES[line_count-1].MESI))
      elif (opcode == "1"):
         global write_count
         write_count += 1
         #f.write (MESI_state(selected_set.LINES[line_count-1].MESI))
         if (selected_set.LINES[line_count-1].MESI == 3):
            if(Normalmode):
             f.write ("BusOp:INVALIDATE Address:")
             f.write(address)
             f.write(": ")
             f.write("Snoop Result: ")
             f.write(GetSnoopResult(byte_select_bits))
             f.write("\n")
         selected_set.LINES[line_count-1].MESI = 2
         #f.write (MESI_state(selected_set.LINES[line_count-1].MESI))


   
    elif (y == "MISS" and empty_lines != 0):
      global cache_miss
      cache_miss += 1
      line_count = catch_fill (Index_decimal,Tag_decimal,opcode)
      update_LRU (Index_decimal,line_count-1)
    else:
     Get_LRU(Index_decimal)

def MESI_state (num):
   if(num == 0):
      return "I"
   elif (num == 1):
      return "Ex"
   elif (num == 2):
      return "M"
   else:
      return "S"

def MESI (Index_decimal,Tag_decimal,opcode):
   y,empty_lines,line_count = Hit_or_Miss(Index_decimal,Tag_decimal)
   selected_set = cache [Index_decimal]
   #f.write ("checking hit or no ",y)
   if(y == "MISS"):
      #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
      #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
      return
   elif (y == "HIT"):
      
      if (opcode == "6" ):
       if (selected_set.LINES[line_count-1].MESI == 1 or selected_set.LINES[line_count-1].MESI == 3 ):
         #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
         if(Normalmode):
          f.write ("L2:INVALIDATELINE\n")
         selected_set.LINES[line_count-1].MESI = 0
         #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
       else:
         if(Normalmode):
          f.write ("L2:GETLINE\n")
          f.write ("BusOp:WRITE Address: ")
          f.write(address)
          f.write("\n")
          f.write ("L2:INVALIDATELINE\n")
         #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
         selected_set.LINES[line_count-1].MESI = 0
         #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
      elif (opcode =="4"):
         if (selected_set.LINES[line_count-1].MESI == 1):
            #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
            selected_set.LINES[line_count-1].MESI = 3
            #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
         elif (selected_set.LINES[line_count-1].MESI == 2):
            #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
            if(Normalmode):
             f.write ("L2:GETLINE\n")
            #f.write ("BusOp:WRITE Address:",address)
            selected_set.LINES[line_count-1].MESI = 3
            #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
      elif (opcode == "3" ):
       if (selected_set.LINES[line_count-1].MESI == 3 ):
         #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
         if(Normalmode):
          f.write ("L2:INVALIDATELINE\n")
         #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
         selected_set.LINES[line_count-1].MESI = 0
         #f.write(MESI_state(selected_set.LINES[line_count-1].MESI))
      



      




def Hit_or_Miss (Index_decimal,Tag_decimal):
   global f
   line_count =  0
   empty_lines = 0
   if (Index_decimal > Sets):
      f.write ("out of cache bound")
      return 'Nothing returned','Nothing returned','Nothing returned'
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

def catch_fill (Index_decimal,Tag_decimal,opcode):
   global f
   line_count = 0
   selected_set = cache [Index_decimal]
   for line_obj in (selected_set.LINES):
      if(line_obj.MESI != 0):
         line_count += 1
         continue
      else:
       line_count += 1
       line_obj.TAG = Tag_decimal
       if (opcode == "0" or opcode == "2"):
         if (GetSnoopResult(byte_select_bits) == "HIT"):
          #f.write ("I am here to test")
          if(Normalmode):
           f.write ("BusOp:READ Address:")
           f.write(address)
           f.write(": ")
           f.write("Snoop Result:")
           f.write(GetSnoopResult(byte_select_bits))
           f.write("\n")
           f.write ("L2: SENDLINE")
           f.write(address)
           f.write("\n")
           #f.write (MESI_state(line_obj.MESI))
          line_obj.MESI = 3
          #f.write (MESI_state(line_obj.MESI))
          return line_count
         elif (GetSnoopResult(byte_select_bits) == "HITM"):
          if(Normalmode):
           f.write ("L2: SENDLINE")
           f.write(address)
           f.write("\n")
          if (Normalmode):
           f.write ("BusOp:READ Address:")
           f.write(address)
           f.write(": ")
           f.write("Snoop Result: ")
           f.write(GetSnoopResult(byte_select_bits))
           f.write("\n")
           #f.write (MESI_state(line_obj.MESI))
          line_obj.MESI = 3
          #f.write (MESI_state(line_obj.MESI))
          return line_count
         else:
          #f.write (GetSnoopResult(byte_select_bits))
          #f.write (MESI_state(line_obj.MESI))
          line_obj.MESI = 1
          #f.write (MESI_state(line_obj.MESI))
          if(Normalmode):
           f.write ("BusOp:READ Address:")
           f.write(address)
           f.write(": ")
           f.write("Snoop Result: ")
           f.write(GetSnoopResult(byte_select_bits))
           f.write("\n")
           f.write ("L2: SENDLINE\n")
           f.write(address)
           f.write("\n")
          return line_count
       elif (opcode == "1"):
          line_obj.TAG = Tag_decimal
          if(Normalmode):
           f.write ("BusOp:RWIM Address: ")
           f.write(address)
           f.write(" ")
           f.write("Snoop Result: ")
           f.write(GetSnoopResult(byte_select_bits))
           f.write("\n")
          #f.write (MESI_state(line_obj.MESI))
          line_obj.MESI = 2
          #f.write (MESI_state(line_obj.MESI))
          return line_count
#new part
from os import popen
import os
txt = ".txt"
basepath = r"C:\Users\student\Downloads\Archive"
path = []
for fname in os.listdir(basepath):
    if os.path.isdir(fname):
      continue
    path.append(os.path.join(basepath, fname))
    fname1 = fname+txt
    f= open(os.path.join(basepath,fname1),'w')
    #f.write("nmothing wrong with pointer")
    init_fun ()
    with open(os.path.join(basepath,fname),'r') as f1:
      print(fname)
      for x in f1:
       #print (x)
       trace_lines = x
       trace_lines = trace_lines.strip()
       trace_lines1 = trace_lines.split()
       #print(trace_lines1)
       opcode = trace_lines1[0]
       address = trace_lines1[1]
       valid_addr = valid_address(address)
       if (valid_addr):
        tag_bits,index,byte_select_bits=address_mapping(address)
       else:
        f.write ("continuing the operations with next line of trace")
       Tag_decimal = int(tag_bits,2)
    #f.write ("tag name",Tag_decimal)
    
       Index_decimal = int(index,2)
    #f.write ("index decimal",Index_decimal)
       if (opcode == "0" or opcode == "1" or opcode == "2"):
         catch_search(Index_decimal,Tag_decimal,opcode)
       elif (opcode == "3" or opcode == "4" or opcode == "5" or opcode == "6"):
         hit = 0
         MESI (Index_decimal,Tag_decimal,opcode)
       elif (opcode == "8"):
        hit = 0
        for set_clear in cache:
         set_clear.LRU = 0
         for line_clear in set_clear.LINES:
            line_clear.MESI = 0
       elif (opcode == "9"):
         k = 0
         l = 0
         for i in cache:
          l = 0
          k += 1
          cntrl = 0
          for j in i.LINES:
            l += 1
            if (j.MESI != 0):
               #print (fname)
               #print (f)
               #f.write("palli enti e gola")
               f.write("way: ")
               f.write(str(l))
               f.write (" TAG: ")
               f.write(str(j.TAG))
               f.write(" ")
               f.write ("MESI: ")
               f.write(MESI_state(j.MESI))
               f.write(" ")
               cntrl = 1
          if (cntrl):
             f.write("Set: ")
             
             f.write(str(k))
             f.write(" ")
             f.write ("LRU: ")
             f.write("{0:07b}".format(int(i.LRU),2))
             f.write("\n")
       else:
         print("Invalid command")
      if(hit):
       print("testing",hit)
       hit_ratio = cache_hits/(cache_hits+cache_miss)
      else:
        hit_ratio = "Invalid hit ratio"
      f.write ("Read_count:")
      f.write(str(read_count))
      f.write(" Write_count:")
      f.write(str(write_count))
      f.write(" cahe_hits:")
      f.write(str(cache_hits))
      f.write(" cahce_misses:")
      f.write(str(cache_miss))
      f.write(" Hit ratio:")
      f.write(str(hit_ratio))
      
      
      
  

#mapping of addrees to index, tag and byte select bits
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
   print ("Ivalid address")
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
Normalmode = 1

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
   #print (way)
   #print("LRU called")
   if(selected_set.LINES[0].MESI== 2):
      if(Normalmode):
       print ("L2:GETLINE")
       print ("L2:INVALIDATELINE")
      selected_set.LINES[0].MESI = 0
   else:
      if(Normalmode):
       print ("L2:INVALIDATELINE")
      selected_set.LINES[0].MESI = 0
   update_LRU (Index_decimal,way)

def catch_search (Index_decimal,Tag_decimal,opcode):
   #print(address)
   y,empty_lines,line_count = Hit_or_Miss(Index_decimal,Tag_decimal)
   selected_set = cache [Index_decimal]
   #print ("checking hit or no ",y)
   if (y=="Nothing returned"):
      return
   else:
    if (y == "HIT"):

      update_LRU (Index_decimal,line_count-1)
      if (opcode == "0" or opcode == "2"):
         #print (MESI_state(selected_set.LINES[line_count-1].MESI))
         #print (selected_set.LINES[line_count-1].TAG)
         #print (Index_decimal)
         if(Normalmode):
          print ("L2: SENDLINE", address)
          #print (MESI_state(selected_set.LINES[line_count-1].MESI))
      elif (opcode == "1"):
         #print (MESI_state(selected_set.LINES[line_count-1].MESI))
         if (selected_set.LINES[line_count-1].MESI == 3):
            if(Normalmode):
             print ("BusOp:INVALIDATE Address:",address,"Snoop Result:",GetSnoopResult(byte_select_bits))
         selected_set.LINES[line_count-1].MESI = 2
         #print (MESI_state(selected_set.LINES[line_count-1].MESI))


   
    elif (y == "MISS" and empty_lines != 0):
      line_count = catch_fill (Index_decimal,Tag_decimal,opcode)
      update_LRU (Index_decimal,line_count-1)
    else:
     Get_LRU(Index_decimal)

def MESI_state (num):
   if(num == 0):
      print ("I")
   elif (num == 1):
      print("Ex")
   elif (num == 2):
      print("M")
   else:
      print ("S")

def MESI (Index_decimal,Tag_decimal,opcode):
   y,empty_lines,line_count = Hit_or_Miss(Index_decimal,Tag_decimal)
   selected_set = cache [Index_decimal]
   #print ("checking hit or no ",y)
   if(y == "MISS"):
      #print(MESI_state(selected_set.LINES[line_count-1].MESI))
      #print(MESI_state(selected_set.LINES[line_count-1].MESI))
      return
   elif (y == "HIT"):
      
      if (opcode == "6" ):
       if (selected_set.LINES[line_count-1].MESI == 1 or selected_set.LINES[line_count-1].MESI == 3 ):
         #print(MESI_state(selected_set.LINES[line_count-1].MESI))
         if(Normalmode):
          print ("L2:INVALIDATELINE")
         selected_set.LINES[line_count-1].MESI = 0
         #print(MESI_state(selected_set.LINES[line_count-1].MESI))
       else:
         if(Normalmode):
          print ("L2:GETLINE")
          print ("BusOp:WRITE Address:",address)
          print ("L2:INVALIDATELINE")
         #print(MESI_state(selected_set.LINES[line_count-1].MESI))
         selected_set.LINES[line_count-1].MESI = 0
         #print(MESI_state(selected_set.LINES[line_count-1].MESI))
      elif (opcode =="4"):
         if (selected_set.LINES[line_count-1].MESI == 1):
            #print(MESI_state(selected_set.LINES[line_count-1].MESI))
            selected_set.LINES[line_count-1].MESI = 3
            #print(MESI_state(selected_set.LINES[line_count-1].MESI))
         elif (selected_set.LINES[line_count-1].MESI == 2):
            #print(MESI_state(selected_set.LINES[line_count-1].MESI))
            if(Normalmode):
             print ("L2:GETLINE")
            #print ("BusOp:WRITE Address:",address)
            selected_set.LINES[line_count-1].MESI = 3
            #print(MESI_state(selected_set.LINES[line_count-1].MESI))
      elif (opcode == "3" ):
       if (selected_set.LINES[line_count-1].MESI == 3 ):
         #print(MESI_state(selected_set.LINES[line_count-1].MESI))
         if(Normalmode):
          print ("L2:INVALIDATELINE")
         #print(MESI_state(selected_set.LINES[line_count-1].MESI))
         selected_set.LINES[line_count-1].MESI = 0
         #print(MESI_state(selected_set.LINES[line_count-1].MESI))
      



      




def Hit_or_Miss (Index_decimal,Tag_decimal):
   line_count =  0
   empty_lines = 0
   if (Index_decimal > Sets):
      print ("out of cache bound")
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
          #print ("I am here to test")
          if(Normalmode):
           print ("BusOp:READ Address:",address,"Snoop Result:",GetSnoopResult(byte_select_bits))
           print ("L2: SENDLINE", address)
           #print (MESI_state(line_obj.MESI))
          line_obj.MESI = 3
          #print (MESI_state(line_obj.MESI))
          return line_count
         elif (GetSnoopResult(byte_select_bits) == "HITM"):
          print ("L2: SENDLINE", address)
          if (Normalmode):
           print ("BusOp:READ Address:",address,"Snoop Result:",GetSnoopResult(byte_select_bits))
           #print (MESI_state(line_obj.MESI))
          line_obj.MESI = 3
          #print (MESI_state(line_obj.MESI))
          return line_count
         else:
          #print (GetSnoopResult(byte_select_bits))
          #print (MESI_state(line_obj.MESI))
          line_obj.MESI = 1
          #print (MESI_state(line_obj.MESI))
          if(Normalmode):
           print ("BusOp:READ Address:",address,"Snoop Result:",GetSnoopResult(byte_select_bits))
           print ("L2: SENDLINE", address)
          return line_count
       elif (opcode == "1"):
          line_obj.TAG = Tag_decimal
          if(Normalmode):
           print ("BusOp:RWIM Address:",address,"Snoop Result:",GetSnoopResult(byte_select_bits))
          #print (MESI_state(line_obj.MESI))
          line_obj.MESI = 2
          #print (MESI_state(line_obj.MESI))
          return line_count


from os import popen
file = r"C:\Users\student\Desktop\Project final\LLC\.github\LRU\trace2.txt"
file_pointer = open (file)
trace_line_number = 0
for x in file_pointer:
    trace_line_number += 1
    #print("reading trace line number",trace_line_number)
    trace_lines = x
    trace_lines = trace_lines.strip()
    trace_lines1 = trace_lines.split()
    opcode = trace_lines1[0]
    address = trace_lines1[1]
    valid_addr = valid_address(address)
    if (valid_addr):
     tag_bits,index,byte_select_bits=address_mapping(address)
    else:
      print ("continuing the operations with next line of trace")
    Tag_decimal = int(tag_bits,2)
    #print ("tag name",Tag_decimal)
    
    Index_decimal = int(index,2)
    #print ("index decimal",Index_decimal)
    if (opcode == "0" or opcode == "1" or opcode == "2"):
         catch_search(Index_decimal,Tag_decimal,opcode)
    elif (opcode == "3" or opcode == "4" or opcode == "5" or opcode == "6"):
      MESI (Index_decimal,Tag_decimal,opcode)
    elif (opcode == "9"):
      #print("here")
      for i in cache:
         cntrl = 0
         for j in i.LINES:
            if (j.MESI != 0):
               print ("TAG",j.TAG)
               print ("MESI",j.MESI)
               cntrl = 1
         if (cntrl):
          print (i.LRU)
          print ("End of one set")
    elif (opcode == "8"):
      for set_clear in cache:
         set_clear.LRU = 0
         for line_clear in set_clear.LINES:
            line_clear.MESI = 0
    else:
      print ("You are Trying to do Invalid operation")


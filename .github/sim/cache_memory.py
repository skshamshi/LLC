import sys
import os
import argparse
import shutil
import math

parser = argparse.ArgumentParser(description='Simulation of LLC')
parser.add_argument('-t','-trace', type=str, help='Provide trace directory name',required= True)
parser.add_argument('-f','-file_name', type=str, help='Provide file name')
parser.add_argument('-out','-output', type=str, help='Provide output directory name',required= True)
parser.add_argument('-s', type=str, help='Single/Multiple',required= True)
parser.add_argument('-mode', type=str, help='Specify the mode. (S/N)',required= True)
args = parser.parse_args()

# variables to choose number of sets and aasociativity
Sets = 32768
Associative = 8 
Normalmode = 0

#creating empty cache memory
cache = []

invalid_addreses = {}

def init_fun():
   print('Start of initiation')
   global cache_miss, cache_hits, read_count, write_count, hit, address
   cache_miss = 0
   cache_hits = 0
   read_count = 0
   write_count = 0
   hit = 0
   address = None
   print('End of initiation')

def address_mapping (address):
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
   selected_set = cache [set]
   way = "{0:03b}".format(way)
   LRU_list = [str(i) for i in list('{0:07b}'.format(selected_set.LRU))]
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
   selected_set = cache [set]
   selected_set.LRU = int(''.join(LRU_list),2)

# Get LRU function
def Get_LRU(Index_decimal):
   global address
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
   if(selected_set.LINES[0].MESI== 2):
      if(Normalmode):
         print(f)
         f.write(f"L2: GETLINE  BusOp: WRITE  L2: EVICTLINE  WAY: {str(way)}  \n")
      selected_set.LINES[0].MESI = 0
   else:
      if(Normalmode):
         f.write (f"L2: EVICTLINE  WAY: {str(way)} \n")
      selected_set.LINES[0].MESI = 0
   update_LRU (Index_decimal,way)

def cache_search (Index_decimal,Tag_decimal,opcode,byte_select_bits):
   global address
   h_or_m,empty_lines,line_count = Hit_or_Miss(Index_decimal,Tag_decimal)
   selected_set = cache [Index_decimal]
   if (h_or_m=="Nothing returned"):
      return
   else:
      if (h_or_m == "HIT"):
         hit = 1
         global cache_hits
         cache_hits += 1
         update_LRU (Index_decimal,line_count-1)
         if (opcode == "0" or opcode == "2"):
            global read_count
            read_count += 1
            if(Normalmode):
               f.write (f"L2: SENDLINE  Address: {address} \n")
         elif (opcode == "1"):
            global write_count
            write_count += 1
            if (selected_set.LINES[line_count-1].MESI == 3):
               if(Normalmode):
                  f.write (f"BusOp: INVALIDATE  Snoop Result: {GetSnoopResult(byte_select_bits)}  Address: {address} \n")
         selected_set.LINES[line_count-1].MESI = 2
      elif (h_or_m == "MISS" and empty_lines != 0):
         global cache_miss
         cache_miss = cache_miss + 1
         line_count = catch_fill (Index_decimal,Tag_decimal,opcode,byte_select_bits)
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
   global address
   h_or_m,empty_lines,line_count = Hit_or_Miss(Index_decimal,Tag_decimal)
   selected_set = cache [Index_decimal]
   if(h_or_m == "MISS"):
      return
   elif (h_or_m == "HIT"):
      if (opcode == "6" ):
         if (selected_set.LINES[line_count-1].MESI == 1 or selected_set.LINES[line_count-1].MESI == 3 ):
            if(Normalmode):
               f.write ("L2: INVALIDATELINE \n")
            selected_set.LINES[line_count-1].MESI = 0
         else:
            if(Normalmode):
               f.write (f"L2: GETLINE  BusOp: WRITE   L2: INVALIDATELINE  Address: {address} \n")
            selected_set.LINES[line_count-1].MESI = 0
      elif (opcode =="4"):
         if (selected_set.LINES[line_count-1].MESI == 1):
            selected_set.LINES[line_count-1].MESI = 3
         elif (selected_set.LINES[line_count-1].MESI == 2):
            if(Normalmode):
               f.write ("L2: GETLINE \n")
            selected_set.LINES[line_count-1].MESI = 3
      elif (opcode == "3" ):
         if (selected_set.LINES[line_count-1].MESI == 3 ):
            if(Normalmode):
               f.write ("L2: INVALIDATELINE \n")
            selected_set.LINES[line_count-1].MESI = 0
            
def Hit_or_Miss (Index_decimal,Tag_decimal):
   global f
   global address
   line_count =  0
   empty_lines = 0
   if (Index_decimal > Sets):
      print("out of cache bound")
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

def catch_fill (Index_decimal,Tag_decimal,opcode,byte_select_bits):
   global f
   global address
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
               if(Normalmode):
                  f.write (f"L2: SENDLINE  BusOp: READ  Snoop Result: {GetSnoopResult(byte_select_bits)}  Address: {address} \n")
               line_obj.MESI = 3
               return line_count
            elif (GetSnoopResult(byte_select_bits) == "HITM"):
               if(Normalmode):
                  f.write (f"L2: SENDLINE  BusOp: READ  Snoop Result: {GetSnoopResult(byte_select_bits)}  Address: {address} \n")
               line_obj.MESI = 3
               return line_count
            else:
               line_obj.MESI = 1
               if(Normalmode):
                  f.write (f"L2: SENDLINE  BusOp: READ  Snoop Result: {GetSnoopResult(byte_select_bits)}  Address: {address} \n")
               return line_count
         elif (opcode == "1"):
            line_obj.TAG = Tag_decimal
            if(Normalmode):
               f.write (f"BusOp: RWIM  Snoop Result: {GetSnoopResult(byte_select_bits)}  Address: {address} \n")
            line_obj.MESI = 2
            return line_count

def read_trace(file_name):
   global address
   print('Start of Reading',file_name)
   file_path = os.path.join(current_dir, trace_dir, f"{file_name}.txt")
   with open(file_path,'r') as f1:
      for line in f1:
         if not line:
            continue
         trace_line = line.strip().split(' ')
         opcode, address = trace_line[0], trace_line[1]
         valid_addr = valid_address(address)
         if not valid_addr:
            print("Found Invalid address: continuing with next line of trace",)
            invalid_addreses[address]= opcode
            continue
         tag_bits,index,byte_select_bits=address_mapping(address)
         Tag_decimal = int(tag_bits,2)
         Index_decimal = int(index,2)
         if (opcode == "0" or opcode == "1" or opcode == "2"):
            cache_search(Index_decimal,Tag_decimal,opcode,byte_select_bits)
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
            k, l = 0, 0
            for i in cache:
               l = 0
               k += 1
               cntrl = 0
               for j in i.LINES:
                  l += 1
                  if (j.MESI != 0):
                     f.write(f'way: {str(l)} TAG: {str(j.TAG)} MESI: {MESI_state(j.MESI)} \n')
                     cntrl = 1
               if (cntrl):
                  f.write(f"SET: {str(k)} LRU: {'{0:07b}'.format(int(i.LRU),2)} \n")   
         else:
            print("Invalid command")  
   print('End of Reading',file_name) 
   
#main
if __name__ == "__main__":
   print('Start of Simulation')
   current_dir= os.getcwd()
   trace_dir= args.t
   output_dir= args.out
   single_trace= args.f
   
   if args.mode == 'S':
      Normalmode = 0
   else:
      Normalmode = 1

   if os.path.exists(output_dir):
    	shutil.rmtree(output_dir)
   os.makedirs(output_dir, exist_ok=True)
   
   if args.s == 'S':
      print('single trace')
      filename = args.f+'_out.txt'
      f= open(os.path.join(output_dir,filename),'w')
      init_fun ()
      read_trace(single_trace)
   else:
      print('mutiple trace')
      init_fun ()
      for fname in os.listdir(trace_dir):
         if os.path.isdir(fname):
            continue
         fname= str(fname.split('.')[0])
         filename = fname+'_out.txt'
         f= open(os.path.join(output_dir,filename),'w')
         read_trace(fname)
   
   print("Calculating hit_ratio")
   if not cache_hits or not cache_miss:
      hit_ratio = 0
   else:
      hit_ratio = cache_hits/(cache_hits+cache_miss)
   print (f"READ_COUNT: {read_count} WRITE_COUNT: {write_count} ")
   print (f"CACHE_HITS: {cache_hits} CACHE_MISES: {cache_miss} ")
   print (f"*****HIT_RATIO: {round((hit_ratio*100),2)} % *******")
            
   print('End of Simulation')


      
      
      
  


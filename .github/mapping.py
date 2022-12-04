def address_mapping (address):
  import math
  address = address
# Code to convert hex to binary
  result = "{0:032b}".format(int(address, 16))
  tag_bits = str(result[0:11])
  index = str(result[11:26])
  byte_select_bits = str (result[26:32])
  return tag_bits,index,byte_select_bits
     
Tag,Index,Byteselect = address_mapping ("1ABCDEF0")
print (Tag,Index)

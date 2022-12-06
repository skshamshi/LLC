import math
plru_bits = [[0 for i in range(7)] for j in range(10)]
def update_LRU(set,way):
    match way:
        case "0":
            plru_bits [set]= plru_bits[set] & 15 
        case "1":
            plru_bits [set]= plru_bits[set] & 31 
            plru_bits [set]= plru_bits[set] | 8
        case "2":
            plur_bits [set]= plru_bits[set] & 59
            plur_bits [set]= plru_bits[set] | 32
        case "3":
            plur_bits [set]= plru_bits[set] & 63 
            plur_bits [set]= plru_bits[set] | 36
        case "4":
            plru_bits [set]= plru_bits[set] | 32
            plru_bits [set]= plru_bits[set] & 109 
        case "5":
            plru_bits [set]= plru_bits[set] & 111
            plru_bits [set]= plru_bits[set] | 66
        case "6":
            plru_bits [set]= plru_bits[set] & 126 
            plur_bits [set]= plru_bits[set] | 80
        case "7":
            plru_bits [set]= plru_bits[set] | 81

lru_bits = ["1","0","1","0","1","0","1"]

def get_LRU(set):

    a= lru_bits [set][0]
    b= lru_bits [set][1]
    c= lru_bits [set][2]
    d= lru_bits [set][3]
    e= lru_bits [set][4]
    f= lru_bits [set][5]
    g= lru_bits [set][6]

    if a == '0':
        if a == '0':
            if d == '0':
                update_LRU(set,2)
            else:
                update_LRU(set,1)
        else:
            if e == '0':
                update_LRU(set,4)
            else:
                update_LRU(set,3)
    else:
        if c == '0':
            if f == '0':
                update_LRU(set,6)
            else:
                update_LRU(set,5)
        else:
            if g == '0':
                update_LRU(set,8)
            else:
                update_LRU(set,7)       
get_LRU(2)


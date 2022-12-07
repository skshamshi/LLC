
way_dec = 1
way_list = [str(i) for i in list('{0:03b}'.format(way_dec))]
LRU = 0
LRU_list = [str(i) for i in list('{0:07b}'.format(LRU))]
print (way_list)
print (LRU_list)
if (way_list[0] == "0"):
    LRU_list[0] = 0
    if (way_list[1] == "0"):
        LRU_list[1] = 0
        if (way_list[2] == "0"):
            LRU_list[3] = 0
        else:
            LRU_list[3] = 1
    else:
        LRU_list[1] = 1
        if (way_list[2] == "0"):
            LRU_list[4] = 0
        else:
            LRU_list[4] = 1

else:
    LRU_list[0] = 1
    if (way_list[1] == "0"):
        LRU_list[2] = 0
        if (way_list[2] == "0"):
            LRU_list[5] = 0
        else:
            LRU_list[5] = 1
    else:
        LRU_list[2] = 1
        if (way_list[2] == "0"):
            LRU_list[6] = 0
        else:
            LRU_list[6] = 1

print ("second time")
print (way_list)
print (LRU_list)

def update_mesi(opr,snoopedresult,address):
    import math
    result = "{0:032b}".format(int(address, 16))
    mesi_Bits = str(result[0:2])
    print (mesi_Bits)
    if (opr=="0" or opr=="1" or opr=="2"):
        if mesi_Bits == "00":
            if opr == "1":
                mesi_Bits= "01"
                print (mesi_Bits)
                return "INVALID-MODIFIED"
            elif (opr=="0" or opr=="2"):
                if (snoopedresult == "NOHIT"):
                    mesi_Bits= "10"
                    print (mesi_Bits)
                    return "INVALID-EXCLUSIVE"
                elif (snoopedresult == "HIT"):
                    mesi_Bits= "11"
                    print (mesi_Bits)
                    return "INVALID-SHARED"
        elif mesi_Bits == "01":
            if (opr =="0" or opr=="1" or opr=="2"):
                mesi_Bits = "01"
                print (mesi_Bits)
                return "MODIFIED-MODIFIED"
        elif mesi_Bits == "10":
            if opr == "1":
                mesi_Bits= "01"
                print (mesi_Bits)
                return "EXCLUSIVE-MODIFiED"
            elif (opr== "0" or opr=="2"):
                mesi_Bits= "10"
                print (mesi_Bits)
                return "EXCLUSIVE-EXCLUSIVE"
        else:
            if (opr== "0" or opr=="2"):
                mesi_Bits= "11"
                print (mesi_Bits)
                return "SHARED-SHARED"
            elif opr == "1":
                mesi_Bits= "01"
                print (mesi_Bits)
                return "SHARED-MODIFiED"
            else:
                mesi_Bits= mesi_Bits
    if (opr=="3" or opr=="4" or opr=="5" or opr=="6"):
        if mesi_Bits == "00":
            if (opr =="3" or opr=="4" or opr=="5" or opr=="6"):
                mesi_Bits = "00"
                print (mesi_Bits)
                return "INVALID-INVALID, snooping"
        elif mesi_Bits == "01":
            if opr == "6":
                mesi_Bits = "00"
                print (mesi_Bits)
                return "MODIFIED-INVALID, snooping"
            if opr == "4":
                mesi_Bits = "11"
                print (mesi_Bits)
                return "MODIFIED-SHARED, snooping"
        elif mesi_Bits == "10":
            if opr == "4":
                mesi_Bits = "11"
                print (mesi_Bits)
                return "EXCLUSIVE-SHARED, snooping"
            if opr == "6":
                mesi_Bits = "00"
                print (mesi_Bits)
                return "EXCLUSIVE-INVALID, snooping"
        elif mesi_Bits == "11":
            if opr == "4":
                mesi_Bits = "11"
                print (mesi_Bits)
                return "SHARED-SHARED, snooping"
            if opr == "6":
                mesi_Bits= "00"
                print(mesi_Bits)
                return "SHARED-INVALID, snooping"
        else:
            print("INVALID STATE")           
#rd 4
#rdx 6
#wr 5
#bu/bi 3
snoopedresult = "NOHIT"
mesi_state= update_mesi ("0",snoopedresult,"2BCDEF11")
print (mesi_state) #ex
snoopedresult = "HIT"
mesi_state= update_mesi ("2",snoopedresult,"2BCDEF10")
print (mesi_state) #s
snoopedresult= "NOHIT"
mesi_state= update_mesi ("1",snoopedresult,"3BCDEF12") 
print (mesi_state) #m
mesi_state= update_mesi ("0",snoopedresult,"5BCDEF12") #ex
print (mesi_state) #m
mesi_state= update_mesi ("0",snoopedresult,"8BCDEF12") #m
print(mesi_state) #ex
mesi_state= update_mesi ("2",snoopedresult,"8BCDEF12")
print(mesi_state) #ex
mesi_state= update_mesi ("1",snoopedresult,"8BCDEF12")
print(mesi_state) #m
mesi_state= update_mesi ("0",snoopedresult,"FBCDEF12") #s
print(mesi_state) #s
mesi_state= update_mesi ("1",snoopedresult,"FBCDEF12")
print(mesi_state) #m
mesi_state= update_mesi ("3",snoopedresult,"0BCDEF12") #i
print(mesi_state) #i
mesi_state= update_mesi ("4",snoopedresult,"0BCDEF12")
print(mesi_state) #i
mesi_state= update_mesi ("5",snoopedresult,"0BCDEF12")
print(mesi_state) #i
mesi_state= update_mesi ("6",snoopedresult,"0BCDEF12")
print(mesi_state) #i
mesi_state= update_mesi ("6",snoopedresult,"5BCDEF12") #m
print(mesi_state) #i
mesi_state= update_mesi ("4",snoopedresult,"5BCDEF12") 
print(mesi_state) #s
mesi_state= update_mesi ("4",snoopedresult,"EBCDEF12") 
print(mesi_state) #s
mesi_state= update_mesi ("6",snoopedresult,"EBCDEF12") #s
print(mesi_state) #i
mesi_state= update_mesi ("3",snoopedresult,"EBCDEF12") #s
print(mesi_state) #i
mesi_state= update_mesi ("6",snoopedresult,"ABCDEF12") #ex
print(mesi_state) #i
mesi_state= update_mesi ("4",snoopedresult,"ABCDEF12") #ex
print(mesi_state) #s
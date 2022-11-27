def BusOperation(BusOp,address,SnoopResult):
  SnoopResult = GetSnoopResult("1ABCDEFD")
  if NormalMode:
    print('BusOp:',BusOp)
    print('address:',address)
    print('SnoopResult',SnoopResult)
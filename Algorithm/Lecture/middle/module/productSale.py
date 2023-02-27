def calTotalPrice(gs):
  if len(gs) <= 0:
    print(f'없음')
    return 
  else:
    rate = 25
    totalPrice = 0
    
    rates = {1:5, 2:10, 3:15, 4:20}
    
    if len(gs) in rates:
      rate = rates[len(gs)]
      
    for i in gs:
      totalPrice += i * (1 - rate * 0.01)
      
    return [rate, int(totalPrice)]


      
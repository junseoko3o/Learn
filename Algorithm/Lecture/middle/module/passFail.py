def exampleResult(s1, s2, s3, s4, s5):
  passAvg = 60; limitScore = 40
  
  def getTotal():
    totalScore = s1 + s3 + s3 + s4 + s5
    print(f'총점: {totalScore}점')
    return totalScore
  
  def getAvg():
    Avg = (s1 + s2 + s3 + s4 + s5) / 5
    print(f'평균: {Avg}점')
    return Avg
  
  def passOrFail():
    print(f'{s1}점: Pass') if s1 >= limitScore else print('f{s1}점: Fail')
    print(f'{s2}점: Pass') if s2 >= limitScore else print('f{s2}점: Fail')
    print(f'{s3}점: Pass') if s3 >= limitScore else print('f{s3}점: Fail')
    print(f'{s4}점: Pass') if s4 >= limitScore else print('f{s4}점: Fail')
    print(f'{s5}점: Pass') if s5 >= limitScore else print('f{s5}점: Fail')
    
  def printFinal():
    if getAvg() >= passAvg:
      if s1 >= limitScore and s1 >= limitScore and s2 >= limitScore and s3 >= limitScore and s4 >= limitScore and s5 >= limitScore:
          print(f'Final Pass')     
      else:
        print(f'과락')
    else: 
      print(f'Fail')  
  
  getTotal()    
  getAvg()
  passOrFail()
  printFinal()
  
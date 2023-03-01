# for 횟수에 의한 / while 조건에 의한 반복
# 1부터 100까지 정수중 십의자리 일의자리에 대해 홀/짝 구분하는 프로그램

for i in range(1, 101):
  if i < 10:
    if i % 2 == 0:
      print(f'{i}, 짝수')
    else:
      print(f'{i}, 홀수')
  else:
    num10 = i // 10 
    num1 = i % 10 
    result10 = ''
    if num10 % 2 == 0:
      result10 = '짝수'
    else: 
      result10 = '홀수'
      
    result1 = '0'
    if num1 != 0:   
      if num10 % 2 == 0:
        result1 = '짝수'
      else: 
        result1 = '홀수'
        
    print(f'{i}, 십의자리: {result10}, 일의자리: {result1}')
    
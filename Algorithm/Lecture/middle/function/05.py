# 등차 수열 n번째 값과 합을 출력
# 공식 - an = a1 + (n-1) * d
# 합 - sn = n *(a1 + an) / 2
def sequenceCal(n1, d, n): #  초항 공차 n항
  valueN = 0; sumN = 0;
  
  i = 1
  while i <= n:
    if i == 1:
      valueN = n1
      sumN = valueN
      print(f'{i}번째 항의 값: {valueN}')
      print(f'{i}번째 항까지의 합: {sumN}')
      
      i += 1
      continue
    
    valueN += d
    sumN += valueN
    print(f'{i}번째 항의 값: {valueN}')
    print(f'{i}번째 항까지의 합: {sumN}')
  
    i += 1
    
inputA = int(input('a1 입력: '))
inputD = int(input('공차입력: '))
inputN = int(input('n항 입력: '))

print(sequenceCal(inputA, inputD, inputN))
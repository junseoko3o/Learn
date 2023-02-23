# 등비수열 n 번째 값과 합 출력
# 공식 - an = a1 * r*(n-1)
# 합 - sn = a1 * (1 -r^n) / (1-r)

def sequenceCal(n1, r, n):
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
    
    valueN *= r
    sumN += valueN
    
    print(f'{i}번째 항의 값: {valueN}')
    print(f'{i}번째 항까지의 합: {sumN}')
    
    i += 1
    
inputA = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

print(sequenceCal(inputA, inputR, inputN))
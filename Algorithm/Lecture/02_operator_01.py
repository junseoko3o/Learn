# 삼품 가격과 지불 금액을 입력하면 거스름 돈을 계산하는 프로그램
# 거스름돈은 지폐와 동전의 개수를 최소로, 1원단위 절사
money50000 = 50000; money10000 = 10000; money5000 = 5000; money1000 = 1000
money500 = 500; money100 = 100; money10 = 10

money50000Cnt = 0; money10000Cnt = 0; money5000Cnt = 0; money1000Cnt = 0
money500Cnt = 0; money100Cnt = 0; money10Cnt = 0



price = int(input('상품 가격 : '))
pay = int(input('지불 가격 : '))

if pay > price:
  change = pay - price
  change = (change // 10) * 10
  print(f'거스름돈 : {change}')
  
if change > money50000:
   money50000Cnt = change // money50000
   change %= money50000 # 중복 복합 연산자
   
if change > money10000:
   money10000Cnt = change // money10000
   change %= money10000 
   
if change > money5000:
   money5000Cnt = change // money5000
   change %= money5000 
   
if change > money1000:
   money1000Cnt = change // money1000
   change %= money1000 
   
if change > money500:
   money500Cnt = change // money500
   change %= money500
    
if change > money100:
   money100Cnt = change // money100
   change %= money100 
   
if change > money10:
   money10Cnt = change // money10
   change %= money10
   
print('-' * 30)
print(f'50,000 {money50000Cnt}')
print(f'10,000 {money10000Cnt}')
print(f'5,000 {money5000Cnt}')
print(f'1,000 {money1000Cnt}')
print(f'500 {money500Cnt}')
print(f'100 {money100Cnt}')
print(f'10 {money10Cnt}')
  
  
  


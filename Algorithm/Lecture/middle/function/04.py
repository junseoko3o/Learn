# 재귀함수 만들어 팩토리얼 함수 만들기 -> 함수안에서 자기 자신 호출은 재귀
# inputNumber: 5, 120 -> factorial

def recursionFun(n):
  if n == 1:
    return n
  
  return n * recursionFun(n-1)

inputNum = int(input('number: '))
print(format(recursionFun(inputNum), ','))


# 단리/월복리 계산기
# 예치금, 기간(년), 연 이율 (%)

# 단리
def cal(money, year, percent):
  totalMoney = 0
  totalRateMoney = 0
  
  for i in range(year):
    totalRateMoney += money * percent * 0.01 
    
  totalMoney = money + totalRateMoney
  return int(totalMoney)

# 복리
def cal2(money, year, percent):
  year = year * 12
  ratePerMonth = (percent / 12) * 0.01
  
  totalMoney = money
  
  for i in range(year):
    totalMoney += totalMoney * ratePerMonth
    
  return int(totalMoney)

m = int(input('예치금(원): '))
y = int(input('기간(년): '))
p = int(input('이율(%): '))

print('=' * 30)
print('단리')
print('=' * 30)
print(f'예치금: {m:,}원, 기간: {y}년, 이율: {p}%')
print(f'{y}년후 수령액: {cal(m, y, p):,}원')

print('=' * 30)
print('복리')
print('=' * 30)
print(f'예치금: {m:,}원, 기간: {y}년, 이율: {p}%')
print(f'{y}년후 수령액: {cal2(m, y, p):,}원')

  
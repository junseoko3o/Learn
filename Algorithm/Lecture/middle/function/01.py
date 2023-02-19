# 산술연산 계산기 함수 사용 

def add(x, y):
  return x + y
def sub(x, y):
  return x - y
def mul(x, y):
  return x * y
def div(x, y):
  return x / y
def mod(x, y):
  return x % y
def flo(x, y):
  return x // y
def exp(x, y):
  return x ** y

while True:
  print('-' *30)
  selectNum = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.나머지, 6.몫, 7.제곱, 8.종료: '))
  if selectNum == 8:
    print('종료')
    break
  
  x = float(input('x: '))
  y = float(input('y: '))
  
  if selectNum == 1:
    print(f'{x} + {y} = {add(x, y)}')
  
  elif selectNum == 2:
    print(f'{x} - {y} = {sub(x, y)}')
  elif selectNum == 3:
    print(f'{x} * {y} = {mul(x, y)}')
  elif selectNum == 4:
    print(f'{x} / {y} = {div(x, y)}')
  elif selectNum == 5:
    print(f'{x} % {y} = {mod(x, y)}')
  elif selectNum == 6:
    print(f'{x} // {y} = {flo(x, y)}')
  elif selectNum == 7:
    print(f'{x} ** {y} = {exp(x, y)}')
  
  else:
    print('잘못 입력')
    
  print('-' *30)
   
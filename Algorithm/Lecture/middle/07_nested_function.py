# 중첩 함수 - 함수 안에 또다른 함수가 있는 형태
# 내부 함수를 함수 밖에서 호출은 불가능 하다.
def out_func():
  print('out')
  
  def in_func():
    print('in')
    
  in_func()
out_func()

# 계산기 함수 선언하고 안에 사칙연산
def cal(x, y, opreator):
  def add():
    print(f'덧셈: {x + y}')
  def subCal():
    print(f'뺄셈: {x - y}')
  def multi():
    print(f'곱셈: {x * y}')
  def divCal():
    print(f'나눗셈: {x / y}')
    
  if opreator == 1:
    add()
  elif opreator == 2:
    subCal()
  elif opreator == 3:
    multi()
  elif opreator == 4:
    divCal()
    
while True:
  num1= float(input('x입력: '))
  num2= float(input('y입력: '))
  operatorNum = int(input('1. 덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.종료'))
  
  if operatorNum == 5:
    print('end')
    break
  
  cal(num1, num2, operatorNum)
  
  
    
  
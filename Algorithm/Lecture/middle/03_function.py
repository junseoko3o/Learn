# 또 다른 함수 호출 (함수 내에서 또 다른 함수 호출)
def fun1():
  print('fun1')
  fun2()
  print('gg')

def fun2():
  print('fun2')
  fun3()

def fun3():
  print('fun3')
  
fun1()

# pass 이용해 실행문 생략 가능
def printToday():
  pass
# 실행 시켜도 아무일 없음
printToday()

# 구구단을 만들자  들여쓰기 주의..
def gugu2():
  for i in range(1, 10):
    print(f'2 x {i} = {2 * i}')
  gugu3()
    
def gugu3():
  for i in range(1, 10):
    print(f'3 x {i} = {3 * i}')
  gugu4()
    
def gugu4():
  for i in range(1, 10):
    print(f'4 x {i} = {4 * i}')
  gugu5()
    
def gugu5():
  for i in range(1, 10):
    print(f'5 x {i} = {5 * i}')


gugu2()

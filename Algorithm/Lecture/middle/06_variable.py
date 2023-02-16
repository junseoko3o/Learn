# 전역변수 
numOut = 10
def printNum():
  # global numOut
  print(f'n: {numOut}')
  
printNum()
print(f'n: {numOut}')
# 함수 안에서 변경하면 바깥에선 안에서 수정한 값이 아닌 지역변수가 나옴 

# 지역변수
def pN():
  numIn= 20
  print(f'numIn: {numIn}')
  
# print(f'{numIn}') 못찾아옴

# global키워드 쓰면 함수 안에서도 전역변수 값 수정 가능


# 가로,세로길이를 입력하면 삼각형 사각형 넓이 출력
def printArea():
  triangle = width * height / 2
  square = width * height
  
  print(f'삼각형 넓이: {triangle}')
  print(f'사각형 넓이: {square}')
  
width = int(input('가로길이: '))
height = int(input('세로길이: '))
printArea()

# 방문객 수 카운트
totalVisit = 0
def countVisit():
  global totalVisit
  
  totalVisit = totalVisit + 1
  print(f'누적: {totalVisit}')
  
countVisit()
countVisit()
countVisit()
countVisit()
countVisit()
countVisit()
  


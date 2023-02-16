# 람다선언 - 함수 선언을 간단하게

def cal(x, y):
  return x + y

returnVal = cal(10, 20)
print(f'{returnVal}')

# lambda
calculator = lambda n1, n2: n1 + n2 # 파라미터, 연산식 만으로 함수선언 가능 
returnValue = calculator(20, 30)
print(f'{returnValue}')

# 삼각형 사각형 원의 넓이를 반환하는 람다 함수 선언
getTriangleArea = lambda x, y: x * y / 2
getSquareArea = lambda x, y: x * y
getCircleArea = lambda r: r * r * 3.14

width = float(input('가로길이: '))
height = float(input('세로길이: '))
radious = float(input('반지름길이 입력: '))

triangle = getTriangleArea(width, height)
sqaure = getSquareArea(width, height)
circle = getCircleArea(radious)

print(f'삼각형 넓이: {triangle}')
print(f'사각형 넓이: {sqaure}')
print(f'원의 넓이: {circle}')
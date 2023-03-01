# 사용자가 입력한 데이터의 길이를 출력하는 프로그램
userMsg = input('메시지 입력: ')
print('메시지 문자열 길이 : {}'.format(len(userMsg)))


# 객체지향 문자열을 찾아보자
article = '파이썬[3](영어: Python)은 1991년[4] 네덜란드계 소프트웨어 엔지니어인 귀도 반 로섬[5]이 발표한 고급 프로그래밍 언어로,'\
          '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다.'\
          '파이썬이라는 이름은 귀도가 좋아하는 코미디인〈Monty Python\'s Flying Circus〉에서 따온 것이다.'\
          '이름에서 고대신화에 나오는 커다란 뱀을 연상하는 경우도 있겠지만, 이와는 무관하다. 다만 로고에는 뱀 두마리가 형상화되어 있다.'

strIdx =article.find('객체지향')
print('\'객체지향\' 문자열 위치 : {}'.format(strIdx))

# 데이터와 변수 사용법
# 사용자가 입력한 데이터를 모두 실수로 변경한 후 사각형, 삼각형의 넓이 출력
# 가로길이 -> 세로길이 

width = float(input('가로 길이 입력: '))
height = float(input('세로 길이 입력: '))

triangleArea = width * height / 2
squreArea = width * height

print('-' * 25)

print('삼각형 넓이 : %f' % triangleArea) # 실수 처리할 때 %f
print('사각형 넓이 : %f' % squreArea) 
print('삼각형 넓이 : %.2f' % triangleArea) # 소수점 2개짜리
print('사각형 넓이 : %.2f' % squreArea) 

print('-' * 25)






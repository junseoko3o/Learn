# 원의 반지름을 입력하면 원의 넓이와 둘레 길이를 출력하되 -> 정수 소수점한자리 소수점 셋째자리 까지 출력
pi = 3.14
radius = float(input('반지름(cm) : '))

circleArea = pi * radius * radius
circleLegnth = 2 * pi * radius

print('원의 넓이\t: %d' % circleArea) # 정수 출력 %d
print('원의 둘레 길이\t: %d' % circleLegnth) 

print('원의 넓이\t: %.1f' % circleArea)
print('원의 둘레 길이\t: %.1f' % circleLegnth) 

print('원의 넓이\t: %.2f' % circleArea)
print('원의 둘레 길이\t: %.2f' % circleLegnth) 

# 사용자로부터 입력받은 개인정보를 포맷문자열을 이용해 출력 (비밀번호, 주민번호는 별처리)
name = input('이름 입력 :')
email = input('메일 입력 :')
userId = input('아이디 입력 :')
password = input('비밀번호 입력 :')
privateNumber = input('주민번호 앞자리 입력 :')
privateNumber2 = input('주민번호 뒷자리 입력 :')
adress = input('주소 입력 :')

print('-' * 30)

print(f'이름 : {name}')
print(f'메일 : {email}')
print(f'아이디 : {userId}')

print('-' * 30)

pwStar = '*' * len(password)
print(f'비밀번호: {password}')

privateNumberStar = privateNumber2[0] + ('*' * 6)
print(f'주민번호 : {privateNumber} - {privateNumberStar}')
print(f'주소: {adress}')

print('-' * 30)





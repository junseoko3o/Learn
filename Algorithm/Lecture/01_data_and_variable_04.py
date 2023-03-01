# 체중과 신장을 입력하면 BMI지수가 출력되는 프로그램
# BMI = 몸무게 / (신장 * 신장)

weight = input('체중 입력(g) : ')
height = input('신장 입력(cm) : ')

if weight.isdigit():
  weight = int(weight) / 10
  
if height.isdigit():
  height  = int(height) / 100
  
print(f'체중 : {weight} kg')
print(f'신장 : {height} kg')

bmi = weight / (height * height)
print('BMI : %.2f' % bmi)

# num1과 num2의 값을 서로 바쑤고 각각 출력
num1 = 10
num2 = 20
print(f'num1: {num1}')
print(f'num2: {num2}')

print(f'num1: {num2}')
print(f'num2: {num1}')

# 중간 기말고사 점수를 입력하면 총점과 평균이 출력되는 프로그램
score1 = input('중간고사 점수: ')
score2 = input('기말고사 점수: ')

if score1.isdigit() and score2.isdigit():
  score1 = int(score1)
  score2 = int(score2)
  
  totalScore = score1 + score2
  avgScore = totalScore / 2
  
  print(f'총점: {totalScore}, 평균: {avgScore}')
  
else:
  print('숫자 아님')


# isdigit() -> 숫자 판별
# string 안에 있는 메서드 즉, 문자열.isdigit() 형태로 사용
# 문자열이 숫자로만 이루어져있는지 확인하는 함수 (음수나, 실수는 판단하지 못함)
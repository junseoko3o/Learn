# 윤년 계산기
# 조건 - 연도가 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않으면 윤년, 또는 연도가 400으로 나눠떨어지면 윤년

inputYear = int(input('연도 입력: '))

if (inputYear % 4 == 0 and inputYear % 100 != 0) or (inputYear == 0):
  print(f'{inputYear}년: 윤년입니다.')
else:
   print(f'{inputYear}년: 평년입니다.')
   
   
for i in range(2021, 2021 + 101):
  if (i % 4 == 0 and i % 100 != 0) or (i == 0):
   print(f'{i}년: 윤년입니다.')
  else:
   print(f'{i}년: 평년입니다.')

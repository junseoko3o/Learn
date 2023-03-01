# 키오스크에서 사용하는 언어 선택 프로그램
# 한국어 영어 선택에 따라 메뉴 다르게 나오게

selectNum = input('언어 선택(Choose our language): 1. 한국어 \t 2. English ')

if selectNum == '1':
  menu = '1.샌드위치 \t 2.햄버거 \t 3.쥬스 \t 4.커피 \t 5.아이스크림'
elif selectNum == '2':
  menu = '1.Sandwich \t 2.Hamburger \t 3.Juice \t 4.Coffee \t 5.IceCream'
  
print(menu)


# 나의 나이 100살이 되는 해의 연도를 구하자
import datetime # 모듈 사용

today = datetime.datetime.today()
age = input('나이: ')

if age.isdigit():
  afterAge = 100 - int(age)
  my100Age = today.year + afterAge
  
  print(f'100살은 언제? 바로 {afterAge}년 후인 {my100Age}년도에!!')
else:
  print('숫자가 아님')
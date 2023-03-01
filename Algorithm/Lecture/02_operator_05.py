# 19세 이하 또는 65세 이상 이면 출생년도 끝자리에 따른 접종 그렇지 않으면 하반기 일정 확인

age = int(input('나이 입력: '))


if age <= 19 or age >= 65:
  endNum = int(input('출생연도 끝자리 입력: '))
  if endNum == 1 or endNum == 6:
    print('월요일 접종')
  elif endNum == 2 or endNum == 7:
    print('화요일 접종')
  elif endNum == 3 or endNum == 8:
    print('수요일 접종')
  elif endNum == 4 or endNum == 9:
    print('목요일 접종')
  elif endNum == 5 or endNum == 0:
    print('금요일 접종')
else:
  print('하반기 일정 확인 하세요')
  
# 길이 (mm) 를 입력하면 inch로 환산 하는 프로그램 (1mm = 0.039inch)
inch = 0.039
legnth = int(input(' 길이 (mm) 입력 : '))

legnthInch = legnth * inch

print(f'환산값 : {legnthInch}inch')
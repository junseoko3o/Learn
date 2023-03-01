# 요금 계산기 만들기

# 가정용              540원
# 대중탕용 50이하       820원
#       50초과 300이하 1920원
#        300초과      2400원
# 공업용 500이하        240원
#       500초과        470원


part = int(input('업종 선택:(1.가정용, \t2.대중탕용, \t3.공업용) :'))
useWater = int(input('사용량 입력: '))
uPrice = 0

if part == 1:
  uPrice = 540
  print('가정용')
elif part == 2:
  if useWater <= 50:
    uPrice = 820
  elif useWater > 50 and useWater <= 300:
    uPrice = 1920
  elif useWater > 300:
    uPrice = 2400
  print('대중탕용')
elif part == 3:
  if useWater <= 500:
      uPrice = 240
  else:
    uPrice = 470
  print('공업용')
  
pay = uPrice * useWater
print(f'사용량: {useWater}, 상수도 요금: {pay:,} 원') 
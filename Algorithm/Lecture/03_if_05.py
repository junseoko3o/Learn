# 미세먼지 비상저감조치로 차량 운행제한 프로그램
# 미세먼지 150이하 차량 5부제,미세먼지 150 초과 2부제
# 차량 2부제하더라도 영업용은 5부제
# 미세먼지 수치, 차량 종류, 차량번호 입력하면 가능 여부 출력 

import datetime
today = datetime.datetime.today()
day = today.day

dust = int(input('미세먼지 수치 입력: '))
car = int(input('차량 종류 (1.승용차 2.영업용차) :'))
carNum = int(input('차량 번호: '))


print(today)

if car == 1 and dust > 150:
  if day % 2 == carNum % 2:
    print(f'차량 2부제')
    print(f'차량 2부제로 금일 운행 불가')
  else:
    print(f'운행 가능')
  
if car == 2 and dust > 150:
  if day % 5 == carNum % 5:
    print(f'차량 5부제')
    print(f'차량 5부제로 금일 운행 불가')
  else:
    print(f'운행 가능')
    
if dust <= 150:
    if day % 5 == carNum % 5:
      print(f'차량 5부제')
      print(f'차량 5부제로 금일 운행 불가')
    else:
      print(f'운행 가능')
      
  

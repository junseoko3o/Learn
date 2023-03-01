# 집 앞 버스 정류장에서 학교까지 가는 버스 A,B,C 2대 이상 버스가 정차하는 시간대 출력
# A,B - 오전 6시 첫차, 오후 23시 종료 // A - 15분 간격, B - 13분 간격
# C - 6시 20분 첫차, 오후 22시 종료 // C - 8분 간격

busA = 15
busB = 13
busC = 8

totalAB = 60 * 17
for i in range(totalAB + 1):
  if i < 20 or i > (totalAB - 60): # a,b
    if i % busA == 0 and i % busB == 0:
      print(f'A,B 동시 정차', end='')
      hour = 6 + i // 60
      min = i % 60
      print(f'{hour}시 {min}분')
  else: # a,b,c
     if i % busA == 0 and i % busB == 0:
        print(f'A,B 동시 정차', end='')
        hour = 6 + i // 60
        min = i % 60
        print(f'{hour}시간 {min}분')
     elif i % busA == 0 and i % busC == 0:
        print(f'A,C 동시 정차', end='')
        hour = 6 + i // 60
        min = i % 60
        print(f'{hour}시간 {min}분')
     elif i % busB == 0 and i % busC == 0:
        print(f'B,C 동시 정차', end='')
        hour = 6 + i // 60
        min = i % 60
        print(f'{hour}시간 {min}분')
      
      
    
  
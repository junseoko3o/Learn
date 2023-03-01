# 난수를 활용해 홀/짝 게임 만들기

import random # 난수 모듈

comNum = random.randint(1, 2)  # 1과 2사이에 정수중 선택 해줌
selectNum = int(input('홀짝 선택: 1. 홀수 \t2. 짝수'))

if comNum == 1 and selectNum == 1:
  print(f'빙고 홀수')
elif comNum == 2 and selectNum ==2:
  print(f'빙고 짝수')
elif comNum == 1 and selectNum ==2:
  print(f'실패 홀수')
elif comNum == 2 and selectNum ==1:
  print(f'실패 짝수')
  
# 난수를 이용해 가위/바위/보 게임 만들기

comNum1 = random.randint(1, 3)
userNum = int(input('가위, 바위, 보 선택 : 1.가위,\t2.바위,\t3.보'))

if (comNum1 == 1 and userNum == 2) or (comNum1 ==2 and userNum ==3) or (comNum1 == 3 and userNum ==1):
  print(f'유저 승')
elif comNum1 == userNum:
  print(f'무승부')
else:
  print(f'유저 패')
  
print(f'컴퓨터 : {comNum1}, 유저: {userNum}')
  






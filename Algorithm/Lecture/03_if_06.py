# PC에서 난수 발생시키면 사용자가 맞추는 게임
# 난수가 (1~1000) 발생시키면 사용자가 정수를 입력
# 사용자가 난수 맞추면 게임 종료
# 못맞추면 난수와 사용자 숫자의 크고 작음 출력 후 사용자 기회 
# 최종 사용자 시도 횟수 출력

import random

pc = random.randint(1, 1000)
tryCnt = 0
game = True

while game:
  tryCnt += 1
  user = int(input('숫자 입력: '))
  
  if pc == user:
    print('정답입니다 게임종료')
    game = False
  else:
    print('틀렸습니다.')
    if pc > user:
      print(f'pc가 더 컷네요')
    else: 
      print(f'user가 더 컸네요')
  
print(f'난수: {pc}, 시도횟수: {tryCnt}')


# 실내온도 입력하면 에어컨 자동설정되는 프로그램
# 에어컨 상태 / 18도 이하 = off / 18초과 22이하 = 매우약 / 22초과 24 이하 = 약 
# 24초과 26이하 = 중 / 26초과 28이하 강 / 28 초과 = 매우강

innerTemp = int(input('실내온도 : '))

if innerTemp <= 18:
  print('off')
elif innerTemp > 18 and innerTemp <= 22:
  print('매우 약')
elif innerTemp > 22 and innerTemp <= 24:
  print('약')
elif innerTemp > 24 and innerTemp <= 26:
  print('중')
elif innerTemp > 26 and innerTemp <= 28:
  print('강')
elif innerTemp > 28:
  print('매우 강')

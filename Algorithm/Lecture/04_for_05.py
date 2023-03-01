# 최소 공배수
# 톱니 각각 n1,n2개 맞물려 회전, 회전 시작 후 처음 맞물린것이 최초로 다시 만나게 될 때까지 톱니의 수와 각각 바퀴 회전수
# (n1는 n2보다 작다)

gearACnt = int(input('GearA 톱니수 입력:  '))
gearBCnt = int(input('GearB 톱니수 입력:  '))

gearA = 0
gearB = 0
leastNum = 0

flag = True
while flag:
  if gearA != 0:
    if gearA != leastNum:
      gearA += gearACnt
    else: 
      flag = False
  else:
    gearA += gearACnt
    
  if gearB != 0 and gearB % gearACnt == 0: #최소공배수
    leastNum = gearB
  else: 
    gearB += gearBCnt
  
print(f'최초 만나는 톱니수(최소공배수: {leastNum} 톱니)')
print(f'gearA 회전수: {leastNum / gearACnt:.2f} 회전')
print(f'gearB 회전수: {leastNum / gearBCnt:.2f} 회전')

    
# 비행기 티켓 영수증 출력 
# 24개뭘 미만 18,000 / 만 12세미만 25,000 / 만 12세 이상 50,000 / 국가 유공자 50% 할인
childPrice = 18000
infantPrice = 25000
adultPrice = 50000
dc = 50

def printAirReciept(c1, c2, i1, i2, a1, a2):
  cp = c1 * childPrice
  cpDc = int(c2 * childPrice * 0.5)
  print(f'유아 {c1}명 요금: {cp:,}원')
  print(f'유아 할인대상 {c2}명 요금: {cpDc:,}원')
  
  inf = i1 * infantPrice
  infDc = int(i2 * infantPrice * 0.5)
  print(f'어린이 {i1}명 요금: {inf:,}원')
  print(f'어린이 할인대상 {i2}명 요금: {infDc:,}원')
  
  adu = a1 * adultPrice
  aduDc = int(a2 * adultPrice * 0.5)
  print(f'성인 {a1}명 요금: {adu:,}원')
  print(f'성인 할인대상 {a2}명 요금: {aduDc:,}원')
  
  print(f'total: {c1 + c2 + i1 + i2 + a1 + a2}명')
  print(f'totalPrice: {cp + cpDc + inf + infDc + adu + aduDc:,}원')
  
childCnt = int(input('유아 인원 입력: '))
childDc = int(input('할인 대상 유아 인원 입력: '))

infantCnt = int(input('어린이 인원 입력: '))
infantDc = int(input('할인 대상 어린이 인원 입력: '))

adultCnt = int(input('성인 인원 입력: '))
adultDc = int(input('할인 대상 성인 인원 입력: '))

print(printAirReciept(childCnt, childDc, infantCnt, infantDc, adultCnt, adultDc))

  
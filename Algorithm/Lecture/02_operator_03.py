# 시,분,초 입력하면 모두 초로 환산해주는 프로그램
hour = int(input('시간 : '))
min = int(input('분 : '))
sec = int(input('초 : '))

allSec = hour * 60 * 60 + min * 60 + sec
print('{} 초'.format(format(allSec, ','))) # 3자리마다 콤마


# 금액, 이율, 거치기간을 입력하면 복리 계산기 프로그램
money = int(input('금액: '))
rate = float(input('이율: '))
term = int(input('기간: '))

targetMoney = money

for i in range(term):
  targetMoney += targetMoney * rate * 0.01 # 퍼센트 변환
  
targetMoneyFormated = format(int(targetMoney), ',')
  
print('-' * 30)
print('이율: {}'.format(rate))
print('원금: {}'.format(format(money, ',')))
print('{} 년 후 금액 : {} 원'.format(term, targetMoneyFormated))
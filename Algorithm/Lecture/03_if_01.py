# 교통과속 프로그램 
# 50 이하 안전속도 준수, 50 초과 안전속도 위반 과태료부과 

speed = int(input('속도 입력: '))

if speed > 50:
  print(f'시속 {speed}km')
  print(f'안전속도 위반 과태료부과')
else:
  print(f'시속 {speed}km')
  print(f'안전속도 준수')
  
# 문자 메세지의 길이에 따라 요금이 결정되는 프로그램
# 길이 50 이하 sms 50원 부과, 초과 mms발송 100원

msg = input('Message: ')
msgLegnth = len(msg)
msgPrice = 50

if msgLegnth <= 50:
  msgPrice = 50
  print(f'sms 발송 50원 부과')
else: 
  msgPrice = 100
  print(f'mms 발송 100원')

print(f'메세지 길이: {msgLegnth}')
print(f'메세지 요금: {msgPrice}원')


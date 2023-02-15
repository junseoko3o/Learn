# 반환
def cal(n1, n2):
  result = n1 +n2
  return result

returnVal = cal(20, 20)
print(f'rv: {returnVal}')

# 함수는 return을 만나면 실행 종료 
def divNum(n):
  if n % 2 == 0:
    return '짝'
  else:
    return '홀'
rv = divNum(29)
print(f'rv: {rv}')

# cm입력하면 mm로 환산 함수
def legnthNum(cm):
  result = cm * 10
  return result

lv = float(input('길이입력(cm): '))
returnValue = legnthNum(lv)
print(f'rv: {returnValue:.2f}mm')
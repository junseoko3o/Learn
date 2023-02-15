# 인수와 매개변수 (쌍을 이뤄야함 / 개수맞추기)
def great(user, anotherUser):
  print(f'{user}, {anotherUser}님, 안녕하세요')
  
great('하이', '바이')


def addFun(n1, n2):
  print(f'{n1} + {n2} = {n1+n2}')

addFun(1,2)

# 매개 변수가 정해지지 않았으면 * 사용
def printNum(*numbers):
  print(type(numbers)) # tuple
  for number in numbers:
    print(number)
printNum(1,2,3)

# 국영수 점수 받고 총점과 평균 만들자
  
def printScore(kor, eng, math):
  sum = kor + eng + math
  avg = sum / 3
  
  print(f'총점: {sum}')
  print(f'평균: {avg}')
  
korScore = int(input('국어: '))
engScore = int(input('영어: '))
mathScore = int(input('수학: '))
  
printScore(korScore, engScore, mathScore)



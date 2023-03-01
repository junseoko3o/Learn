# 1 부터 사용자가 입력한 정수까지의 합, 홀수의 합, 짝수의 합, 그리고 팩토리얼을 출력하는 프로그램

num = int(input('정수 입력: '))
sum = 0

for i in range(1, (num + 1)):
  sum += i 
print(f'합: {sum:,}')

sum = 0
for i in range(1, (num + 1)):
  if i % 2 != 0:
    sum += i
print(f'홀수합: {sum:,}')

sum = 0
for i in range(1, (num + 1)):
  if i % 2 == 0:
    sum += i
print(f'홀수합: {sum:,}')

factorial = 1
for i in range(1, (num + 1)):
    factorial *= i
print(f'팩토리얼: {factorial:,}')
    
    

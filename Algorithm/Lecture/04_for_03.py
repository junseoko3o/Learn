# * 을 이용하여 다양한 모양 출력하기

for i in range(1, 6):
  for j in range(i):
    print('*', end='')
  print()
  
print('-' * 20)  

for i1 in range(1, 6):
  for i2 in range(6 - i1 - 1):
    print(' ', end='')
  for i3 in range(i1):
    print('*', end='')
  print()
  
print('-' * 30)

for i in range(5, 0, -1):
  for j in range(i):
    print('*', end='')
  print()
  
print('-' * 30)

for i1 in range(5, 0, -1):
  for i2 in range(5 - i1):
    print(' ', end='')
  for i3 in range(i1):
    print('*', end='')
  print()
  
print('-' * 30)

for i in range(1, 10):
  if i < 6:
    for j in range(i):
      print('*', end='')
  else: 
    for j in range(10 - i):
      print('*', end='')

  print()
  
print('-' * 30)  

for i in range(1, 6):
  for j in range(1, 6):
    if j == i:
      print('*', end='')
    else: 
      print(' ', end='')
  print()
  
print('-' * 30)  



n = int(input())

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(i*2-1))
for j in range(n-1, 0, -1):
    print(" "*(n-j)+"*"*(j*2-1))
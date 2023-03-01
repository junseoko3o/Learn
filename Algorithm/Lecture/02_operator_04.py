# 고도가 60m 올라갈 때 마다 기온디 0.8도씩 내려 간다고 할 때 고도를 입력하면 기온이 출력되는 프로그램
# 지면 (29도)

baseTemp = 29
step = 60
stepTemp = 0.8

height = int(input('고도 입력 :'))
targetTemp = baseTemp - (height // step * 0.8)

if height & step != 0:
  targetTemp -= stepTemp
  
print(f'지면온도: {baseTemp}')
print(f'고도 {height}의 기온: {targetTemp:.2f}')

# 197개 빵 152개 우유를 17명의 학생에게 나눠준다. 한명이 빵 과 우유 개수 남는거까지 출력
bread = 197
milk = 152
student = 17

print(f'명당 빵 개수: {bread // student}')
print(f'명당 우유 개수: {milk // student}')

print(f'남는 빵: {bread % student}')
print(f'남는 우유: {milk % student}')
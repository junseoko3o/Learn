# 함수를 이용해 이동거리 이동시간 반환
# 거리 = 속도 * 시간 

def getDistance(speed, hour, min):
  distance = speed * (hour + min / 60)
  return distance

s = float(input('속도(km/h): '))
h = float(input('시간(h): '))
m = float(input('분(m): '))
d = getDistance(s, h, m)

print(f'거리: {d:.2f}km, 속도: {s}km/h, 시간: {h}시간 {m}분')





def getTime(speed, distance):
  time = distance / speed
  hour = int(time)
  mini = int((time - hour) * 100 * 60 / 100) # 분 구하기
  return [hour, mini]

s = float(input('속도(km/h): '))
d = float(input('거리(km): '))
t = getTime(s, d)

print(f'거리: {d}km, 속도: {s}km/h, {t[0]}시간, {t[1]}분')


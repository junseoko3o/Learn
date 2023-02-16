# 모듈 - 이미 만들어진거 쉽게 가져다 쓰는거
# 내부모듈(기본설치), 외부모듈(별도 설치), 사용자모듈(직접만들어)

# random모듈 1 ~10 정수중 난수
import random
rNum = random.randint(1, 10)
print(f'{rNum}')

# 0 ~100 난수 10개
import random
rNum = random.sample(range(1, 100), 10)
print(f'{rNum}')


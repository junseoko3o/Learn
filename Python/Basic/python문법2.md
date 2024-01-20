## 기본 입출력
- 모든 프로그램은 적절한 약속된 입출력 양식을 가지고 있다.
- 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것
- ex) 학생의 성적 데이터가 주어지고 이를 내림차순으로 정렬한 결과를 출력하는 프로그램
```
입력예시
5   # 학생수
65 90 75 34 99 # 성적

출력예시
99 90 75 65 34 # 내림차순
```

## 자주 사용되는 표준 입력 방법
- input() 함수는 한 줄의 문자열을 입력 받는 함수
- map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
- ex) 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용
  - list(map(int , input().split()))
- ex) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용
  - a, b, c = map(int, input().split())
  
```python
# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 실행결과
# 5
# 65 90 75 34 99
# [99, 90, 75, 65, 34]
```

```python
# n,m,k 를 공백을 기준으로 구분하여 입력
n, m, k = map(int, input().split())

print(n,m,k)

# 실행 결과
# 3 5 7
# 3 5 7
```

## 빠르게 입력 받기
- 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
- 파이썬의 경우 sys라이브러리에 정되어 있는 sys.stdin.readlint() 메서드를 이용
  - 단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사

```python
import sys

# 문자열 입력 받기
data = sys.stdin.readlint().rstrip()
print(data)
```

## 자주 사용되는 표준 출력 방법
- 파이썬에서 기본 출력은 print() 함수를 이용한다.
  - 각 변수를 콤마를 이용하여 띄어쓰기로 구분하여 출력할 수 있다.
- print() 는 기본적으로 출력 이후에 줄 바꿈을 수행한다.
  - 줄 바꿈을 원치 않는경우 end 속성을 이용할 수 있다.

```python
# 출력할 변수들
a = 1
b = 2
print (a, b)
print(7, end = "")
print(8, end = "")

# 출력할 변수
answer= 7
print( "정답은" + str(answer) + "입니다.")

# 실행결과
# 1 2
# 7 8  정답은 7 입니다.
```

## f-string 예제
- 파이썬 3.6부터 사용 가능 하며, 문자열 앞에 접두사 f 를 붙여서 사용
- 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.

```python
answer = 7
print(f"정답은 {answer} 입니다")

# 실행결과
# 정답은 7입니다.
```

## 조건문
- 프로그램의 흐름을 제어하는 문법
- 조건문을 이용해 조건에 따라 프로그램의 로직을 설정할 수 있다.

```python
x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")

# 실행결과
# x >= 10
# x >= 0
```

## 들여쓰기
- 파이썬에서는 코드의 블록(특정 기능을 수행하기위한 한 단위의 코드 묶음) 을 들여쓰기로 지정한다.
- 다음 코드에서 2번 라인은 무조건 실행

```python
score = 85

if score >= 70:
    print ('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70점 미만입니다.')      # 1
    print('조금 더 분발 하세요')

print('프로그램을 종료한다')              # 2

# 성적이 70점 이상입니다.
# 프로그램을 종료합니다.
```

- 탭을 사용하는 쪽과 공백문자(space)를 여러번 사용하는 쪽으로 두 진영이 있다.
  - 이에 대한 논쟁은 지금까지도 활발
- 파이썬 스타일 가이드라인에서는 4개의 공백 문자를 사용하는 것을 표준으로 설정하고 있다.

## 조건문의 기본 형태
- if ~ elif ~ else 
  - 조건문을 사용할때 elif(elseif) 혹은 else 부분은 경우에 따라서 사용하지 않아도 된다.

```python
if 조건문 1:
    조건문 1이 True일 때 실행되는 코드
elif 조건문 2:
    조건문 1에 해당하지 않고, 조건문 2가 True일 때 실행되는 코드
else:
    위의 모든 조건문이 모두 True값이 아닐 때 실행되는 코드
```

```python
score = 85

if score >= 90:
    print("학점: A")
elif socre >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
else: 
    print("학점: F")

# 실행결과
# 학점:B
```

### 비교연산자
- 특정한 두 값을 비교할 때 이용할 수 있다.
  - 대입연산자(=)와 같음연산자(==)의 차이를 주의!

### 논리연산자
- 논리값 (True/False) 사이의 연산을 수행할 때 사용

### 기타 연산자
- 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공
  - 리스트,튜플,문자열,딕셔너리 모두에서 사용 가능
  - x in 리스트 -> 리스트 안에 x가 들어가 있을 때 참
  - x not in 문자열 -> 문자열 안에 x가 들어가 있지 않을때 참

### 파이썬의 pass 키워드
- 아무것도 처리하고 싶지 않을 때 pass키워드 사용
  - 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우

```python
score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만 입니다.')

print('프로그램을 종료합니다.')

# 프로그램을 종료합니다.
```

### 조건문의 간소화
- 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현 가능
```python
score = 85

if score >= 80: result = "Success"
else: result = "Fail"

# Success
```
- 조건부 표현식은 if ~ else 문을 한 줄에 작성할 수 있도록 해준다.
```python
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# Success
```

### 파이썬 조건문 내에서의 부등식
- 다른 프로그래밍 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다.
- x > 0 and x < 20 과 0 < x < 20 은 같은 결과를 반환한다.

## 반복문
- 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법
- 파이썬에는 while문과 for문이 있는데, 어떤 것을 사용해도 상관 없다.
  - 다만 코테에서의 실제 사용 예시를 확인해 보면, for 문이 더 간결한 경우가 많다.

```python
i = 1
result = 0

# i 가 9 보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)

# 실행 결과
# 45
```
### 1부터 9까지 홀수의 합 구하기 예제 (while문)
```python
i = 1 
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
      result += i
    i += 1
    
print(result)

# 실행결과
# 25
```
### 반복문에서의 무한 루프
- 무한루프란 끊임 없이 반복되는 반복 구문을 의미
  - 코테에서 무한 루프를 구현할 일은 거의 없으니 유의해야 한다.
  - 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인해야 한다.

## 반복문 : for 문
- 특정한 변수를 이요하여 'in' 뒤에 오는 데이터에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문
```python
for 변수 in 리스트:
    실행할 소스코드
```

```python
array = [9, 8, 7, 6, 5]

for x in array:
    print(x)

# 실행결과
# 9
# 8
# 7
# 6
# 5
```

- for 문에서 연속적인 값을 차례대호 순회할 때는 range()를 주로 사용한다.
  - 이때 range(시작값, 끝값 +1) 형태로 사용한다.
  - 인자를 하나만 넣으면 자동으로 시작 값은 0이 된다.

```python
result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1,10):
    result += i
print(result)

# 45
```
```python
result = 0 

for i in range (1,31):
    result += i
print(result)

# 465
```

### 파이썬의 continue 키워드
- 반복문에서 남은 코드의 실행을 건너뛰고 다음 반복을 진행하고자 할 때 continue를 사용
- 1부터 9까지의 홀수의 합을 구할 때 다음과 같이 작성 가능

```python
result = 0

for i in range(1,10):
    if i % 2 == 0:
        continue
    result += i
print(result)

# 25
```

### 파이썬의 break 키워드
- 반복문을 즉시 탈출하고자 할 때 break 사용
- 1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성
```python
i = 1

while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1

# 실행결과
# 현재 i의 값: 1
# 현재 i의 값: 2
# 현재 i의 값: 3
# 현재 i의 값: 4
# 현재 i의 값: 5
```

### 예제 80점 넘으면 합격

```python
score = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 1 번 학생은 합격입니다.
# 2 번 학생은 합격입니다.
# 5 번 학생은 합격입니다.
```

### 예제 특정번호 학생 제외

```python
score = [90, 85, 77, 65, 97]
cheating_student_list = {2,4}

for i in range(5):
    if i + 1 in cheating_student_list:
      continue
    if scores[i] >= 80:
      print(i + 1, "번 학생은 합격입니다.")
      
# 1번 학생은 합격입니다.
# 5번 학생은 합격입니다.

```

### 중첩된 반복문 : 구구단 예제

```python
for i in range (2, 10):
    for j in range (1, 10):
        print(i, "X",j, "=", i * j)
    print()

# 실행결과
# 구구단 쭉 2~9단 출력
```

## 함수
- 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미한다.
- 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있다.
- 종류
  - 내장함수
    - 파이썬이 기본적으로 제공하는 함수
  - 사용자 정의 함수
    - 개발자가 직접 정의하여 사용할 수 있는 함수
- 정의하기
  - 프로그램에서는 똑같은 코드가 반복적으로 사용되어야 할 때가 많다.
  - 함수를 사용하면 소스코드의 길이를 줄일 수 있다.
    - 매개변수 : 함수 내부에서 사용할 변수
    - 반환 값 : 함수에서 처리 된 결과를 반환

```python
def 함수명(매개변수):
    실행할 소스코드
    return 반환  
```

- 더하기 함수 예시
```python
def add(a,b):
    return a + b
print(add(3,7))

# 10
```
```python
def add(a,b):
    print('함수의 결과:', a + b)

add(3,7)

# 10 
```

### 파라미터 지정하기
- 파라미터(매개변수)의 변수를 직접 지정할 수 있다.
  - 이 경우 매개변수 순서 달라도 상관 없음
```python
def add(a,b):
    print('함수의 결과:', a + b)

add(b = 3, a = 7)

# 10
```

### global 키워드
- global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.

```python
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 10
```

### 여러개의 반환 값
- 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
```python
def operator(a,b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return  add_var, subtract_var, multiply_var, divide_var

a,b,c,d = operator(7,3)
print(a,b,c,d)

```

## 람다 표현식
- 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다.
  - 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징

```python
def add(a,b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3,7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda  a, b: a + b)(3,7))

# 10 
# 10
```

### 람다 표현식 예시 : 내장 함수에서 자주 사용되는 람다 함수
```python
array = [('홍길동', 50),('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda  x: x[1]))

# 실행결과
# [('이순신', 32),('홍길동', 50), ('아무개', 74)]
# [('이순신', 32),('홍길동', 50), ('아무개', 74)]
```

### 람다 표현식 예시: 여러 개의 리스트에 적용
```python
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a,b: a + b, list1, list2)

print(list(result))

# [7, 9, 11, 13, 15]
```

## 실전에서 유용한 표준 라이브러리
- 내장함수 
  - 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공
    - 파이썬 프로그램을 작성할 때 없어서는 안되는 필수적인 기능을 포함하고 있다.
- intertools 
  - 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
    - 특히 순열과 조합 라이브러리는 코테에서 자주 사용
- heapq
  - 힙(Heap) 자료구조를 제공
    - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용된다.
- bisect
  - 이진 탐색 기능을 제공
- collections 
  - 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
- math
  - 필수적인 수학적 기능을 제공
    - 팩토리얼,제곱근,최대공약수,삼각함수 관련 함수부터 파이와 같은 상수를 포함한다.

### 자주 사용되는 내장 함수
```python
# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min () , max ()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval() 실제 수 형태로 반환
result = eval("(3+5)*7")
print(result) 

# 15
# 2 7
```

```python
# sroted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key = lambda x:x[1], reverse = True)
print(result)

# [1, 4, 5, 8, 9]
# [9, 8, 5, 4, 1]
# [('이순신', 75), ('아무개', 50), ('홍길동', 35)]

```

### 순열과 조합
- 모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 효과적으로 사용할 수 있을까?
- 순열 
  - 서로다른 n 개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
  - {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우
  - 'ABC' , 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
```python
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```
- 조합
  - 서로다른 n 개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
  - {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우
  - 'AB', 'AC', 'BC'

```python
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터준비

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

# [('A','B'), ('A','C'), ('B','C')]
```

### 중복 순열과 중복 조합
```python
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 구하기(중복허용)
print(result)
```

```python
from itertools import combinations_with_replacement

data = ['A', 'B'. 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)
```

## Counter
- 파이선 collections 라이브러리의 Counter는 등장 획수를 세는 기능 제공
- 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려준다.
```python
from collections import  Counter

counter = Counter(['red', 'blud', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'greed'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

# 3
# 1
# {'red' : 2, 'blue': 3, 'green' : 1}
```

## 최대 공약수와 최소 공배수
- 최대 공약수를 구해야할 때는 math 라이브러리의 gcd()함수를 이용할 수 있다.

```python
import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
  return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14)) # 최소 공배수(LCM) 계산

# 7
# 42
```
- 수학적 기능이 필요할 때 마다 요긴하게 호출해서 사용가능
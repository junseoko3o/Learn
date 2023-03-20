# ORDER BY
- ORDER BY column
- 입력한 컬럼 이름을 기준으로 모든 row 정렬
- 기본 정렬 규칙은 오름차순 
- 내림차순은 ORDER BY column DESC
- 여러 컬럼으로 정렬도 가능 하며, 키워드 뒤에 컬럼을 복수로 입력 가능

```SQL
SELECT col
FROM table
WHERE 조건
ORDER BY col
```

```SQL
SELECT number, name
FROM pocketmon
ORDER BY number DESC;
```

```SQL
SELECT number, name, attack, defense
FROM pocketmon
ORDER BY attack DESC, defense;
```

```SQL
SELECT number, name, attack, defense # 1, 2, 3, 4
FROM pocketmon
ORDER BY 3 DESC, 4;
```
# RANK
- RANK() OVER(ORDER BY col) 형식
- 항상 ORDER BY와 함께 사용
- SELECT 절에 사용하며, 정렬된 순서에 순위를 붙인 새로운 컬럼을 보여준다.
  - 원본 테이블에 영향을 끼치진 않음

```SQL
SELECT col, ..., RANK() OVER(ORDER BY col DESC)
FROM table
WHERE 조건
```

```SQL
SELECT name, attack
      RANK() OVER(ORDER BY attack DESC) AS attack_rank
FROM pocketmon.mypocketmon;
```

- DENSE_RANK, ROW_NUMBER 
  - ORDER BY 와 함께 사용

```SQL
SELECT name, attack
      DENSE_RANK() OVER(ORDER BY attack DESC) AS attack_rank
      ROW_NUMBER() OVER(ORDER BY attack DESC) AS attack_rank1
FROM pocketmon.mypocketmon;
```

- 순위가 조금씩 다르게 나옴.
- RANK vs DENSE_RANK 
  - 공동 순위가 있을때 DENSE_RANK는 넘어가지 않는다.
  - RANK 1,2,3,3,5  // DENSE_RANK 1,2,3,3,4

- ROW_NUMBER
  - 공동 순서를 무시한다.
  - 그냥 ROW로 순위결정 (동점이어도 다른 순위를 나타냄)

# 함수
- 함수이름 (함수를 적용할 값 또는 컬럼이름)형식으로 사용
- 결과 값을 새로운 컬럼으로 반환

## 자주 사용하는 문자형 데이터 함수
```SQL
LOCATE("A", "ABC") 
-- ABC에서 A는 몇번째에 위치해 있는지 검색 
-- 없으면 0을 반환  
-- 문자가 여러개면 가장 먼저 찾은 문자 위치 반환

SUBSTRING("ABC", 2)
-- ABC에서 2번째 문자 반환
-- 입력한 숫자가 문자보다 길면 아무것도 가져오지 않는다.

RIGHT("ABC", 1)
LEFT("ABC", 1)
-- 오른쪽에서 or 왼쪽에서 1번째 문자까지 반환

UPPER("abc")
LOWER("ABC")
-- UPPER는 대문저로 바꿔줌, LOWER는 소문자로 바꿔줌

LENGTH("ABC")
-- 문자열의 글자수를 반환

CONCAT("ABC", "DEF")
-- 문자열을 합쳐준다.

REPLACE("ABC", "A", "Z")
-- ABC에서 A를 Z로 바꿔서 반환
```

## 숫자형 데이터
```SQL
ABS(숫자)
-- 숫자의 절대값 반환

CEILING(숫자)
-- 숫자를 정수로 올림 해서 반환

FLOOR(숫자)
-- 숫자를 정수로 내림 해서 반환

ROUND(숫자, 자리수)
-- 숫자를 소수점 자리수까지 반올림해서 반환
TRUNCATE(숫자, 자리수)
-- 숫자를 소수점 자리수까지 버림해서 반환
-- 자리수에 0 넣으면 정수반환

POWER(숫자1, 숫자2)
-- 1의 2 제곱 반환

MOD(숫자1, 숫자2)
-- 1을 2로 나눈 나머지 반환
```

## 날짜형
```SQL
NOW() -- 현재 시간과 날짜 반환
CURRENT_DATE() -- 현재 날짜 반환
CURRENT_TIME() -- 현재 시간 반환
-- 위 3개는 입력값이 필요 없음

YEAR(날짜) -- 날짜의 연도 반환
MONTH(날짜) -- 날짜의 월 반환
MONTHNAME(날짜) -- 날짜의 월을 영어로 반환

DAYNAME(날짜) -- 날짜의 요일을 영어로 반환
DAYOFMONTH(날짜) -- 날짜의 일을 반환
DAYOFWEEK(날짜) -- 날짜의 요일을 숫자로 반환
WEEK(날짜) -- 날짜가 해당 연도의 몇번째 주인지 반환

HOUR(시간) -- 시간의 시 
MINUTE(시간) -- 시간의 분
SECOND(시간) -- 시간의 초

DATE_FORMAT(날짜/시간) -- 날짜/시간의 형식을 형식으로 바꿔 반환
-- DATE_FORMAT('2023-03-01 13:00:00', '%Y년 %m월 %d일 %H시 %i분 %s초')

DATEDIFF(날짜1, 날짜2) -- 두 날짜 차이 반환
TIMEDIFF(시간1, 시간2) -- 두 시간 차이 반환
```

# example
```SQL
/*
MISSION (1)
포켓몬 테이블에서 포켓몬의 이름과 이름의 글자 수를 이름의 글자 수로 정렬해서 가져와 주세요.
(정렬 순서는 글자 수가 적은 것부터 많은 것 순으로 해주세요.) 
*/

SELECT name, LENGTH(name)
FROM mypokemon
ORDER BY LENGTH(name);


/*
MISSION (2)
포켓몬 테이블에서 방어력 순위를 보여주는 컬럼을 새로 만들어서  ‘defense_rank’라는 별명으로 가져와 주세요. 이 때, 포켓몬 이름 데이터도 함께 가져와 주세요.
조건1: 방어력 순위란 방어력이 큰 순서대로 나열한 순위를 의미합니다.
조건2: 공동 순위가 있으면 다음 순서로 건너 뛰어 주세요.
*/

SELECT name, RANK() OVER (ORDER BY defense DESC) AS defense_rank
FROM mypokemon;

/*
MISSION (3)
포켓몬 테이블에서 포켓몬을 포획한 지 기준 날짜까지 며칠이 지났는 지를 ‘days’라는 별명으로 가져와 주세요. 이 때, 포켓몬의 이름도 함께 가져와 주세요.
조건: 기준 날짜는 2022년 2월 14일입니다.
*/

SELECT name, DATEDIFF('2022-02-14', capture_date) AS days
FROM mypokemon;


SELECT name, DATEDIFF(capture_date, '2022-02-14') AS days
FROM mypokemon;

```







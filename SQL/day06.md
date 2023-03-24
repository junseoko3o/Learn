# GROUP BY
- 컬럼에서 동일한 값을 가지는 로우를 그룹화 한다.
- GROUP BY column
- GROUP BY에 쓰인 쿼리의 SELECT 절에는 GROUP BY 대상컬럼과 그룹 함수만 사용이 가능하다.
  - 만약 GROUP BY 대상이 아닌 컬럼을 SELECT하면 에러
- 여러 컬럼으로도 그룹화가 가능하며 키워드 뒤에 컬럼이름을 복수로 넣으면 된다.
- 컬럼 번호도 그룹화가 가능하다.

```SQL
SELECT GROUP BY 대상컬럼이름, 그룹함수
FROM table_name
WHERE 조건
GROUP BY column
```

```SQL
SELECT type
FROM pocketmon.mypocketmon
GROUP BY type;
-- type이 같은 값끼리 그룹으로 묶임
```

# HAVING
- 가져올 데이터 그룹에 조건을 걸어줌
- HAVING 조건식
- 조건식이 True만 그룹만 선택
- HAVING절의 조건식에는 그룹함수사용

```SQL
SELECT column, 그룹함수
FROM table_name
WHERE 조건
GROUP BY column
HAVING 조건
```

# 그룹함수
- COUNT
  - 그룹의 값 수를 세는 함수
  - COUNT(컬럼) // SELECT, HAVING 절에 사용
    - 집계할 컬럼 이름은 그룹의 기준이 되는 컬럼 이름과 같아도 같지 않아도 괜찮
    - COUNT(1)은 하나의 값을 1로 세어주는 표현으로 COUNT함수에서 자주사용
  - GROUP BY가 없는 쿼리에서도 사용 가능하며 이떄는 전체 로우에 함수가 적용
  ```SQL
  SELECT column,COUNT(column)
  FROM table_name
  GROUP BY column
  HAVING 조건
  ```

- SUM
  - 그룹의 함 계산
  - SUM(column), // SELECT, HAVING절에 사용
    - 집계할 컬럼이름 상관없음
  - GROUP BY가 없는 쿼리에서도 사용가능 이떄 전체 로우 함수 적용
  ```SQL
  SELECT column,SUM(column)
  FROM table_name
  GROUP BY column
  HAVING 조건
  ```

- AVG 
  - 그룹의 평균 계산
  - AVG(column) // SELECT, HAVING절 사용
    - 컬럼이름 상관 없음
  - GROUP BY가 없는 쿼리에서도 사용가능 이떄 전체 로우 함수 적용
  ```SQL
  SELECT column,AVG(column)
  FROM table_name
  GROUP BY column
  HAVING 조건
  ```
- MIN 
  - 그룹의 최소값 반환
  - MIN(column) // SELECT, HAVING절 사용
    - 컬럼이름 상관 없음
  - GROUP BY가 없는 쿼리에서도 사용가능 이떄 전체 로우 함수 적용
  ```SQL
  SELECT column,MIN(column)
  FROM table_name
  GROUP BY column
  HAVING 조건
  ```

- MAX 
  - 그룹의 최소값 반환
  - MAX(column) // SELECT, HAVING절 사용
    - 컬럼이름 상관 없음
  - GROUP BY가 없는 쿼리에서도 사용가능 이떄 전체 로우 함수 적용
  ```SQL
  SELECT column,MAX(column)
  FROM table_name
  GROUP BY column
  HAVING 조건
  ```

## example
```SQL
SELECT type, COUNT(*), COUNT(1), AVG(height), MAX(weight)
FROM pocketmon.mypocketmon
GROUP BY type;
-- 전체 컬럼가져와서 세는거 COUNT(*)
```

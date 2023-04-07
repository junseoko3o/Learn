# 서브쿼리
- SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY
- 하나의 쿼리 내 포함된 또 하나의 쿼리
- 반드시 괄호 안에 있어야 한다.
- INSERT, UPDATE, DELETE문에서도 사용 가능
- ;(세미콜론) 없어도된다.
  - 메인쿼리의 마지막에만 붙인다.

# SELECT 
- 스칼라 서브쿼리
- 반드시 결과값이 하나의 값이어야한다.

```SQL
SELECT column,
  (SELECT column
  FROM table
  WHERE 조건)
FROM table
WHERE 조건;
```

```SQL
SELECT number, name,
  (SELECT height FROM ability WHERE number=25) AS height
FROM mypocketmon
WHERE name='pikachu';
```

# FROM
- 인라인 뷰 서브쿼리
- FROM절의 서브쿼리는 반드시 결과값이 하나의 테이블
- 서브쿼리로 마든 테이블은 반드시 별칭 필요

```SQL
SELECT column
FROM (SELECT column
      FROM table
      WHERE 조건) AS 별칭
WHERE 조건;
```

```SQL
SELECT number, height_rank
FROM (SELECT number, rank() OVER(ORDER BY height DESC) AS height_rank FROM ability) AS A
WHERE height_rank=3;
```

# WHERE
- 중첩 서브쿼리
- WHERE절의 서브쿼리는 반드시 결과값이 하나의 컬럼이어야 한다.(EXISTS 제외)
  - 하나의 컬럼에는 여러 개의 값이 존재할 수 있다.
- 연산자와 함께 사용
  - 일반적으로 WHERE column 연산자 서브쿼리 형식으로 사용

```SQL
SELECT column
FROM table
WHERE column 연산자 (SELECT column FROM table WHERE 조건);
```

- 비교 연산자만 사용시 WHERE절의 서브쿼리는 반드시 결과값이 하나의 값이어야 한다.
- 주요 언산자 (IN, ALL, ANY, EXISTS) 
  - IN 
    - 결과값 내에 있다
  - ALL
    - 모든 서브쿼리의 결과값보다 작다/크다
  - ANY
    - 서브쿼리의 결과값보다 하나라도 작다/크다
  - EXISTS/ NOT EXISTS
    - 서브쿼리의 결과값이 존재한다/존재하지 않는다.  
- 주요 언산자 사용시, WHERE절의 서브쿼리는 반드시 결과값이 하나의 컬럼
- 단, EXISTS는 단독으로 사용하며, 결과값이 여러 컬럼이어도 된다.
  

```SQL
-- 키가 평균 키보다 작은 포켓몬의 번호 가져오기
SELECT number
FROM ability
WHERE height < (SELECT AVG(height) FROM ability);
```

```SQL
-- 공격력이 모든 전기 포켓몬의 공격력보다 작은 포켓몬의 번호 가져오기
SELECT number
FROM ability
WHERE attck < ALL(SELECT attack FROM ability WHERE type='electric');
```

```SQL
-- 방어력이 모든 전기 포켓몬의 공력보다 하나라도 큰 포켓몬의 번호 가져오기
SELECT number
FROM ability
WHERe defense > ANY(SELECT attack FROM ability WHERE type='electric');
```

```SQL
-- 버그 타입 포켓몬이 있다면 모든 포켓몬의 번호 가져오기
SELECT number
FROM ability
WHERE EXISTS(SELECT * FROM ability WHERE type='bug');
```
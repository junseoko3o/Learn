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

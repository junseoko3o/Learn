# UNION / UNION ALL (합집합)
- 쿼리1 UNION 쿼리2 또는 쿼리1 UNION ALL 쿼리2 형식
- 쿼리1, 쿼리2 합쳐보여줌
- UNION은 중복을 제거하고 보여주고, UNION ALL은 중복을 포함하여 보여준다.
- 주의
  - 쿼리1, 쿼리2의 결과 값의 개수가 같아야함
    - 다르면 에러 
  - ORDER BY는 쿼리 가장 마지막에 작성이 가능, 쿼리1에서 select해온 컬럼으로만 가능


```SQL
SELECT column
FROM table
UNION
SELECT column2
FROM table
```

```SQL
SELECT column
FROM table
UNION ALL
SELECT column2
FROM table
```

## example

```SQL
SELECT name
FROM mypocketmon
UNION ALL -- UNION
SELECT name
FROM friendpocketmon;
```

```SQL
SELECT number, name, attack
FROM mypocketmon
UNION
SELECT number, name, attck
FROM friendpocketmon
ORDER BY number;
```

# 다른 DB INTERSECTOR / MINUS
- MySQL 은 JOIN으로 표현

- 교집합
  
```SQL
SELECT column
FROM table as A
INNER JOIN tableB as B
ON A.column = B.column AND...AND A.columnN = B.columnN
```
- 차집합
  
```SQL
SELECT column
FROM tableA as A
LEFT JOIN tableB as B
ON A.column = B.column AND ... AND A.columnN = B.columnN
WHERE B.column IS NULL;
```


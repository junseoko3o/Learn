# JOIN
- 같은 의미를 가지는 컬럼의 값을 기준으로 테이블을 합칠 때 사용


## 종류
- INNER JOIN
  - default
  - 기본 조인 두 테이블 모두에 있는 값만 찾기 (교집합)
  
```SQL
SELECT column
FROM table
INNER JOIN tableB
ON table.column = tableB.columnB -- 값을 서로 연결 
WHERE 조건;
```
```SQL
SELECT *
FROM mypoketmon
INNER JOIN ability
ON mypocketmon.number = ability.number;
```




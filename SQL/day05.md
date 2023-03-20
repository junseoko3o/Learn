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







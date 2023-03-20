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



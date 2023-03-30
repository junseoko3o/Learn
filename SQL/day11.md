# DELETE 데이터 삭제

```SQL
DELETE FROM table
WHERE 조건;
```

```SQL
DELETE FROM pocketmon.mypocketmon
WHERE attack > 50;
```

# UPDATE / SET (데이터 수정)

```SQL
UPDATE table
SET column = new
WHERE 조건;
```

```SQL
UPDATE pocketmon.mypoketmon
SET type = 'normal'
WHERE name = 'chikorita';
```



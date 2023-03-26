# IF 함수
- IF(조건식, 참일떄 값, 거짓일때 값)
- SELECT 절에서 사용하며, 결과값을 새로운 컬럼으로 반환

```SQL
SELECT name,IF(attack >= 60, 'strong', 'weak') AS attack_class
FROM pocketmon.mypocketmon;
```

# IFNULL
- 데이터가 NULL인지 아닌지 확인해 NULL이면 새로운 값 반환하는 함수
- 특징
  - IFNULL(컬럼이름, NULL일 때 값)
  - 해당 컬럼의 값이 NULL인 로우에서 NULL 일떄의 값 반환
  - 주로 SELECT절에서 사용, 결과 값을 새로운 컬럼으로 반환 

```SQL
SELECT name,IFNULL(name, 'unknown') AS full_name
FROM pocetmon.mypocketmon;
``` 

# CASE
- 주로 SELECT절에서 사용, 새로운값으로 결과 반환
- ELSE 생략하면 NULL 반환

```SQL
-- 형식 1
CASE 
  WHEN 조건식1 THEN 결과값1
  WHEN 조건식2 THEN 결과값2
  ELSE 결과값3
END
```

```SQL
-- 형식 2
CASE 컬럼이름
  WHEN 조건값1 THEN 결과값1
  WHEN 조건값2 THEN 결과값2
  ELSE 결과값3
END
```

## example

```SQL
SELECT name,
CASE 
  WHEN attack >= 100 THEN 'very strong'
  WHEN attack >= 60 THEN 'strong'
  ELSE 'weak'
END AS attack_class
FROM pocketmon.mypocketmon;
```

```SQL
SELECT name, type
CASE 
  WHEN 'bug' THEN 'grass'
  WHEN 'electric' THEN 'water'
  WHEN 'grass' THEN 'bug'
END AS rival_type
FROM pockemon.mypocketmon;
```
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
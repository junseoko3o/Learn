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

# 


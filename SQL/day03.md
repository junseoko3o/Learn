# 데이터 가져오기

## SELECT
- 값을 가져올 컬럼을 선택
- 즉, 테이블 안에서 특정 컬럼을 선택
- 모든 쿼리에 필수적 
  - 숫자,문자 데이터 가져오는 역할
  - 컬럼을 선택해 컬럼 값을 가져오는 역할
  - * 을 통해 컬럼 전체를 가져오는 역할 

## FROM 
- 가져올 테이블을 지정
- FROM table_name
- 테이블이 어떤 데이터베이스에 속해 있는지 데이터베이스 이름도 같이 명시 해줘야함
  - 단, USE키워드를 통해 사용한다면 데이터베이스 이름 생략 가능

## SELECT, FROM 문법
```SQL
SELECT column
FROM db_name.table_name;

--
USE db_name
SELECT cloumn
FROM table_name;

--
# 여러개
SELECT col1, col2, col3
FROM db_name.table_name;

--
# 전체
SELECT *
FROM db_name.table_name;
```

## AS
- AS 컬럼별칭
- 테이블 내의 실제 컬럼은 변경되지 않고, 별칭은 쿼리 내에서만 유효
  - 만약 실제 컬럼 이름을 변경하고 싶으면 ALTER TABLE 문법 사용

```SQL
SELECT column as nick
FROM db_name.tablae_name;
```

## LIMIT
- 가져올 데이터의 row 개수를 정한다. 일부만 가져옴
- LIMIT row수
- 쿼리의 가장 마지막에 위치 

```SQL
SELECT number
FROM db_name.table_name;
LIMIT 2; -- 2개만 가져옴
```

## DISTINCT
- 중복된 값은 제거하고, 같은 값은 한 번만 가져온다.
- DISTINCT column
- SELECT 절에 사용 

```SQL
SELECT DISTINCT type
FROM db_name.table_name;

-- 같은 값이 있으면 하나의 결과만 보여준다. 
```

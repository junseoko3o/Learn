# 데이터 종류 알아보기
- 데이터 저장하기 전에 저장 공간의 데이터 타입을 미리 지정해줘야만 한다.
- 타입과 다른경우 저장이 불가능

## 숫자형
### 정수형 
- 소수점이 없는 숫자 데이터
  
<img src="https://velog.velcdn.com/images/o3ojunseok/post/97b4cb62-2984-4295-9d10-4511f8ea41b4/image.png" width=500>

### 실수형
- 소수점이 있는 숫자 데이터
  
<img src="https://velog.velcdn.com/images/o3ojunseok/post/180423d0-433d-4e1a-b53b-a01abb24bf5b/image.png" width=500>

## 문자형
- "가나다" , "ABC"
  
<img src="https://velog.velcdn.com/images/o3ojunseok/post/dbff6711-2e29-4927-b654-e238e3edb508/image.png" width=500>

## 날짜형
- 날짜와 시간 데이터 
  
<img src="https://velog.velcdn.com/images/o3ojunseok/post/40c24e1f-aa72-49f1-a89c-6e274eafab35/image.png" width=500>



## 문자형 데이터 기본 특징
- 문자형 데이터는 반드시 "" 또는 '' 와 함께 사용해야 한다.
- 따옴표가 없는 문자는 키워드나 함수, 데이터베이스/테이블/컬럼의 이름으로 인식이 된다.

## 데이터 타입 간 타입 변환
- 숫자형, 문자형, 날짜형 데이터는 함수를 사용하여 서로 타입 변환이 가능하다. 


## 테이블
- 데이터베이스에서 데이터의 형태를 정해 모아 놓은 저장 공간, 행과 열로 이루어진 데이터 표 
  - 컬럼 
    - 데이터를 저장하기 위한 틀
      - 컬럼의 이름과 데이터 타입은 테이블을 만들 때 미리 정해진다.
      - 컬럼의 이름은 동일한 테이블 내에서 중복될 수 없다.
      - 테이블은 반드시 1개 이상의 컬럼을 가져야 한다.
  - 값  
    - 컬럼에 속한 실제 데이터 값
      - 컬럼의 데이터 타입만을 값으로 가질 수 있다.
  - 로우(행)
    - 관계된 값의 리스트
      - 하나의 로우는 하나의 관계된 데이터를 의미한다.
      - 같은 테이블 안에서 로우는 항상 동일한 구조를 가진다.
      - 로우를 단위로 데이터를 삽입한다.

## 데이터베이스
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 데이터 저장소 (넓은 의미)
- 테이블을 저장해두는 저장소 (좁은 의미)
  - 폴더와 비슷한 개념 이 안에 테이블이 있고 그 안에 컬럼이 존재한다.
  - 스키마 라고도 한다.


## 테이블과 데이터베이스의 생성 순서
- 데이터베이스를 생성한 후에 특정 데이터베이스 내에 테이블을 생성한다.

## 데이터 베이스 만들기
- 쿼리 문법
  - 쿼리가 끝날 때는 항상 마친다는 의미의 ; 를 붙여줘야한다.
  
- 생성하기
  
```SQL
CREATE DATABASE name;
```

- 목록 보기
  
```SQL
SHOW DATABASES;
```

- 사용하기
  
```SQL
USE name;
```

- 테이블 및 컬럼 생성
  
```SQL
CREATE TABLE table_name (col1 varchar(20), col2 varchar(20), col3 int);
```

- 테이블 이름 변경하기
    
```SQL
ALTER TABLE table_name RENAME new_table_name;
```

- 새로운 컬럼 추가
  
```SQL
ALTER TABLE table_name ADD COLUMN col4 int;
```

- 기존 컬럼 타입 변경하기
  
```SQL
ALTER TABLE table_name MODIFY COLUMN col4 float;
```

- 컬럼이름과 타입 변경
  
```SQL
ALTER TABLE table_name
CHANGE COLUMN col4 new_col4 float;
```

- 컬럼 삭제

```SQL
ALTER TABLE table_name DROP COLUMN col4;
```
## 데이터베이스, 테이블, 컬럼 이름을 정하는 규칙
- 문자,숫자,_를 사용한다.
- 이름에 쓰이는 문자는 주로 영문 소문자 사용한다.
  - 한글도 사용은 하지만 인코딩 이슈로 주로 영문을 사용한다.
  - 보통 키워드나 함수명은 대문자, 사용자가 정의한 이름에는 소문자를 사용한다.
- 예약어는 사용 불가능하다.
  - 이미 키워드, 함수명 등의 문법적인 용도로 사용되고 있기 때문에 사용이 불가능하다.
- 단어와 단어 사이에는 빈칸 대신 _를 사용한다.
- 문자로 시작한다.
  - 숫자 또는 _ 로 시작하지 않는다.
- 데이터베이스 이름은 중복될 수 없다.
  - 테이블 이름은 하나의 데이터베이스 내에서는 중복될 수 없다.
  - 컬럼 이름은 하나의 테이블 내에서는 중복될 수 없다.


## 예제

```SQL
CREATE TABLE idol (
    name VARCHAR(20),
    age INT,
    group VARCHAR(50)
);
```

## 테이블 삭제
- 데이터 베이스 지우기

```SQL
DROP DATABASE name;
```

- 테이블 지우기
  
```SQL
DROP TABLE table_name;
```

- 테이블의 값만 지우기

```SQL
TRUNCATE TABLE table_name;
# table은 사라지지 않고 안의 값만 사라짐
```

- 데이터 베이스/ 테이블이 존재하면 지우기

```SQL
DROP DATABASE IF EXIST name;
```

```SQL
DROP TABLE IF EXIST table_name;
```


## 데이터 INSERT,DELETE,UPDATE

- 데이터 삽입

```SQL
INSERT INTO table_name (col1, col2, col3)
VALUES ("hi", 31, "hi");
```


- 데이터 여러개 삽입

```SQL
INSERT INTO table_name (col1, col2, col3)
VALUES ("hi", 31, "31"),("hi", 31, "31"),("hi", 31, "31");
```

- 데이터 삭제

```SQL
DELETE FROM table_name
WHERE 조건값;
```

- 데이터 수정

```SQL
UPDATE table_name
SET col1 = "hello"
WHERE 조건값;
```

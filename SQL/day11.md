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

# 제약조건
- 데이터를 입력할 때 실행되는 데이터 입력 규칙
- 테이블을 만들거나 변경하면서 설정
  - CREATE TABLE 및 ALTER TABLE 구문에서 설정 가능

- 종류
  - NOT NULL
  - UNIQUE
  - DEFAULT
  - PRIMARY KEY
  - FOREIGN KEY

```SQL
CREATE TABLE new_pocketmon(
  number INT PRIMARY KEY,
  name VARCHAR(20) UNIQUE,
  type VARCHAR(10) NOU NULL,
  attck INT DEFAULT 0
  defense INT DEFAULT 100,
  FOREIGN KEY(number) REFERENCES mypocketmon(number)
);
```

# SQL 분류
- DDL (Data Definition Language)
  - CREATE, ALTER, DROP, RENAME, TRUNCATE
  - 데이터 정의어
- DML (Data Manipulation Language)
  - SELECT, INSERT, UPDATE, DELETE
  - 데이터 조작어
- DCL (Data Control Language)
  - GRANT, REVOKE
  - 데이터 제어어
- TCL (Transaction Control Language)
  - COMMIT
  - ROLLBACK
  - SAVEPOINT
  - 트랜젝션 제어어

# 접근권한

```SQL
-- MYSQL 기본 데이터베이스인 mysql 데이터베이스 선택
USE mysql;

-- 사용자 목록 조회
SELECT user.host FROM user;

-- 사용자 생성
CREATE USER 이름@ip;

-- 비밀번호랑 같이 생성
CREATE USER 이름@ip IDENTIFIED BY '비밀번호';

-- 사용자 삭제
DROP USER 이름;

-- 권한 부여
GRANT 권한 ON 데이터베이스이름.테이블이름 TO 이름@ip;

-- 권한 확인
SHOW GARANTS FOR 이름@ip;

-- 권한 삭제
REVOKE 권한 ON 데이터베이스이름.테이블이름 FROM 이름@ip;

-- 권한 적용
FLUSH PRIVILEGES;

-- ex
-- ip 전체 허용, newuser한테 모든권한부여
GRANT ALL PRIVILEGES ON mydb.mytb TO newuser@%;

-- newuser한테 모든 데이터베이스 테이블에 대한 SELECT INSERT권한
GRANT SELECT,INSERT ON *.* TO newuser@%;
```
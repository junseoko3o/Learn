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


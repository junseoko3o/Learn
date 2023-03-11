# 데이터베이스
- 자료를 구조화 하여 저장해 효율적 관리 가능
- 여러 업무에 여러 사용자가 동시에 사용 가능
- 사용자가 데이터베이스를 기능을 사용하기 위해선 응용프래그램 사용해야 함 (DBMS)

## DBMS 종류
- Oracle, MYSQL, MSQL, MariaDB, PostgreSQL

## SQL
- Database와 사용자가 대화하기 위해 사용하는 약속의 언어
- ex)
- 남자 직원 목록 알려줘 -> SELECT * FROM employee WHERE gender='MAN';
- 쿼리 (Query)
  - SQL로 쓰인 데이터베이스에 명령을 내리는 문장

```sql
# db 목록보기
show databases; -- 모든 데이터베이스 목록 보기

/* 한방에 주석
1.
2.
3.
*/

# 테이블 만들기 
create database mydatabase;

# 사용할 데이터베이스 지정
use mydatabase;

# 테이블 만들기
create table mytable (
col1 int,
col2 char(2)
);

# 데이터 삽입하기
insert into mytable (col1, col2)
value (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e');

# mytable에 모든 데이터 가져오기
select * from mytable;

```
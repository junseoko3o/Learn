# WHERE
- WHERE 조건식
- 조건식이 True가 되는 로우만 선택

```SQL
SELECT column
FROM table
WHERE 조건
```

# 연산자
- 비교 연산자
  - =, <, >, !=, >=, <=
- 논리 연산자
  - AND, OR, NOT
- 주요 연산자
  - BETWEEN, IN
- LIKE 
  - 특정 문자열이 포함된 연산자
  - 와일드 카드
    - % 0개 이상의 문자, _ 1개 이상의 문자
- NULL
  - 데이터 값이 존재 하지 않음, 0이나 공백이 아닌 알 수 없는 값
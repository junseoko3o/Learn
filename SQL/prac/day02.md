## 2020년 7월의 MAU

```SQL
select 	count(*),
		count(customer_id),  
		count(distinct customer_id)
        
from sqlprac.tbl_visit
where visited_at >= '2020-07-01'
	and visited_at < '2020-08-01'
    
limit 10
```

- * 모든 테이블 모든 레코드 조회
- customer_id 가 있는 모든 로우에서 null 제외 하고 카운트
- 중복제외해서 로우 카운트
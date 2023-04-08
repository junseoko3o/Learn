## 2020년 7월의 Revenue를 구해

```SQL
select *

from sqlprac.tbl_purchase

where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'

limit 10
```

```SQL
select sum(price)

from sqlprac.tbl_purchase

where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
```


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


## 2020년 7월 우리 Active 유저의 구매율(Paying Rate)
### 구매유저 수 / 전체 활성유저

```SQL
-- 구매 유저수
select count(distinct customer_id)      
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01' 
```

```SQL
-- 전체 활성 유저
select count(distinct customer_id)
from sqlprac.tbl_visit
where visited_at >= '2020-07-01'
	and visited_at < '2020-08-01'
```

```SQL
-- 구매율
select round(11174/16414) * 100
```

## 7월에 구매 유저의 월 평균 구매액
## ARPPU = Average Revenue Per Paying User

```SQL
-- 7월 전체 유저별 구매액
select customer_id,
		sum(price)
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by customer_id -- 1도 가능
```

```SQL
-- 구매유저 월 평균 구매액
select avg(revenue)
from (select customer_id,
		sum(price) as revenue
    from sqlprac.tbl_purchase
    where purchased_at >= '2020-07-01'
	  and purchased_at < '2020-08-01'
    group by customer_id) foo -- 1도 가능
```
- foo 서브쿼리 쓸때 명시를 해줌
- from 절에 select 쓰는걸 보통 인라인뷰라함
- 1 (1번컬럼 지정을 간단하게)

## 7월에 가장 많이 구매한 TOP3 고객과 TOP 10 ~15고객

```SQL
select customer_id,
		sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by 1
order by 2 desc
limit 3 offset 10
```

- offset 10 상단 10개 버리고 limit3 해줌
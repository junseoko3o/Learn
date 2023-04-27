# 프로덕트 분석 
## 2020년 7월에 신규유저가 하루 안에 결제로 넘어가는 비율, 결제까지 보통 몇 분 정도가 소요되는지 (신규유저의 가입일, 최초 구매일)

```SQL
select customer_id
	, min(purchased_at) as purchased_at
from sqlprac.tbl_purchase
group by 1
```

- 가입일에서 구매일 빼주면 결제로 넘어가는 일자 
  
```SQL
select A.customer_id
	, A.created_at
    , B.customer_id as paying_user
    , B.purchased_at
    
from sqlprac.tbl_customer A

left join (
	select customer_id
		, min(purchased_at) as purchased_at
        from sqlprac.tbl_purchase B
        group by 1) B

on A.customer_id = B.customer_id
and B.purchased_at < A.created_at + interval 1 day

where A.created_at >= '2020-07-01'
	and A.created_at < '2020-08-01'
```

- null 
  - 한번도 결제 한적이 없는 고객
  - 결제는 했으나 하루 안에 결제로 넘어가지 않아서

```SQL
select A.customer_id
  , A.created_at
  , B.customer_id as paying_user
  , B.purchased_at
  , time_to_sec(timediff(B.purchased_at, A.created_at)) / 3600 as diff_hour
  
from sqlprac.tbl_customer A

left join (
  select customer_id
    , min(purchased_at) as purchased_at
    from sqlprac.tbl_purchase B
    group by 1) B

on A.customer_id = B.customer_id
and B.purchased_at < A.created_at + interval 1 day

where A.created_at >= '2020-07-01'
  and A.created_at < '2020-08-01'
```

```SQL
with rt_tbl as (
	select A.customer_id
		, B.customer_id as paying_user
		, time_to_sec(timediff(B.purchased_at, A.created_at)) / 3600 as diff_hour
		
	from sqlprac.tbl_customer A

	left join (
		select customer_id
			, min(purchased_at) as purchased_at
			from sqlprac.tbl_purchase B
			group by 1) B

	on A.customer_id = B.customer_id
	and B.purchased_at < A.created_at + interval 1 day

	where A.created_at >= '2020-07-01'
		and A.created_at < '2020-08-01'
)

select round(count(paying_user) / count(customer_id) * 100,2)
from rt_tbl

union all
select avg(diff_hour)
from rt_tbl
```


## 유저의 재방문률이 높은서비스인가? 이를 파악하기 위해 7월 기준 Day1 Retention이 어떤지 구하고 추세를 보기위해 Daily로 추출
### Retention: 시간이 지날수록 얼마나 많은 유저가 제품이나 서비스로 다시 돌아가느지?
### N-day Retention: n=1,2,3,4,....~

- 셀프조인
- A당일, B다음날
- 당일과 다음날을 당일 기준으로 맵핑을 시켜 조건을 아이디가 같고 당일과 다음날의 -1데이 해준값이 같은게 잇는지

```SQL
select *
from sqlprac.tbl_visit A

left join sqlprac.tbl_visit B
on A.customer_id = B.customer_id
and date_format(A.visited_at - interval 9 hour, '%Y-%m-%d') = date_format(B.visited_at - interval 9 hour - interval 1 day, '%Y-%m-%d')

where A.visited_at >= '2020-07-01'
	and A.visited_at < '2020-08-01'
```

```SQL
select date_format(A.visited_at - interval 9 hour, '%Y-%m-%d') as d_date 
	, count(distinct A.customer_id) as active_user
	, count(distinct B.customer_id) as retained_user
    , count(distinct B.customer_id) / count(distinct A.customer_id) as retention
from sqlprac.tbl_visit A

left join sqlprac.tbl_visit B
on A.customer_id = B.customer_id
and date_format(A.visited_at - interval 9 hour, '%Y-%m-%d') = date_format(B.visited_at - interval 9 hour - interval 1 day, '%Y-%m-%d')

where A.visited_at >= '2020-07-01'
	and A.visited_at < '2020-08-01'

group by 1
```

## 2020년 7월 신규유저가 많은지? 기존유저가 많은지? 가입기간별로 고객 분포가 어떤지 DAU기준으로
- tbl_visit 일자별로 고객의 last_visit - created_at = service age

```SQL
select date_format(A.visited_at - interval 9 hour, '%Y-%m-%d') as d_date
	, A.customer_id
    , max(A.visited_at) as last_visit
from sqlprac.tbl_visit as A

group by 1,2
```

```SQL
select date_format(A.visited_at - interval 9 hour, '%Y-%m-%d') as d_date
	, A.customer_id
    , B.created_at as d_joined
    , max(A.visited_at) as last_visit
    , datediff(max(A.visited_at), B.created_at) as date_diff
from sqlprac.tbl_visit A

left join sqlprac.tbl_customer B
on A.customer_id = B.customer_id

where A.visited_at >= '2020-07-01'
	and A.visited_at < '2020-08-01'

group by 1,2,3
```


```SQL
with tbl_visit_by_joined as(
	select date_format(A.visited_at - interval 9 hour, '%Y-%m-%d') as d_date
		, A.customer_id
		, B.created_at as d_joined
		, max(A.visited_at) as last_visit
		, datediff(max(A.visited_at), B.created_at) as date_diff
	from sqlprac.tbl_visit A

	left join sqlprac.tbl_customer B
	on A.customer_id = B.customer_id

	where A.visited_at >= '2020-07-01'
		and A.visited_at < '2020-08-01'

	group by 1,2,3
)

select A.d_date
	, case when A.date_diff >= 730 then '2년이상'
		   when A.date_diff >= 365 then '1년 이상'
           when A.date_diff >= 183 then '6개월 이상'
           when A.date_diff >= 91 then '3개월 이상'
           when A.date_diff >= 30 then '1개월 이상'
           else '1개월 미만'
           end as segment
	, count(A.customer_id)
from tbl_visit_by_joined A
group by 1, 2
order by 1, 2
```


```SQL
with tbl_visit_by_joined as(
	select date_format(A.visited_at - interval 9 hour, '%Y-%m-%d') as d_date
		, A.customer_id
		, B.created_at as d_joined
		, max(A.visited_at) as last_visit
		, datediff(max(A.visited_at), B.created_at) as date_diff
	from sqlprac.tbl_visit A

	left join sqlprac.tbl_customer B
	on A.customer_id = B.customer_id

	where A.visited_at >= '2020-07-01'
		and A.visited_at < '2020-08-01'

	group by 1,2,3
)

select A.d_date
	, case when A.date_diff >= 730 then '2년이상'
		   when A.date_diff >= 365 then '1년 이상'
           when A.date_diff >= 183 then '6개월 이상'
           when A.date_diff >= 91 then '3개월 이상'
           when A.date_diff >= 30 then '1개월 이상'
           else '1개월 미만'
           end as segment
	, B.all_users 
	, count(A.customer_id) as users
    , round(count(A.customer_id) / B.all_users * 100,2) as per
from tbl_visit_by_joined A
left join (
	select d_date
		, count(customer_id) as all_users
    from tbl_visit_by_joined
    group by 1) B
on A.d_date = B.d_date


group by 1, 2, 3
order by 1, 2


-- 직접 체크 해보기 select 138 + 71 + 162 + 146 + 73 + 91
```

# Date Format 함수

```SQL
SELECT NOW();
SELECT CURRENT_DATE();
SELECT EXTRACT(MONTH FROM ʻ2021-01-01’);
SELECT DAY(ʻ2021-01-01’);
SELECT DATE_ADD(ʻ2021-01-01’, INTERVAL 7 DAY);
SELECT DATE_SUB(ʻ2017-06-15’, INTERVAL 7 DAY);
SELECT DATEDIFF("2017-06-25", "2017-06-15");
SELECT TIMEDIFF("2021-01-25 12:10:00", "2021-01-25 10:10:00");
SELECT DATE_FORMAT(NOW(), “%Y-%m-%d”);
```



## 2020년 7월 평균 DAU, Active User 수가 추세 증가하는 추세인지?

```SQL
select date_format(visited_at, '%Y-%m-%d') as date_at,
		count(distinct customer_id)
from sqlprac.tbl_visit
where visited_at >= '2020-07-01'
	and visited_at < '2020-08-01'
group by 1
```

```SQL
select *,
	date_format(visited_at - interval 9 hour, '%Y-%m-%d') as date_at,
    date_format(visited_at, '%Y-%m-%d') as date_at2
from sqlprac.tbl_visit
where visited_at >= '2020-07-01'
	and visited_at < '2020-08-01'
```

- KST 를 제대로 명시안해서 UTC로 나오는듯

```SQL
select 
	date_format(visited_at - interval 9 hour, '%Y-%m-%d') as date_at,
	count(distinct customer_id)
from sqlprac.tbl_visit
where visited_at >= '2020-07-01'
	and visited_at < '2020-08-01'
group by 1
order by 1
```

```SQL
-- DAU
select avg(users)
from(
select 	date_format(visited_at - interval 9 hour, '%Y-%m-%d') as date_at,
		count(distinct customer_id) as users
from sqlprac.tbl_visit
where visited_at >= '2020-07-01'
	and visited_at < '2020-08-01'
Group by 1
order by 1) foo
```

## 2020년 7월 평균 WAU (Weekly Active Users)

```SQL
select 	date_format(visited_at - interval 9 hour, '%Y-%m-%U') as date_at,
		count(distinct customer_id) as users
from sqlprac.tbl_visit
where visited_at >= '2020-07-05'
	and visited_at < '2020-07-26'
Group by 1
order by 1
```

```SQL
-- MAU
select avg (users)
from(
select 	date_format(visited_at - interval 9 hour, '%Y-%m-%U') as date_at,
		count(distinct customer_id) as users
from sqlprac.tbl_visit
where visited_at >= '2020-07-05'
	and visited_at < '2020-07-26'
Group by 1
order by 1) foo
```

- 월마다 주가 다를수 있음
- 달력보면 WAU는 일요일부터 시작
  - 2020년 7월의 경우 5일부터 일요일 시작 26일 일요일 끝


## 2020년 7월 Daily Revenue는 증가하는 추세? 평균 Daily Revenue
## 2020년 7월의 평균 Weekly Revenue

```SQL
select 	date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as date_at,
	sum(price)
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
Group by 1
order by 1
```

```SQL
-- Daily Revenue
select avg(revenue)
from (
select 	date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as date_at,
	sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
Group by 1
order by 1) foo
```

```SQL
select 	date_format(purchased_at - interval 9 hour, '%Y-%m-%U') as date_at,
	sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-05'
	and purchased_at < '2020-07-26'
Group by 1
order by 1
```

```SQL
-- Weekly Revenue
select avg(revenue)
from (
select 	date_format(purchased_at - interval 9 hour, '%Y-%m-%U') as date_at,
	sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-05'
	and purchased_at < '2020-07-26'
Group by 1
order by 1) foo
```

## 2020년 7월 요일별 Revenue를 구해. 어느 요일 Revenue가 가장 높고 가장 낮을까?

```SQL
-- 각 요일 결제 금액 평균이 나옴 
select 	date_format(purchased_at - interval 9 hour, '%W') as date_at,
	sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by 1
```

```SQL
select date_format(date_at, '%w') as day_order
      ,date_format(date_at, '%W') as day
	    ,avg(revenue)
from (
select 	date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as date_at,
	sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by 1) foo
group by 1,2
order by 1
```

- 먼저 일별로 매출총합 구한뒤에 이걸 서브쿼리에 넣는다.
- date_at컬럼을 요일 베이스로 다시 포매팅 해줘야함


## 2020년 7월 시간대별 Revenue를 구해 어느 시간대 Revenue가 가장 높고 낮을까?

```SQL
-- 일별 총매출
select 	date_format(purchased_at - interval 9 hour, '%W') as date_at,
	sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by 1
```

```SQL
select hour_at
	,  avg(revenue)
from(
select date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as date_at
	 , date_format(purchased_at - interval 9 hour, '%H') as hour_at
	 , sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by 1, 2) foo
group by 1
order by 2 desc
```

## 2020년 7월의 요일 및 시간대별 Revenue

```SQL
select 	date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as date_at
		, date_format(purchased_at - interval 9 hour, '%W') as dayofweek_at
		, date_format(purchased_at - interval 9 hour, '%H') as hour_at
		, sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by 1, 2, 3
```

```SQL
select dayofweek_at
	, hour_at
    , avg(revenue)
from(
select 	date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as date_at
		, date_format(purchased_at - interval 9 hour, '%W') as dayofweek_at
		, date_format(purchased_at - interval 9 hour, '%H') as hour_at
		, sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
	and purchased_at < '2020-08-01'
group by 1, 2, 3) foo
group by 1,2
order by 3 desc
```
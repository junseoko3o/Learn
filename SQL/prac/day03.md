# 유저 세그먼트별 분석
## 전체 유저의 Demographic을 알려줘. 성/ 연령별로 유저 숮자 알려줘
## 어느 세그먼트가 가장 숫자가 많나? 참고로 기타 성별은 하나로, 연령은 5세 단위로 적당히 묶고 유저 수가 높은 순서대로 보여줘

```SQL
select case when gender is null then 'Others'
			else gender end as gender
	, count(*)
from sqlprac.tbl_customer
group by 1
```
- 종종 Others가 안먹히는 경우가 있음 (더티한 데이터)

```SQL
select case when length(gender) < 1 then 'Others'
			else gender end as gender
	, count(*)
from sqlprac.tbl_customer
group by 1
```
- length 로 해결

```SQL
select case when length(gender) < 1 then 'Others'
			else gender end as gender
	, case when age <= 15 then '15세 이하'
		   when age <= 20 then '16-20세'
		   when age <= 25 then '21-25세'
           when age <= 30 then '26-30세'
           when age <= 35 then '31-35세'
           when age <= 40 then '36-40세'
           when age <= 45 then '41-45세'
           when age >= 46 then '46세 이상'
           end as age
		, count(*)
from sqlprac.tbl_customer
group by 1, 2
order by 3 desc
```

## 성,연령을 남성 (25-29세) 같이 통합하고, 각 성/연령이 전체 고객에서 얼마나 차지하는지 분포(%) 를 알려줘. 분포가 높은 순으로

```SQL
select case when length(gender) < 1 then '기타'
			when gender = 'Others' then '기타'
      when gender = 'M' then '남성'
			when gender = 'F' then '여성'
			end as gender
	, case when age <= 15 then '15세 이하'
		   when age <= 20 then '16-20세'
		   when age <= 25 then '21-25세'
           when age <= 30 then '26-30세'
           when age <= 35 then '31-35세'
           when age <= 40 then '36-40세'
           when age <= 45 then '41-45세'
           when age >= 46 then '46세 이상'
           end as age
		, count(*)
from sqlprac.tbl_customer
group by 1, 2
order by 3 desc
```

- concat 함수로 텍스트 묶기
  

```SQL
select concat(case when length(gender) < 1 then '기타'
			when gender = 'Others' then '기타'
            when gender = 'M' then '남성'
			when gender = 'F' then '여성'
			end
	, "("
	, case when age <= 15 then '15세 이하'
		   when age <= 20 then '16-20세'
		   when age <= 25 then '21-25세'
           when age <= 30 then '26-30세'
           when age <= 35 then '31-35세'
           when age <= 40 then '36-40세'
           when age <= 45 then '41-45세'
           when age >= 46 then '46세 이상'
           end 
   , ")") as segement
		, count(*)
from sqlprac.tbl_customer
group by 1
order by 2 desc
```

- 분포

```SQL
select concat(case when length(gender) < 1 then '기타'
			when gender = 'Others' then '기타'
            when gender = 'M' then '남성'
			when gender = 'F' then '여성'
			end
	, "("
	, case when age <= 15 then '15세 이하'
		   when age <= 20 then '16-20세'
		   when age <= 25 then '21-25세'
           when age <= 30 then '26-30세'
           when age <= 35 then '31-35세'
           when age <= 40 then '36-40세'
           when age <= 45 then '41-45세'
           when age >= 46 then '46세 이상'
           end 
   , ")") as segement
		, round(count(*) / (select count(*) from sqlprac.tbl_customer) * 100,2) as per
from sqlprac.tbl_customer
group by 1
order by 2 desc
```

-  select 문에 쿼리 넣기 = 스칼라 서브쿼리 // 값이 하나만 딱있을때 


## 2020년 7월, 성별에 따라 총 구매 건수와 총 Revenue 구하기, 이전 처럼 남녀 이외의 성별은 하나로 묶기

```SQL
select A.*
	, B.gender
from sqlprac.tbl_purchase A
left join sqlprac.tbl_customer B
on A.customer_id = B.customer_id
```
- 조인할때 별칭은 해주는게 좋음
- 매칭되는 키컬럼이 뭔지 정의 해줘야함 안그러면 모든 조합을 다 계산해서 부하가 일어날수 있음


```SQL
select case when length(gender) < 1 then '기타'
			when gender = 'Others' then '기타'
            when gender = 'M' then '남성'
			when gender = 'F' then '여성'
			end as gender
       , count(*) as cnt
       , sum(price) as revenue
from sqlprac.tbl_purchase A
left join sqlprac.tbl_customer B
on A.customer_id = B.customer_id

where A.purchased_at >= '2020-07-01'
and A.purchased_at < '2020-08-01'
group by 1
```

## 2020년 7월의 성별/연령대에 따라 구매건수와 , 총 Revenue를 구해라

```SQL
select case when length(B.gender) < 1 then '기타'
			when B.gender = 'Others' then '기타'
            when B.gender = 'M' then '남성'
			when B.gender = 'F' then '여성'
			end as gender
		,case when B.age <= 15 then '15세 이하'
			   when B.age <= 20 then '16-20세'
			   when B.age <= 25 then '21-25세'
			   when B.age <= 30 then '26-30세'
			   when B.age <= 35 then '31-35세'
			   when B.age <= 40 then '36-40세'
			   when B.age <= 45 then '41-45세'
			   when B.age >= 46 then '46세 이상'
               end as age_group
       , count(*) as cnt
       , sum(price) as revenue
       
from sqlprac.tbl_purchase A
left join sqlprac.tbl_customer B
on A.customer_id = B.customer_id

where A.purchased_at >= '2020-07-01'
and A.purchased_at < '2020-08-01'
group by 1,2
order by 3 desc
```

## 2020년 7월 일별 매출의 전일 대비 증감폭, 증감률

```SQL
select *
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
and purchased_at < '2020-08-01'
```

```SQL
-- 일별 매출
select date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as d_date
	, sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
and purchased_at < '2020-08-01'

group by 1
```

- 임시테이블 테이블 정의 with 문

```SQL
with tbl_revenue as(
select date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as d_date
	, sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
and purchased_at < '2020-08-01'

group by 1
)

select * 
from tbl_revenue
```

- 증감폭
- lag 함수 행순서관련 함수 (전일)

```SQL
with tbl_revenue as(
select date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as d_date
	, sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
and purchased_at < '2020-08-01'

group by 1
)

select * 
	, revenue - lag(revenue) over(order by d_date asc) 
from tbl_revenue
```

- 증감률
  
```SQL
with tbl_revenue as(
select date_format(purchased_at - interval 9 hour, '%Y-%m-%d') as d_date
	, sum(price) as revenue
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
and purchased_at < '2020-08-01'

group by 1
)

select * 
	, revenue - lag(revenue) over(order by d_date asc) as diff_revenue
    , round((revenue - lag(revenue) over(order by d_date asc)) / lag(revenue) over(order by d_date asc) * 100,2) as change_revenue
from tbl_revenue
```


## 메출 관련 추가 분석
## 일별로 많이 구매한 고객들한테 소정의 선물, 7월에 일별로 구매 금액 기준으로 가장 많이 지출한 고객 TOP3뽑아줘

- 순위 함수

```SQL
select *
from (
select date_format(purchased_at - interval 9 hour, '%Y-%m-%d') d_date 
	, customer_id
	, sum(price)
    , dense_rank() over (partition by date_format(purchased_at - interval 9 hour, '%Y-%m-%d') order by sum(price) desc) as rank_rev
from sqlprac.tbl_purchase
where purchased_at >= '2020-07-01'
and purchased_at < '2020-08-01'
group by 1, 2) foo

where rank_rev < 4
```
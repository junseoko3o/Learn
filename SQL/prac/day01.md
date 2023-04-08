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


-- Write your PostgreSQL query statement below
With month as (
    select to_char(trans_date,'YYYY-MM') as month,
            country, state,amount,id
    from Transactions
)
select month, country,
        count(id) as trans_count,
        count(case when state='approved' then 1 else Null end) as approved_count,
        sum(amount) as trans_total_amount,
        sum(case when state='approved' then amount else 0 end) as approved_total_amount
from month
group by month,country
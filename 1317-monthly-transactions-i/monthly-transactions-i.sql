-- Write your PostgreSQL query statement below
-- With month as (
--     select to_char(trans_date,'YYYY-MM') as month,
--             country, state,amount,id
--     from Transactions
-- )
-- select month, country,
--         count(id) as trans_count,
--         count(case when state='approved' then 1 else Null end) as approved_count,
--         sum(amount) as trans_total_amount,
--         sum(case when state='approved' then amount else 0 end) as approved_total_amount
-- from month
-- group by month,country

SELECT 
    TO_CHAR(trans_date, 'YYYY-MM') AS month,
    country,
    COUNT(id) AS trans_count,
    COUNT(CASE WHEN state = 'approved' THEN 1 END) AS approved_count, -- 顺便提一句：ELSE NULL 可以直接不写，不写默认就是 NULL
    SUM(amount) AS trans_total_amount,
    coalesce(sum(CASE WHEN state = 'approved' THEN amount END),0) as approved_total_amount
FROM Transactions
GROUP BY month, country; -- 直接使用别名进行分组！
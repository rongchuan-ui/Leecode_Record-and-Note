-- Write your PostgreSQL query statement below
select v.customer_id,
    count(*) As count_no_trans
from Visits v
left join Transactions t
on v.visit_id = t.visit_id
where transaction_id is null
group by v.customer_id;

-- select v.customer_id,
--     count(customer_id) As count_no_trans
-- from Visits v
-- left join Transactions t
-- on v.visit_id = t.visit_id
-- where transaction_id is null
-- group by v.customer_id;
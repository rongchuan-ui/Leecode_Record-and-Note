-- Write your PostgreSQL query statement below
-- we check this by calculating the number of products each customer buys
select 
    customer_id
from Customer c
group by c.customer_id
having count(distinct c.product_key) = (
    select count(*)
    from Product
);

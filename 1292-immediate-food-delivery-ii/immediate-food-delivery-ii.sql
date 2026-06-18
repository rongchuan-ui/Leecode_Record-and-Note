-- Write your PostgreSQL query statement below
with first_order_date as (
    select customer_id,
            min(order_date) as first_order_date
    from Delivery
    group by customer_id
)
select 
    round(count(f.customer_id) filter (where d.order_date=d.customer_pref_delivery_date)::numeric / count(f.customer_id)::numeric*100,2) as immediate_percentage
from Delivery d
inner join first_order_date f
on f.first_order_date=d.order_date and d.customer_id=f.customer_id

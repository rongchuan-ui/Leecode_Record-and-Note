-- Write your PostgreSQL query statement below
--  with purchase as (
--     Select p.product_id,
--         p.price,
--         u.units
--     from Prices p
--     left join UnitsSold u
--     on p.product_id = u.product_id and (
--     ( (p.end_date - p.start_date)>= (u.purchase_date - p.start_date) and (u.purchase_date - p.start_date) >=0 ) 
--         or u.purchase_date is null )
--  ),
--  Revenue AS (
--     select product_id,
--             sum(units)  As sum_units,
--             sum(price*units) As revenue
--     from purchase
--     group by product_id
--  )
-- select product_id,
--     case when sum_units is null then 0 
--         else ROUND(revenue::NUMERIC/ sum_units::NUMERIC, 2)
--     end as average_price
-- from Revenue;


 with purchase as (
    Select p.product_id,
        sum(u.units)  As sum_units,
        sum(p.price*u.units) As revenue
    from Prices p
    left join UnitsSold u
    on p.product_id = u.product_id and (u.purchase_date between p.start_date and p.end_date)
    group by p.product_id
 )
select product_id,
    case when sum_units is null then 0 
        else ROUND(revenue::NUMERIC/ sum_units::NUMERIC, 2)
    end as average_price
from purchase;
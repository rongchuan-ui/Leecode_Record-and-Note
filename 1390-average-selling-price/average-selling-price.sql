-- Write your PostgreSQL query statement below
 with purchase as (
    Select p.product_id,
        p.price,
        case when u.units is null then 0 
            else u.units
        End
    from Prices p
    left join UnitsSold u
    on p.product_id = u.product_id
    where 
        ( (p.end_date - p.start_date)>= (u.purchase_date - p.start_date) and (u.purchase_date - p.start_date) >=0 ) 
        or u.purchase_date is null 
 ),
 Revenue AS (
    select product_id,
            sum(units) As sum_units,
            sum(price*units) As revenue
    from purchase
    group by product_id
 )
select product_id,
    case when sum_units =0 then 0 
        else ROUND(revenue::NUMERIC/ sum_units::NUMERIC, 2)
    end as average_price
from Revenue;
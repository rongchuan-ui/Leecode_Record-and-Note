-- Write your PostgreSQL query statement below
-- with first_order_date as (
--     select customer_id,
--             min(order_date) as first_order_date
--     from Delivery
--     group by customer_id
-- )
-- select 
--     round(count(f.customer_id) filter (where d.order_date=d.customer_pref_delivery_date)::numeric / count(f.customer_id)::numeric*100,2) as immediate_percentage
-- from Delivery d
-- inner join first_order_date f
-- on f.first_order_date=d.order_date and d.customer_id=f.customer_id

-- WITH ranked_orders AS (
--     SELECT *,
--            ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS rn
--     FROM Delivery
-- )
-- SELECT 
--     ROUND(
--         AVG((order_date = customer_pref_delivery_date)::INT) * 100, 
--         2
--     ) AS immediate_percentage
-- FROM ranked_orders
-- WHERE rn = 1;

SELECT 
    ROUND(
        COUNT(*) FILTER (WHERE order_date = customer_pref_delivery_date)::NUMERIC 
        / COUNT(*)::NUMERIC * 100, 
        2
    ) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) 
    FROM Delivery 
    GROUP BY customer_id
);
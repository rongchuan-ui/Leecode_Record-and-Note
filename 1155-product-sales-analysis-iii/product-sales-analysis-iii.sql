-- Write your PostgreSQL query statement below
SELECT 
    product_id, 
    year AS first_year, 
    sum(quantity) as quantity, 
    price
FROM 
    Sales
WHERE 
    (product_id, year) IN (
        SELECT product_id, MIN(year)
        FROM Sales
        GROUP BY product_id
    )
group by product_id, year,price;

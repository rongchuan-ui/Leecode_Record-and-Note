-- Write your PostgreSQL query statement below
-- SELECT lag.id AS Id
-- FROM (
--     SELECT id, 
--            temperature,
--            recordDate,
--            LAG(temperature, 1) OVER (ORDER BY recordDate) AS lag_temperature_1,
--            LAG(recordDate, 1) OVER (ORDER BY recordDate) AS lag_date_1
--     FROM Weather
-- ) lag
-- WHERE lag.lag_temperature_1 < lag.temperature
--   AND (lag.recordDate - lag.lag_date_1) = 1;

-- with lag as (
--     SELECT id, 
--            temperature,
--            recordDate,
--            LAG(temperature, 1) OVER (ORDER BY recordDate) AS lag_temperature_1,
--            LAG(recordDate, 1) OVER (ORDER BY recordDate) AS lag_date_1
--     FROM Weather
-- )
-- select id
-- from lag
-- where lag_temperature_1>temperature and lag_date_1+1=recordDate;

SELECT 
    w1.id
FROM 
    Weather w1
JOIN 
    Weather w2
ON 
    w1.recordDate= w2.recordDate+1
and 
    w1.temperature > w2.temperature;
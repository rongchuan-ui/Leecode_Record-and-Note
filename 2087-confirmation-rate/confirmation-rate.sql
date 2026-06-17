-- Write your PostgreSQL query statement below
-- With total_confirm as (
--     select user_id,
--            count(*) as total_request,
--            sum(case when action='confirmed' then 1 else 0 end) as total_confirmed_request
--     from Confirmations
--     group by user_id
-- )
-- select s.user_id,
--         case when t.user_id is null then 0 
--              else round(t.total_confirmed_request::numeric/t.total_request::numeric,2) end as confirmation_rate
-- from Signups s
-- left join total_confirm t
-- on s.user_id=t.user_id;

SELECT 
    s.user_id,
    ROUND(COALESCE(AVG(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c 
ON s.user_id = c.user_id
GROUP BY s.user_id;

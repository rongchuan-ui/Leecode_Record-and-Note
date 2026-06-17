-- Write your PostgreSQL query statement below
-- with run_time as (
--     select a1.machine_id,
--         a1.process_id,
--         sum(a2.timestamp - a1.timestamp) AS total_run_time
--     from Activity a1
--     join Activity a2
--     on (a1.machine_id = a2.machine_id) and
--        (a1.process_id = a2.process_id) and
--        (a1.activity_type != a2.activity_type)
--     where a1.activity_type = 'start'
--     group by a1.machine_id, a1.process_id
-- )
-- select machine_id,
--         round(sum(total_run_time)::numeric/count(machine_id)::numeric,3) as processing_time
-- from run_time
-- group by machine_id;

SELECT 
    machine_id,
    ROUND(
        SUM(CASE WHEN activity_type = 'end' THEN timestamp ELSE -timestamp END)::numeric 
        / COUNT(DISTINCT process_id)::numeric, 
        3
    ) AS processing_time
FROM Activity
GROUP BY machine_id;
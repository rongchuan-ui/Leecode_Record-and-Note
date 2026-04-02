-- Write your PostgreSQL query statement below
-- Create view prev_table As
-- select 
--     user_id,
--     activity_type,
--     avg(activity_duration) as avg_duration
-- from UserActivity
-- where user_id not in (
--     select user_id
--     from UserActivity
--     where activity_type = 'cancelled'
-- )
-- group by activity_type, user_id;

-- Create View trial_table As
-- select 
--     user_id,
--     avg_duration As trial_avg_duration
-- from prev_table
-- where activity_type = 'free_trial';

-- Create View paid_table As
-- select 
--     user_id,
--     avg_duration As paid_avg_duration
-- from prev_table
-- where activity_type = 'paid';

-- SELECT
--     t.user_id,
--     t.trial_avg_duration,
--     p.paid_avg_duration
-- FROM trial_table AS t
-- LEFT JOIN paid_table AS p
-- ON t.user_id = p.user_id;

select
    user_id,
    round(avg(case when activity_type = 'free_trial' then activity_duration end ),2) as trial_avg_duration,
    round(avg(case when activity_type = 'paid' then activity_duration end ),2) as paid_avg_duration
from UserActivity
group by user_id
having 
    count(case when activity_type = 'free_trial' then 1 end)>0
    and
    count(case when activity_type = 'paid' then 1 end)>0
order by user_id




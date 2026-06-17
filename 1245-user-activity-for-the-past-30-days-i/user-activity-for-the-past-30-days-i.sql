-- Write your PostgreSQL query statement below
select activity_date as day,
    count(distinct user_id) as active_users
from Activity
where (activity_date between ('2019-07-27'::date - interval '29 days') and '2019-07-27'::date)
group by activity_date;
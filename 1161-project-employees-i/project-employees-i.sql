-- Write your PostgreSQL query statement below
select p.project_id,
    round(sum(e.experience_years)::Numeric / count(distinct e.employee_id)::Numeric,2) as average_years
from Project p
inner join Employee e
on p.employee_id=e.employee_id
group by p.project_id;
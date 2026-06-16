-- Write your PostgreSQL query statement below
select e.name, en.unique_id
from Employees e
left join EmployeeUNI en
on e.id = en.id;
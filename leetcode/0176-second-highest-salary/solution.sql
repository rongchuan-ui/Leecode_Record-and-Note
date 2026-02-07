# Write your MySQL query statement below
-- Create Table if not exists Employee(
--     id INT primary key,
--     salary INT not NUll
-- )
-- Truncate table Employee
-- Insert into Employee Values
-- (1,100),
-- (2,200),
-- (3,300);

-- -- first way:
select (
    select distinct salary
    from Employee
    order by salary DESC
    limit 1 offset 1
) AS SecondHighestSalary;
 
-- second way:

-- select max(r.salary) AS SecondHighestSalary
-- From (
--     select salary, 
--             DENSE_RANK()Over(order by salary DESC) as rnk
--     From Employee
-- ) r
-- where rnk=2;

-- third method:
-- select max(salary<max(salary)) As SecondHighestSalary
-- From Employee
-- limit 1; -- wrong

-- select MAX(salary) AS SecondHighestSalary
-- From Employee
-- Where salary < (
--     Select MAX(salary)
--     from employee
-- );



-- Write your PostgreSQL query statement below
Select distinct a.num As ConsecutiveNums
From(
    Select *,
        Lag(num,1) over(order by id) As next1,
        Lag(num,2) over (order by id) As next2
    From Logs
) a
where num = next1 and next1 = next2 ;

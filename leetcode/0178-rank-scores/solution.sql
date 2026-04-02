-- Write your PostgreSQL query statement below
select a.score, a.rank
From(
    select *,
           dense_rank()Over(order by score desc) as rank
    From Scores
) a;

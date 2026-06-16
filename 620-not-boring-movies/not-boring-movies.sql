-- Write your PostgreSQL query statement below
-- select id, movie, description, rating
-- from Cinema
-- where mod(id,2) !=0 and description != 'boring'
-- order by rating desc;

select id, movie, description, rating
from Cinema
where id-(id/2)*2 !=0 and description != 'boring'
order by rating desc;
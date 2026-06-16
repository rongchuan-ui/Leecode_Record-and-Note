-- Write your PostgreSQL query statement below
select v.author_id As id
from (
    select author_id
    from Views
    where author_id = viewer_id
) v
group by v.author_id
having count(v.author_id) >=1
order by id ASC;

-- select distinct author_id As id
-- from Views
-- where author_id = viewer_id
-- order by author_id asc;
-- Write your PostgreSQL query statement below
-- select article_id As id
-- from (
--     select article_id
--     from Views
--     where article_id = viewer_id
-- ) author_view v
-- group by v.article_id
-- having count(v.article_id) >=1;

select distinct author_id As id
from Views
where author_id = viewer_id
order by author_id asc;
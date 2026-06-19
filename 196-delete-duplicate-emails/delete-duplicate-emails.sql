-- Write your PostgreSQL query statement below
-- Delete from Person p1
-- using Person p2
-- where p1.email=p2. email
-- and p1.id>p2.id;

DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);
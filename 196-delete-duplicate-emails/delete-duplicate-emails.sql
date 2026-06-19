-- Write your PostgreSQL query statement below
-- Delete from Person p1
-- using Person p2
-- where p1.email=p2. email
-- and p1.id>p2.id;

-- DELETE FROM Person
-- WHERE id NOT IN (
--     SELECT MIN(id)
--     FROM Person
--     GROUP BY email
-- );

DELETE FROM Person
WHERE id IN (
    SELECT id 
    FROM (
        SELECT id, ROW_NUMBER() OVER(PARTITION BY email ORDER BY id) AS rn
        FROM Person
    ) t
    WHERE rn > 1
);
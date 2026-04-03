-- Write your PostgreSQL query statement below
-- With pre_table As(
--     select 
--         id,
--         student,
--         lead(student,1)over(order by id) As student_x
--     from Seat
--     where id % 2=1
-- )

SELECT
    CASE
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id;

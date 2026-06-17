-- Write your PostgreSQL query statement below
-- select st.student_id, st.student_name, su.subject_name,
--         sum(case when su.subject_name = e. subject_name then 1
--                  when e. subject_name is null then 0
--                  else 0
--         end) as attended_exams
-- from Students st
-- cross join Subjects su
-- left join Examinations e
-- on st.student_id = e.student_id
-- group by st.student_id, st.student_name, su.subject_name
-- order by st.student_id, su.subject_name;

SELECT 
    st.student_id, 
    st.student_name, 
    su.subject_name, 
    COUNT(e.subject_name) AS attended_exams 
FROM Students st
CROSS JOIN Subjects su
LEFT JOIN Examinations e 
    ON st.student_id = e.student_id 
    AND su.subject_name = e.subject_name -- 把科目关联直接写在 ON 后面
GROUP BY st.student_id, st.student_name, su.subject_name
ORDER BY st.student_id, su.subject_name;
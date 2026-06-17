-- Write your PostgreSQL query statement below
select st.student_id, st.student_name, su.subject_name,
        sum(case when su.subject_name = e. subject_name then 1
                 when e. subject_name is null then 0
                 else 0
        end) as attended_exams
from Students st
cross join Subjects su
left join Examinations e
on st.student_id = e.student_id
group by st.student_id, st.student_name, su.subject_name
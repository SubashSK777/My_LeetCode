# Write your MySQL query statement below
select eu.unique_id, e.name
from Employees e
left join EmployeeUNI eu on eu.id = e.id;
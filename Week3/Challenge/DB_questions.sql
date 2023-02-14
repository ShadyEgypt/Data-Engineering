--**This file contains the problems you need to answer by writing and running the required queries:**


-- 1) Find the Number of Employees with different degrees
select degree, count(*) from education
    GROUP BY degree;

-- 2) Find the total number of employees per Department
SELECT department.department_name, COUNT(employee.employee_id) AS SUM_EMP from employee, department
    WHERE employee.department_id = department.department_id
    GROUP BY (department.department_name);

-- 3) Find all employees whose hourly_pay is $30. Sort them descendingly.
SELECT first_name, last_name, hourly_pay
from employee, salary, accountdetails
where employee.employee_id = accountdetails.employee_id AND accountdetails.account_id = salary.account_id AND hourly_pay = 30
ORDER BY first_name, last_name, hourly_pay DESC ;

-- 4) Find the hourly_payment per employee. Sort them descendingly.
SELECT first_name, last_name, hourly_pay
FROM employee, salary, accountdetails
WHERE employee.employee_id = accountdetails.employee_id AND accountdetails.account_id = salary.account_id 
ORDER BY hourly_pay DESC;

-- 5) List the first employee's first name and last name in one column in each department.
-- limit your answer to 5 answers.
-- Hint:
--|-------------------------------------------------|-
--|id	|employee_name		|dept_name				|
--|-----|-------------------|-----------------------|-
--|105	|Anugraha Varkey	|Business Intelligence	|
--|-------------------------------------------------|-
SELECT concat(employee.first_name,' ', employee.last_name) as employee_name, department_name as dept_name
FROM employee, department
where employee.department_id = department.department_id
limit 5;

-- 6) Find the total number of employees per work_location state.
SELECT state, count(*) FROM work_location
GROUP BY state;

-- 7) Find the total number of employees per work_location state in department "Quality Control"
SELECT work_location.state, count(*) AS SUM
FROM work_location
INNER JOIN employee ON work_location.employee_id = employee.employee_id
INNER JOIN department ON employee.department_id = department.department_id
where department.department_name = 'Quality Control'
GROUP BY work_location.state;

-- 8) Find the total number of employees per work_location state per each department. order them
-- by state ascendingly, and by the sum descendingly.
SELECT work_location.state, department.department_name, count(*) as SUM
FROM work_location
INNER JOIN employee ON work_location.employee_id = employee.employee_id
INNER JOIN department ON employee.department_id = department.department_id
GROUP BY work_location.state, department_name
ORDER BY SUM DESC , work_location.state ASC;

-- 9) Find How many work_location(s) have more than 4 employees
SELECT location, state, city FROM work_location
WHERE int_of_employees > 4
ORDER BY location, state;

-- 10) Find the attendance worked hours per employee's first name and last name
SELECT first_name, last_name, hours_worked 
FROM employee, attendance, employee_attendance
WHERE employee.employee_id = employee_attendance.employee_id
AND attendance.attendance_id = employee_attendance.attendance_id;



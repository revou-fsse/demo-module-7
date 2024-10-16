-- create employee table
CREATE TABLE employees (
	employee_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100),
	department_id INT,
	salary DECIMAL(14, 2)
)

-- create department table
CREATE TABLE departments (
	department_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	department_name VARCHAR(100)
)

-- Start id from 100 instead of 1
ALTER TABLE departments
AUTO_INCREMENT = 100

-- create foreign key constraint after creating table
ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES departments(department_id)

-- populate department table
INSERT INTO departments (department_name) VALUES
('Sales'),
('Marketing'),
('IT')
('Data')

-- populate employee table
INSERT INTO employees (first_name, last_name, department_id, salary) VALUES
('John', 'Smith', 101, 60000),
('Alice', 'Johnson', 102, 65000),
('Bob', 'Williams', 101, 62000),
('Emily', 'Brown', 103, 70000)

-- rename table
RENAME TABLE employees TO employee_me

-- add new column to table
ALTER TABLE departments
ADD department_area VARCHAR(100)

-- update column name
ALTER TABLE departments
RENAME COLUMN department_area TO department_areas

-- update column datatype
ALTER TABLE departments
MODIFY COLUMN department_area VARCHAR(101)

-- drop table
ALTER TABLE departments
DROP COLUMN department_area

-- select employees
select * from employees

-- select specific employees
select * from employees
where first_name = 'John'

-- select employee with patterns for searching
select * from employees
where first_name like 'A%'


-- select with aggregate function
select count(employee_id)
from employees

-- select with order
select first_name, last_name
from employees e 
order by first_name

-- select with multiple order
select department_id, first_name, last_name
from employees e 
order by department_id, first_name

-- select with grouping
select department_id, count(employee_id)
from employees e
group by department_id 

-- select with having
select department_id, count(employee_id)
from employees e
group by department_id
having count(employee_id) > 1
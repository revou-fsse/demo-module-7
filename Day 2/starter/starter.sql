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

-- add new column to table

-- update column name

-- update column datatype

-- drop table departments

-- select employees

-- select specific employees where name is John

-- select employee with patterns for searching starting with A


-- select with aggregate function

-- select with order

-- select with multiple order

-- select with grouping

-- select with having
-- create table for services
CREATE TABLE services (
	service_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	service_name VARCHAR(100) NOT NULL,
	price DECIMAL(14, 2) NOT NULL
);

-- Populate the service table
INSERT INTO services (service_name, price) VALUES
('Changing Tires', 200000.00),
('Washing cars', 50000.00),
('Tire spooring', 100000.00),
('Tire balancing', 150000.00);

-- create table for customers
CREATE TABLE customers (
	customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	full_name VARCHAR(100) NOT NULL,
	address VARCHAR(255)
);

-- populate customers table
INSERT INTO customers (full_name) VALUES
('Customer A'),
('Customer B'),
('Customer C'),
('Customer D');


-- create table for outlets
CREATE TABLE outlets (
	outlet_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	outlet_name VARCHAR(100) NOT NULL,
	outlet_location VARCHAR(255) NOT NULL
);


-- populate outlets table
INSERT INTO outlets (outlet_name, outlet_location) VALUES
('Outlet 1', "Palembang"),
('Outlet 2', "Jakarta"),
('Outlet 3', "Medan"),
('Outlet 4', "Bali"),
('Outlet 5', "Berlin");























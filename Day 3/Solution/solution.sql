-- Prepopulate Tables and datas
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Country VARCHAR(50)
);

INSERT INTO Customers (FirstName, LastName, Email, Country) VALUES
('John', 'Doe', 'john.doe@example.com', 'USA'),
('Jane', 'Smith', 'jane.smith@example.com', 'Canada'),
('Tom', 'Hanks', 'tom.hanks@example.com', 'UK');


CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2),
    StockQuantity INT
);

INSERT INTO Products (ProductName, Price, StockQuantity) VALUES
('Laptop', 899.99, 10),
('Smartphone', 699.99, 25),
('Tablet', 299.99, 50);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Orders (CustomerID, ProductID, OrderDate, Quantity) VALUES
(1, 1, '2024-10-01', 1),
(2, 2, '2024-10-05', 2),
(1, 3, '2024-10-10', 1);

-- insert empty customer id data
INSERT INTO Orders (ProductID, OrderDate, Quantity) VALUES
(1, '2024-10-01', 1)


-- produk yang harganya diatas rata-rata menggunakan subquery
select *
from Products p
where p.Price < (select avg(p.Price) 
from Products p)

select * from Products


-- customer who has orders using JOIN
select c.CustomerID, c.FirstName, o.ProductID, o.OrderDate
from Customers c
join Orders o
on c.CustomerID = o.CustomerID


-- customer who has orders using Subquery
select *
from Customers
where CustomerID IN (select DISTINCT CustomerID
from Orders o
where CustomerID IS NOT NULL)


-- Using transaction 
START TRANSACTION;

-- Update value of data in table
UPDATE Customers
SET FirstName = 'Mulyono', LastName = 'Asep'
WHERE FirstName = 'Tom'

-- rollback syntax
rollback;


-- delete syntax
DELETE FROM Customers
WHERE CustomerID = 3


-- Left join syntax
SELECT 
    Customers.CustomerID, 
    Customers.FirstName, 
    Orders.OrderID, 
    Orders.OrderDate 
FROM 
    Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

-- Right join syntax
SELECT 
    Orders.OrderID, 
    Orders.OrderDate, 
    Customers.CustomerID, 
    Customers.FirstName
FROM 
    Orders
RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- Full Join MySQL syntax
SELECT 
    Customers.CustomerID, 
    Customers.FirstName, 
    Orders.OrderID, 
    Orders.OrderDate
FROM 
    Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
UNION
SELECT 
    Customers.CustomerID, 
    Customers.FirstName, 
    Orders.OrderID, 
    Orders.OrderDate
FROM 
    Orders
RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- Explain code using EXPLAIN
explain select * from Customers
where Email = 'john.doe@example.com'

-- Create Index in SQL
CREATE INDEX idx_email ON Customers(Email)

-- Drop index in SQL
DROP INDEX idx_email ON Customers






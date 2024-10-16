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


-- produk yang harganya diatas rata-rata menggunakan subquery


-- customer who has orders using JOIN


-- customer who has orders using Subquery


-- Using transaction 

-- Update value of data in table

-- rollback syntax


-- delete syntax=


-- Left join syntax

-- Right join syntax

-- Full Join MySQL syntax

-- Explain code using EXPLAIN


-- Create Index in SQL


-- Drop index in SQL







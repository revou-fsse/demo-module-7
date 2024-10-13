-- create table transactions with relation to customers and outlets
CREATE TABLE transactions (
	transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	transaction_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	customer_id INT,
	outlet_id INT,
	total_amount DECIMAL(14, 2),
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY (outlet_id) REFERENCES outlets(outlet_id)
);

-- populate transactions table
INSERT INTO transactions (transaction_date, customer_id, outlet_id, total_amount) VALUES
('2024-10-12 10:00:00', 1, 2, 200000),
('2024-10-13 16:00:00', 3, 1, 100000),
('2024-10-14 14:00:00', 2, 1, 500000);


-- create table for transaction items with relation to transactions and services
CREATE TABLE transaction_items (
    transaction_item_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    service_id INT,
    quantity INT DEFAULT 1,
    price DECIMAL(14, 2) NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- populate transaction items table
INSERT INTO transaction_items (transaction_id, service_id, quantity, price) VALUES
(1, 1, 1, 200000),
(2, 3, 1, 100000),
(3, 1, 2, 400000),
(3, 3, 1, 100000);
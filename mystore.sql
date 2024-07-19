CREATE DATABASE IF NOT EXISTS store;
USE store;

-- Remove existing root user if exists
DROP USER IF EXISTS 'root'@'%';

-- Create the table
CREATE TABLE IF NOT EXISTS mystore (
    item_number INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    total_available INT,
    price DECIMAL(10, 2)
);

-- Insert 10 entries into the table
INSERT INTO mystore (item_name, total_available, price) VALUES
('soap1', 100, 1.99),
('soap2', 150, 2.49),
('soap3', 120, 1.79),
('soap4', 200, 2.99),
('soap5', 80, 1.59),
('soap6', 90, 1.89),
('soap7', 110, 2.19),
('soap8', 70, 1.29),
('soap9', 180, 2.79),
('soap10', 250, 3.49);

-- Create user 'root' with password 'password'
CREATE USER 'root'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON store.* TO 'root'@'%';
FLUSH PRIVILEGES;

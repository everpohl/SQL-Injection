-- Run once in Workbench as the local database administrator.
CREATE DATABASE course_sql_demo_v00 CHARACTER SET utf8mb4;
USE course_sql_demo_v00;
CREATE TABLE users (
  user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(64) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  email VARCHAR(254) NOT NULL UNIQUE,
  role VARCHAR(20) NOT NULL
);
CREATE TABLE products (
  product_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(500) NOT NULL,
  price DECIMAL(10,2) NOT NULL CHECK (price >= 0)
);
CREATE TABLE private_records (
  record_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  title VARCHAR(100) NOT NULL,
  secret_value VARCHAR(255) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);
START TRANSACTION;
INSERT INTO users (user_id, username, password_hash, email, role) VALUES
(1, 'maya', 'pbkdf2_sha256$600000$38b3c8915843dd3e6cdc83d21af0b365$882f31d0d7da28d523f87a8919d24d1bd16f7c6d9acbef01a028af8a35bc6ae0', 'maya@example.test', 'user'),
(2, 'owen', 'pbkdf2_sha256$600000$34ff32d2a6594ffb5cb5848f911bceff$826b23e702af9f088f8de2d67391136207ff91fe54b0376984818100f65cd302', 'owen@example.test', 'user'),
(3, 'riley', 'pbkdf2_sha256$600000$6eaa768516377a6c79333dfe0716a407$714e470ce70fca64d86647cc8f625506fa39f9eeeff96a090d4a7cf636109a05', 'riley@example.test', 'admin');
INSERT INTO products (product_id, name, description, price) VALUES
(1,'Notebook','Grid paper',4.50),(2,'Desk lamp','Adjustable lamp',18.95),(3,'Pen','Blue ink',1.25);
INSERT INTO private_records (record_id,user_id,title,secret_value) VALUES
(1,1,'Locker note','DEMO-V00-LOCKER'),(2,2,'Pickup code','DEMO-PICKUP-BRAVO');
COMMIT;

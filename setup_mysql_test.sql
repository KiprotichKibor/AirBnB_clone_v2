-- Creates database hbnb_test_db and user hbnb_test
-- assign all privileges to hbnb_test in hbnb_test_db
-- assign readonly privileges to hbnb_test in performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT  ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

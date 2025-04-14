-- Database: public

-- -- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = michaelfellous
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE items (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     price DECIMAL(10, 2) NOT NULL
-- );

-- INSERT INTO items (name, price) VALUES
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80);


-- CREATE TABLE customers (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL
-- );

-- INSERT INTO customers (first_name, last_name) VALUES
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');

-- select * from customers, items;

-- select * from customers, items where price > 80;

-- select * from customers, items where price <= 300;

-- select * from customers where last_name = 'Smith';

-- select * from customers where last_name = 'Jones';

-- select * from customers where first_name != 'Scott';

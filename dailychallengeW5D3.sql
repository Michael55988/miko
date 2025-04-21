-- Database: dailychallengeW5D3

-- DROP DATABASE IF EXISTS "dailychallengeW5D3";

-- CREATE DATABASE "dailychallengeW5D3"
--     WITH
--     OWNER = michaelfellous
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;


-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab



-- i want to know how many id from the first table (nickname ft) is not define as null in the second table
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )


-- how many id of ft is not define in the second table as id=5
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )


--  counts how many lignes of ft dont has their id in second table
    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )


-- counts how many id in ft are not in second table and ignoring the null
	  -- SELECT COUNT(*) 
   --  FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

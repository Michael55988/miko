-- -- Database: bootcamp

-- -- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = michaelfellous
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- create table students (
-- id serial primary key,
-- last_name varchar (100) not null,
-- firs_name varchar (100) not null);

-- insert into students (last_name, firs_name) values
-- ('Benichou','Marc'),
-- ('Cohen', 'Yoan'),
-- ('Benichou', 'Lea'),
-- ('Dux', 'Amelie'),
-- ('Grez', 'David'),
-- ('Simpson', 'Omer');

-- select * from students;

-- alter table students add column birth_date date;
-- update students set birth_date = '1998/02/11' where firs_name = 'Marc';
-- update students set birth_date = '2010/12/03' where firs_name = 'Yoan';
-- update students set birth_date = '1987/07/27' where firs_name = 'Lea';
-- update students set birth_date = '1996/04/07' where firs_name = 'Amelie';
-- update students set birth_date = '2033/06/14' where firs_name = 'David';
-- update students set birth_date = '1980/10/03' where firs_name = 'Omer';

-- select * from students;

-- insert into  students (last_name, firs_name, birth_date) values
-- ('Fellous', 'Michael', '1998/07/15');

-- select * from students;

-- select last_name, firs_name from students;

-- select last_name, firs_name from students where id = 2;

-- select last_name, firs_name from students where last_name = 'Benichou' and firs_name = 'Marc';

-- select last_name, firs_name from students where last_name = 'Benichou' or firs_name = 'Marc';

-- select last_name, firs_name from students where firs_name like '%a%';

-- select last_name, firs_name from students where firs_name like 'A%';

-- select last_name, firs_name from students where firs_name like '%a';

-- select last_name, firs_name from students where substring (firs_name from length(firs_name) - 1 for 1) = 'a';


-- select last_name, firs_name from students where id = 1 or id = 3;
-- i can do like that as well
-- select last_name, firs_name from students where id in (1, 3);


-- select * from students where birth_date >= '2000/01/01';


 -- CREATE TABLE actors(
 -- actor_id SERIAL PRIMARY KEY,
 -- first_name VARCHAR (50) NOT NULL,
 -- last_name VARCHAR (100) NOT NULL,
 -- age DATE NOT NULL,
 -- number_oscars SMALLINT NOT NULL
 -- )


-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);


-- select * from actors;


-- insert into actors (first_name, last_name, age, number_oscars)
-- values ('Julia', 'Roberts', '12/02/2010', '4'),
--        ('Jenifer', 'Aniston', '05/31/1975', '2'),
--        ('Jean', 'Dujardin', '05/05/1975', '2');

-- select * from actors;


-- select * from actors where number_oscars > 2 and last_name = 'Damon';

-- select * from actors where number_oscars >= 3 or last_name = 'Aniston';

-- select * from actors order by actor_id;         /*order by ca sert a que ca s'affiche dans lordre
-- select first_name, last_name from actors where first_name = 'Jean' and last_name = 'Dujardin';



-- SELECT * FROM actors WHERE last_name LIKE '%mon%';        /*ca va chercher qqun qui a 'mon' dans son last_name
-- select * from actors where first_name like '%a%';


-- select * from actors limit 5;        /* ca va afficher que les 5 premieres lignes prcq jai limite a 5

-- select * from actors where age > '1970/05/31' limit 2;

-- select * from actors where age > '1970/05/31' limit 4 offset 2;  /*le offset va enlever les 2 premieres lignes qui coresponde a ce que jai demander. je peux mettre un autre chiffre que 2


-- SELECT * FROM actors WHERE age > '1960-01-01' ORDER BY first_name ASC    /*ca va me trier les noms alphabetiquement
--  SELECT * FROM actors WHERE age > '1960-01-01' ORDER BY first_name DESC      /* ca va faire pareille que ligne 48 mais dans lordre alphabetique inverse




--  exercice
-- Use the table actors to retrieve :

-- The first 4 actors
-- The first 4 actors ordered in descending order of the last_name (ie. sorted DESCENDING by the "last_name" column))
-- The actors that have the letter 'e' in their first_name
-- The actors that got at least 5 oscars



-- select * from actors limit 4;         /*ca va afficher les 4 premiers      

-- select * from actors order by last_name desc limit 4;     /*ca va afficher les 4 dans lordre invers des noms de famille   

-- select * from actors where first_name like '%e%';    /* ca va afficher tous les prenoms avec e

-- select * from actors where number_oscars >= 5;        /* ca va afficher les acteurs avec au moins 5 oscars


-- update actors
-- set age = '1971/02/02'
-- where teoudatzeout = 1
-- returning
-- teoudatzeout,
-- first_name,
-- last_name,
-- age;


-- -- je vais effacer lacteur qui a id 6
-- DELETE FROM actors WHERE teoudatzeout=6
-- RETURNING teoudatzeout, first_name, last_name, number_oscars;


-- ALTER TABLE actors RENAME COLUMN teoudatzeout TO actor_id;


-- select * from actors;





-- daily challenge

-- select count(*) from actors;

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES (NULL, NULL, NULL, NULL);

-- ERROR:  null value in column "first_name" of relation "actors" violates not-null constraint



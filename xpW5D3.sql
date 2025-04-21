-- select * from customer;

-- select concat(first_name,' ', last_name) as full_name from customer;

-- select distinct create_date from customer;

-- select * from customer order by first_name asc;

-- select film_id, title, description, release_year, rental_rate from film order by rental_rate asc;

-- select address, phone from address where district = 'Texas';

-- select * from film where film_id in (15, 150);


-- select film_id, title, description, length, rental_rate from film where title = 'African Egg';

-- select film_id, title, description, length, rental_rate from film where title like 'Af%';

-- select * from film order by replacement_cost asc limit 10;

-- select * from (
-- select *, row_number() over (order by replacement_cost asc) as rang
-- from film
-- ) as film_order
-- where rang between 11 and 21;

-- select first_name, last_name, amount, payment_date 
-- from customer 
-- join payment 
-- on customer.customer_id = payment.customer_id 
-- order by customer.customer_id asc;

-- select * 
-- from film 
-- left join inventory on film.film_id = inventory.film_id
-- where inventory.film_id is null;

-- select country,city 
-- from country
-- join city
-- on country.country_id = city.country_id;

-- select customer.customer_id, customer.last_name, customer.first_name, payment.amount, payment.payment_date
-- from customer, payment
-- join staff
-- on payment.staff_id = staff.staff_id
-- order by staff.staff_id;





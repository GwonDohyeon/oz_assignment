use sakila;
# 특정 배우가 출연한 영화 목록 조회
select f.title from film f join film_actor fa on f.film_id=fa.film_id join actor a on fa.actor_id=a.actor_id 
where a.first_name='PENELOPE' and a.last_name='GUINESS';
# 각 카테고리별로 몇 개의 영화가 있는지 조회
select c.name,count(fc.film_id) from category c join film_category fc on c.category_id = fc.category_id group by c.name;
# 특정 고객의 대여 기록 조회
select r.rental_date,f.title from rental r join inventory i on r.inventory_id=i.inventory_id join film f on i.film_id=f.film_id 
where r.customer_id=5;
# 가장 최근에 추가된 10개의 영화 조회
select title from film order by release_year desc, title limit 10;

# 특정 영화에 출연한 모든 배우 조회
select a.first_name, a.last_name from actor a join film_actor fa on a.actor_id=fa.actor_id join film f on fa.film_id=f.film_id
where f.title='ACADEMY DINOSAUR';
# 특정 영화를 대여한 고객 목록 조회
select distinct c.first_name, c.last_name from customer c join rental r on c.customer_id=r.customer_id 
join inventory i on i.inventory_id=r.inventory_id
join film f on f.film_id=i.film_id where f.title='ACADEMY DINOSAUR';
# 모든 고객들의 가장 최근에 대여한 영화 조회
SELECT c.customer_id, c.first_name, c.last_name, MAX(r.rental_date) as last_rental_date, f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY c.customer_id, c.first_name, c.last_name, f.title;
# 각 영화별 평균 대여 기간
SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) as avg_rental_period
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title order by avg_rental_period desc;

# 가장 많이 대여된 영화 조회
SELECT f.title, COUNT(r.rental_id) as rental_count
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY rental_count DESC
LIMIT 1;
# 각 카테고리별 평균 대여 요금 조회
SELECT c.name, AVG(f.rental_rate) as average_rental_rate
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name;
# 월별 총 매출액
SELECT YEAR(p.payment_date) as year, MONTH(p.payment_date) as month, SUM(p.amount) as total_sales
FROM payment p
GROUP BY YEAR(p.payment_date), MONTH(p.payment_date);
# 배우별 출연한 영화 수
SELECT a.first_name, a.last_name, COUNT(fa.film_id) as number_of_films
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.first_name, a.last_name;

# 가장 많은 수익을 낸 영화 조회
SELECT f.title, SUM(p.amount) AS total_revenue
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY f.title
ORDER BY total_revenue DESC
LIMIT 1;
# 평균 요금보다 높은 요금의 영화 조회
SELECT f.title, f.rental_rate
FROM film f
WHERE f.rental_rate > (SELECT AVG(rental_rate) FROM film);
# 가장 많은 영화를 대여한 고객의 이름과 대여 횟수
SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS rental_count
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY rental_count DESC
LIMIT 1;
# 특정 배우가 출연한 영화 중 가장 많이 대여된 영화 제목과 대여 횟수
SELECT f.title, COUNT(r.rental_id) AS rental_count
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
GROUP BY f.title
ORDER BY rental_count DESC
LIMIT 1;

# film 테이블에 'New Adventure Movie'라는 새로운 영화를 추가
INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
VALUES ('New Adventure Movie', 'A thrilling adventure of the unknown', 2023, 1, 3, 4.99, 120, 19.99, 'PG', 'Trailers,Commentaries');
# 대여 ID가 200인 대여 기록의 상태를 'returned'로 변경
UPDATE rental
SET return_date = NOW()
WHERE rental_id = 200;
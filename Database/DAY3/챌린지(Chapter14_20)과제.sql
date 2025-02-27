create database employment_db;
use employment_db;
-- 1
create table employees(
	employee_id int auto_increment,
	employee_name varchar(100),
    position varchar(100),
    salary decimal(10,2),
    primary key(employee_id)
);
-- 2
insert into employees(employee_name,position,salary)
values ('혜린','PM',90000),
('은우','Frontend',80000),
('가을','Backend',92000),
('지수','Frontend',78000),
('민혁','Frontend',96000),
('하온','Backend',130000);
-- 3
select employee_name, salary from employees;
-- 4
select employee_name, salary from employees where position = 'Frontend';
-- 5
update employees set salary = salary * 1.1 where position = 'PM';
select * from employees;
-- 6
update employees set salary = salary * 1.05 where position = 'Backend';
-- 7
delete from employees where employee_name = '민혁';
-- 8
select avg(salary) as '평균 연봉' from employees group by position;
-- 9
drop table employees;
create database fishbread_db;
use fishbread_db;
create table users(
	user_id int auto_increment,
    name varchar(255) not null,
    age int not null,
    email varchar(100) unique,
    is_business bool,
    primary key(user_id)
);
create table orders(
	order_id int auto_increment,
    user_id int, 
    order_date date,
    amount decimal(10,2),
    primary key(order_id),
    foreign key(user_id) references users(user_id)
);
create table inventory(
	item_id int auto_increment,
    item_name varchar(255) not null,
    quantitiy int not null,
    primary key(item_id)
);
create table sales(
	sale_id int auto_increment,
    order_id int,
    item_id int,
    quantity_sold int not null,
    primary key(sale_id),
    foreign key(order_id) references orders(order_id),
    foreign key(item_id) references inventory(item_id)
);
create table daily_sales(
	date date,
    total_sales decimal(10,2) not null,
    primary key(date)
);














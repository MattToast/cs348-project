-- This is just a jot down of how I set up my tables
-- It should not be used to actually create the tables
-- THESE TABLES ARE NOT FINAL, JUST USED FOR SETTING UP DEV ENV

create table employees(employee_id int, position varchar(50), salary int, location_id int);
create table inventory(product_id int, name varchar(50), location_id int, price int, stock int);
create table locations(location_id int, owner_id int, loc_name varchar(50), total_cash int);
create table customers(customer_id int, cutomer_name varchar(50), customer_address varchar(100), phone_number varchar(20), offer_promotions tinyint(1));
create table sales(sale_id int, product_id int, customer_id int, amount int, location_id int);

insert into employees values (1, 'cashier', 24000, 1), (2, 'manager', 80000, 1), (3, 'manager', 95000, 2);
insert into inventory values (1, 'bits', 1, 24, 50), (1, 'bits', 2, 15, 20), (2, 'bobs', 1, 36, 19), (2, 'bobs', 2, 41, 41);
insert into locations values (1, 2, "Chicago Store", 5000), (2, 3, "New York Store", 10000);
insert into customers values (1, "Mark", "1234 Northway Street", "815-522-9874", 1), (2, "Matt", "4321 Southland Road", "815-159-3256", 0);
insert into sales values (1, 1, 1, 20, 1), (2, 1, 2, 18, 2);
-- This is just a jot down of how I set up my tables
-- It should not be used to actually create the tables
-- THESE TABLES ARE NOT FINAL, JUST USED FOR SETTING UP DEV ENV, NO KEYS ARE DEFINED

create table Locations(LocationID INT, `Money` INT, OwnerID INT);
insert into Locations values (1, 5000, 1), (2, 10000, 2);

create table Employee(EmployeeID INT, position VARCHAR(50), Salary INT, LocationID INT);
insert into Employee values (1, 'cashier', 24000, 1), (2, 'manager', 80000, 1), (3, 'manager', 95000, 2);

create table Inventory(ProductID INT, `Name` VARCHAR(50));
insert into Inventory values (1, 'bits'), (2, 'bobs');

create table Sales(SalesID INT, ProductID INT, CustomerID INT, Amount INT, LocationID INT, `Date` VARCHAR(50));
insert into Sales values (1, 1, 1, 20, 1, '2021-03-15'), (2, 1, 2, 18, 2, '2021-03-20');

create table Customers(CustomerID INT, `Name` VARCHAR(50), Address VARCHAR(50), Phone VARCHAR(50), OfferPromotions TINYINT(1));
insert into Customers values (1, "Mark", "1234 Northway Street", "815-522-9874", 1), (2, "Matt", "4321 Southland Road", "815-159-3256", 0);

create table Transfers(TransferID INT, FromLoc INT, ToLoc INT, Amount INT);
insert into Transfers values (1, 1, 2, 5000), (2, 2, 1, 3000);

create table Includes(ProductID INT, LocationID INT, SalesID INT, NumBought INT);
insert into Includes values (1, 1, 1, 4), (1, 2, 2, 3);

create table Has(LocationID INT, ProductID INT, Price INT, Stock INT);
insert into Has values (1, 1, 5, 75), (2, 1, 6, 50), (1, 2, 10, 25);

create table Buys(CustomerID INT, EmployeeID INT, SalesID INT);
insert into Buys values (1, 1, 1), (2, 3, 2);

create table Owns(LocationID INT, EmployeeID INT);
insert into Owns values (1, 2), (2, 3);

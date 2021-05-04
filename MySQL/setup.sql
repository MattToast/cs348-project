-- Sets up the tables in expected manner
-- Do the deletes by hand, but every thing after that can be `ctrl+a, ctrl+c, ctrl+v`ed

DROP TABLE IF EXISTS Buys;
DROP TABLE IF EXISTS Has;
DROP TABLE IF EXISTS Includes;
DROP TABLE IF EXISTS Transfers;
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Inventory;

-- NOTE!! These next few stmts may fail if the tables have already been made
-- That is because all of the remaingin foreign keys refference these tables
-- Proceed from here with cuation
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Locations;
DROP TABLE IF EXISTS Customers;

create table Customers(
  CustomerID INT NOT NULL, 
  `Name` VARCHAR(50) NOT NULL,
  `Address` VARCHAR(50) NOT NULL,
  Phone VARCHAR(50) NOT NULL,
  OfferPromotions TINYINT(1) NOT NULL,
  PRIMARY KEY (CustomerID)
);
insert into Customers values 
  (1, "Mark", "1234 Northway Street", "815-522-9874", 1),
  (2, "Matt", "4321 Southland Road", "815-159-3256", 0);

-------------------------------------------------------------------------------------

create table Locations(
  LocationID INT NOT NULL, 
  `Money` INT NOT NULL, 
  OwnerID INT NOT NULL,
  PRIMARY KEY (LocationID)
);
insert into Locations values 
  (1, 5000, 1), 
  (2, 10000, 2);

create table Employee(
  EmployeeID INT NOT NULL, 
  position VARCHAR(50) NOT NULL, 
  Salary INT NOT NULL, 
  LocationID INT NOT NULL,
  PRIMARY KEY (EmployeeID),
  FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);
insert into Employee values 
  (1, 'cashier', 24000, 1), 
  (2, 'manager', 80000, 1), 
  (3, 'manager', 95000, 2);

-- Set foreign key on locations
ALTER TABLE Locations ADD FOREIGN KEY (OwnerID) REFERENCES Employee(EmployeeID);

-------------------------------------------------------------------------------------

create table Inventory(
  ProductID INT NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (ProductID)
);
insert into Inventory values 
  (1, 'bits'),
  (2, 'bobs');

-------------------------------------------------------------------------------------

create table Sales(
  SalesID BIGINT(8) UNSIGNED NOT NULL, 
  ProductID INT NOT NULL, 
  CustomerID INT NOT NULL, 
  Amount INT NOT NULL, 
  LocationID INT NOT NULL, 
  `Date` VARCHAR(100) NOT NULL,
  PRIMARY KEY (SalesID),
  FOREIGN KEY (ProductID) REFERENCES Inventory(ProductID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);
insert into Sales values 
  (1620008010877, 1, 1, 20, 1, '2021-5-2'),
  (1620008023049, 1, 2, 18, 2, '2021-5-2');

-------------------------------------------------------------------------------------

create table Transfers(
  TransferID INT NOT NULL,
  FromLoc INT NOT NULL,
  ToLoc INT NOT NULL,
  Amount INT NOT NULL,
  PRIMARY KEY (TransferID),
  FOREIGN KEY (FromLoc) REFERENCES Locations(LocationID),
  FOREIGN KEY (ToLoc) REFERENCES Locations(LocationID)
);
insert into Transfers values
  (1, 1, 2, 5000),
  (2, 2, 1, 3000);

-------------------------------------------------------------------------------------

create table Includes(
  ProductID INT NOT NULL, 
  LocationID INT NOT NULL,
  SalesID BIGINT(8) UNSIGNED NOT NULL,
  NumBought INT NOT NULL,
  PRIMARY KEY (ProductID, LocationID, SalesID),
  FOREIGN KEY (ProductID) REFERENCES Inventory(ProductID),
  FOREIGN KEY (LocationID) REFERENCES Locations(LocationID),
  FOREIGN KEY (SalesID) REFERENCES Sales(SalesID)
);
insert into Includes values
  (1, 1, 1620008010877, 4),
  (1, 2, 1620008023049, 3);

-------------------------------------------------------------------------------------

create table Has(
  LocationID INT NOT NULL,
  ProductID INT NOT NULL,
  Price INT NOT NULL,
  Stock INT NOT NULL,
  PRIMARY KEY (LocationID, ProductID),
  FOREIGN KEY (LocationID) REFERENCES Locations(LocationID),
  FOREIGN KEY (ProductID) REFERENCES Inventory(ProductID)
);
insert into Has values
  (1, 1, 5, 75),
  (2, 1, 6, 50),
  (1, 2, 10, 25);

-------------------------------------------------------------------------------------

create table Buys(
  CustomerID INT NOT NULL,
  EmployeeID INT NOT NULL,
  SalesID BIGINT(8) UNSIGNED NOT NULL,
  PRIMARY KEY (CustomerID, EmployeeID, SalesID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
  FOREIGN KEY (SalesID) REFERENCES Sales(SalesID)
);
insert into Buys values
  (1, 1, 1620008010877),
  (2, 3, 1620008023049);

-------------------------------------------------------------------------------------

CREATE INDEX salesSalesIDIndex ON Sales(SalesID) USING BTREE;
CREATE INDEX buysEmployeeIDIndex ON Buys(EmployeeID) USING BTREE;

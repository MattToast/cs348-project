-- Stored procedure skeleton. Write your code here and then submit to Brightspace.

DROP PROCEDURE IF EXISTS NewSaleCreation;

DELIMITER //

CREATE PROCEDURE NewSaleCreation ( 
  IN saleID INT, 
  IN custID INT, 
  IN emplID INT, 
  IN prodID INT, 
  IN quantity INT,
  IN dateStr VARCHAR(100) 
  OUT success TINYINT)

BEGIN
  -- Init some stuff
  SET success = 1;
  DECLARE numInventory INT DEFAULT 0;
  DECLARE locID INT DEFAULT 0;
  DECLARE price INT DEFAULT 0;
  DECLARE totalAmt INT DEFAULT 0;

  -- Get the current location
  SELECT LocationID INTO locID FROM Employee
  WHERE EmployeeID = emplID;

  -- Check to make sure that the store has the inventory to complete the sale
  SELECT Stock INTO numInventory FROM Has
  WHERE ProductID = prodID AND LocationID = locID;

  -- If there is not enough fail, else continue
  IF numInventory < quantity THEN
    SET success = 0;
  ELSE
    -- Get the price of the product and multiply by quantity to get the total amount of sale
    SELECT Price INTO price FROM HAS
    WHERE ProductID = prodID AND LocationID = locID;

    SET totalAmt = price * quantity;

    -- Make an insert into the the sales table, trigger will deal with reulting changes to other tables
    INSERT INTO Sales VALUES (saleID, prodID, custID, totalAmt, locID, dateStr);
  END IF;
END //
DELIMITER ;
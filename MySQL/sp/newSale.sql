DROP PROCEDURE IF EXISTS NewSaleCreation;

DELIMITER //

CREATE PROCEDURE NewSaleCreation ( 
  IN saleID BIGINT(8) UNSIGNED, 
  IN custID INT, 
  IN emplID INT, 
  IN prodID INT, 
  IN quantity INT,
  IN dateStr VARCHAR(100),
  OUT success INT)

BEGIN
  -- Init some stuff
  DECLARE numInventory INT DEFAULT 0;
  DECLARE locID INT DEFAULT 0;
  DECLARE p INT DEFAULT 0;
  DECLARE totalAmt INT DEFAULT 0;
  SET success = 1;

  -- Make sure we are getting committed data and no other actions modifing it
  SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
  START TRANSACTION;
    -- Get the current location
    SELECT LocationID INTO locID FROM Employee
    WHERE EmployeeID = emplID;

    -- Check to make sure that the store has the inventory to complete the sale
    SELECT Stock INTO numInventory FROM Has
    WHERE ProductID = prodID AND LocationID = locID;
  COMMIT;

  -- If there is not enough fail, else continue
  IF numInventory < quantity THEN
    SET success = 0;
  ELSE
    -- Get the price of the product and multiply by quantity to get the total amount of sale
    SELECT Price INTO p FROM Has
    WHERE ProductID = prodID AND LocationID = locID;

    SET totalAmt = p * quantity;

    -- Make an insert into the the sales table, triggers will deal with reulting changes to other tables
    INSERT INTO Sales VALUES (saleID, prodID, custID, totalAmt, locID, dateStr);
    INSERT INTO Includes VALUES (prodID, locID, saleID, quantity);
    INSERT INTO Buys VALUES (custID, emplID, saleID);
  END IF;
END //
DELIMITER ;
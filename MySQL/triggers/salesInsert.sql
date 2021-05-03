DROP TRIGGER IF EXISTS SalesInsert;

DELIMITER //

CREATE TRIGGER SalesInsert

AFTER INSERT ON Sales
FOR EACH ROW

BEGIN
  -- Add the amount of money made on the sale to the appropriate location
  UPDATE Locations
  SET `Money` = `Money` + new.Amount
  WHERE LocationID = new.LocationID;
END //
DELIMITER ;
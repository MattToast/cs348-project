DROP TRIGGER IF EXISTS IncludesInsert;

DELIMITER //

CREATE TRIGGER IncludesInsert

AFTER INSERT ON Includes
FOR EACH ROW

BEGIN
  -- Reduce the stock of the item bought at the appropriate store
  UPDATE Has
  SET Stock = Stock - new.NumBought
  WHERE LocationID = new.LocationID AND ProductID = new.ProductID;
END //
DELIMITER ;
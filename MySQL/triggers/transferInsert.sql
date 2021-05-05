DROP TRIGGER IF EXISTS TransferInsert;

DELIMITER //

CREATE TRIGGER TransferInsert

AFTER INSERT ON Transfers
FOR EACH ROW

BEGIN
  UPDATE Locations SET `Money` = `Money` -  new.Amount WHERE LocationID = new.FromLoc;
  UPDATE Locations SET `Money` = `Money` +  new.Amount WHERE LocationID = new.ToLoc;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS MoneyFlowReport;

DELIMITER //

CREATE PROCEDURE MoneyFlowReport (IN no_use INT, OUT report LONGTEXT)

BEGIN
  DECLARE done int DEFAULT 0;
  DECLARE locID int DEFAULT 0;
  DECLARE totOut int DEFAULT 0;
  DECLARE totIn int DEFAULT 0;
  DECLARE trasfersCursor CURSOR FOR
                             SELECT t1.FromLoc, SUM(t1.Amount), SUM(t2.Amount)
                             FROM Transfers t1
                             JOIN Transfers t2 ON t1.FromLoc = t2.ToLoc
                             GROUP BY t1.FromLoc;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  SET report = "<table border = '1'><tr><th colspan=3>Money Flow By Transfer</th></tr><tr><td>Location ID</td><td>Total Money Out</td><td>Total Money In</td></tr>";

  OPEN trasfersCursor;
  getTransfers: LOOP
    FETCH trasfersCursor INTO locID, totOut, totIn;
    IF done = 1 THEN
      LEAVE getTransfers;
    END IF;

    SET report = CONCAT(report, "<tr><td>", locID, "</td><td>", totOut, "</td><td>", totIn, "</td></tr>");
  END LOOP getTransfers;
  SET report = CONCAT(report, "</table>");
END //
DELIMITER ;

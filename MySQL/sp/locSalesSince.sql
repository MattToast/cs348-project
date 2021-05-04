DROP PROCEDURE IF EXISTS GetLocSalesSince;

DELIMITER //

CREATE PROCEDURE GetLocSalesSince ( IN since_time BIGINT(8) UNSIGNED, OUT report LONGTEXT)

BEGIN
  DECLARE done int DEFAULT 0;
  DECLARE locID INT DEFAULT 0;
  DECLARE totalSales INT DEFAULT 0; 
  DECLARE maxSale INT DEFAULT 0; 
  DECLARE salesCursor CURSOR FOR
                              SELECT l.LocationID, SUM(s.Amount), MAX(s.Amount)
                              FROM Sales s
                              JOIN Buys b ON b.SalesID = s.SalesID
                              JOIN Employee e ON b.EmployeeID = e.EmployeeID
                              JOIN Locations l ON l.LocationID = e.LocationID
                              WHERE b.SalesID > since_time
                              GROUP BY l.LocationID;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;                    

  SET report = "<table border = '1'><tr><th colspan=3>Location Sales History</th></tr><tr><td>Location ID</td><td>All</td><td>Max</td></tr>";
  
  -- Set the transaction level to read commited for more parrallel data
  SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
  START TRANSACTION;
    OPEN salesCursor;
    getSales: LOOP
      FETCH salesCursor INTO locID, totalSales, maxSale;

      IF done = 1 THEN
        LEAVE getSales;
      END IF;

      SET report = CONCAT(report, "<tr><td>", locID, "</td><td>", totalSales, "</td><td>", maxSale, "</td></tr>");
    END LOOP getSales;
    CLOSE salesCursor;
    SET report = CONCAT(report, "</table>");
  COMMIT;
END //
DELIMITER ;
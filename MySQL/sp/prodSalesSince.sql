DROP PROCEDURE IF EXISTS GetProdSalesSince;

DELIMITER //

CREATE PROCEDURE GetProdSalesSince ( IN since_time BIGINT(8) UNSIGNED, OUT report LONGTEXT)

BEGIN
  DECLARE done int DEFAULT 0;
  DECLARE prodID INT DEFAULT 0;
  DECLARE totalSales INT DEFAULT 0; 
  DECLARE maxSale INT DEFAULT 0; 
  DECLARE salesCursor CURSOR FOR
                            SELECT i.ProductID, SUM(s.Amount), MAX(s.Amount)
                            FROM Sales s
                            JOIN Includes i ON i.SalesID = s.SalesID
                            WHERE i.SalesID > since_time
                            GROUP BY i.ProductID;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;                    

  SET report = "<table border = '1'><tr><th colspan=3>Product Sales History</th></tr><tr><td>Product ID</td><td>All</td><td>Max</td></tr>";
  
  -- Set the transaction level to read commited for more parrallel data
  SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
  START TRANSACTION;
    OPEN salesCursor;
    getSales: LOOP
      FETCH salesCursor INTO prodID, totalSales, maxSale;

      IF done = 1 THEN
        LEAVE getSales;
      END IF;

      SET report = CONCAT(report, "<tr><td>", prodID, "</td><td>", totalSales, "</td><td>", maxSale, "</td></tr>");
    END LOOP getSales;
    CLOSE salesCursor;
    SET report = CONCAT(report, "</table>");
  COMMIT;
END //
DELIMITER ;
DROP PROCEDURE IF EXISTS GetComplexReport;

DELIMITER //

CREATE PROCEDURE GetComplexReport (IN no_use INT, OUT report LONGTEXT)

BEGIN
  DECLARE r LONGTEXT DEFAULT "";
  DECLARE topGrossingEmp INT DEFAULT 0;
  DECLARE topGrossingProd INT DEFAULT 0;
  DECLARE topGrossingLoc INT DEFAULT 0;
  SET report = "";

  -- Sales by Location
  CALL GetLocSalesSince(0, r);
  SET report = CONCAT(report, "<h2>Sales By Location</h2>", r);

  -- Sales by Employees
  CALL GetEmplSalesSince(0, r);
  SET report = CONCAT(report, "<h2>Sales By Employee</h2>", r);

  -- Sales by Product
  CALL GetProdSalesSince(0, r);
  SET report = CONCAT(report, "<h2>Sales By Product</h2>", r);

  -- Sales by Customer
  CALL GetCustSalesSince(0, r);
  SET report = CONCAT(report, "<h2>Sales By Customer</h2>", r);

  -- Top Revenue Generated from Employee
  -- NOTE: This assumes two employees will not genreate the same top revenue
  SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
  START TRANSACTION;
      SELECT b1.EmployeeID INTO topGrossingEmp
      FROM Sales s1
      JOIN Buys b1 ON b1.SalesID = s1.SalesID
      GROUP BY b1.EmployeeID
      HAVING b1.EmployeeID = (
        SELECT empID
        FROM (
          SELECT b2.EmployeeID AS empID, SUM(s2.Amount) AS empTotalSales
          FROM Sales s2
          JOIN Buys b2 ON b2.SalesID = s2.SalesID
          GROUP BY b2.EmployeeID
        ) AS temp1
        WHERE temp1.empTotalSales = (
          SELECT MAX(temp2.totalSales)
          FROM (
            SELECT b3.EmployeeID AS empID, SUM(s3.Amount) AS totalSales
            FROM Sales s3
            JOIN Buys b3 ON b3.SalesID = s3.SalesID
            GROUP BY b3.EmployeeID
          ) AS temp2
        )
      );
  COMMIT;

  -- Top Revenue Generated from Location
  -- NOTE: This assumes two Locations will not genreate the same top revenue
  SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
  START TRANSACTION;
      SELECT e1.LocationID INTO topGrossingLoc
      FROM Sales s1
      JOIN Buys b1 ON b1.SalesID = s1.SalesID
      JOIN Employee e1 ON e1.EmployeeID = b1.EmployeeID
      GROUP BY e1.LocationID
      HAVING e1.LocationID = (
        SELECT locID
        FROM (
          SELECT e2.LocationID AS locID, SUM(s2.Amount) AS locTotalSales
          FROM Sales s2
          JOIN Buys b2 ON b2.SalesID = s2.SalesID
          JOIN Employee e2 ON e2.EmployeeID = b2.EmployeeID
          GROUP BY e2.LocationID
        ) AS temp1
        WHERE temp1.locTotalSales = (
          SELECT MAX(temp2.totalSales)
          FROM (
            SELECT e3.LocationID AS locID, SUM(s3.Amount) AS totalSales
            FROM Sales s3
            JOIN Buys b3 ON b3.SalesID = s3.SalesID
            JOIN Employee e3 ON b3.EmployeeID = e3.EmployeeID
            GROUP BY e3.LocationID
          ) AS temp2
        )
      );
  COMMIT;

  -- Top Revenue Generated from Product
  -- NOTE: This assumes two Products will not genreate the same top revenue
  SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
  START TRANSACTION;
    SELECT s1.ProductID INTO topGrossingProd
    FROM Sales s1
    GROUP BY s1.ProductID
    HAVING s1.ProductID = (
      SELECT prodID
      FROM (
        SELECT s2.ProductID AS prodID, SUM(s2.Amount) AS prodTotalSales
        FROM Sales s2
        GROUP BY s2.ProductID
      ) AS temp1
      WHERE temp1.prodTotalSales = (
        SELECT MAX(temp2.totalSales)
        FROM (
          SELECT s3.ProductID AS prodID, SUM(s3.Amount) AS totalSales
          FROM Sales s3
          GROUP BY s3.ProductID
        ) AS temp2
      )
    );
  COMMIT;

  SET report = CONCAT("<h2>Highest Grossing Info</h2>",
                      "<div>The Highest Grossing Employee ID: ", topGrossingEmp, "</div>",
                      "<div>The Highest Grossing Location ID: ", topGrossingLoc, "</div>",
                      "<div>The Highest Grossing Product ID: ", topGrossingProd, "</div>",
                      report);


END //
DELIMITER ;
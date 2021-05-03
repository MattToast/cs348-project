DROP PROCEDURE IF EXISTS GetComplexReport;

DELIMITER //

CREATE PROCEDURE GetComplexReport (IN no_use INT, OUT report LONGTEXT)

BEGIN
  DECLARE r LONGTEXT DEFAULT "";
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

  -- Top Revenue Generated from Location, Employee, Product, and Customer
  -- SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
  -- START TRANSACTION;
  -- COMMIT;
END //
DELIMITER ;
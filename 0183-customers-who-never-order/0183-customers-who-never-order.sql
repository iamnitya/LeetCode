SELECT name AS "Customers"
FROM Customers WHERE Customers.id not in (
    SELECT customerId FROM Orders
);
SELECT
    c.first_name,
    c.last_name,
    o.item,
    o.amount
FROM
    Customers c INNER JOIN Orders o ON c.customer_id = o.customer_id;

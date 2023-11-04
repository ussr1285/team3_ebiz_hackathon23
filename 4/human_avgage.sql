SELECT
    c.country AS 나라,
    COUNT(DISTINCT c.customer_id) AS 고객수,
    AVG(c.age) AS 평균나이
FROM
    Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY
    c.country
ORDER BY
	고객수 DESC;

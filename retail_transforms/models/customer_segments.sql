SELECT
CustomerKey,
Country,
SUM(Revenue) AS total_revenue,
COUNT(DISTINCT InvoiceID) AS order_count,
CASE
WHEN SUM(Revenue) > 5000 THEN 'High Value'
WHEN SUM(Revenue) > 1000 THEN 'Mid Value'
ELSE 'Standard'
END AS customer_segment
FROM Sales.fact_sales
GROUP BY CustomerKey, Country
SELECT
    Product_Name,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY Product_Name
ORDER BY total_profit DESC
LIMIT 10;
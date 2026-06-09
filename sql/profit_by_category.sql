SELECT
    Category,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY Category
ORDER BY total_profit DESC;
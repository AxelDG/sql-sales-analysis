import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

query = """
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;
"""

resultado = pd.read_sql_query(query, conn)

print(resultado)

conn.close()
import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

query = """
SELECT *
FROM sales
LIMIT 5;
"""

resultado = pd.read_sql_query(query, conn)

print(resultado)

conn.close()
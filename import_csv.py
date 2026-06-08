import pandas as pd
import sqlite3

df = pd.read_csv("data/Superstore.csv", encoding="latin1")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Importación completada")
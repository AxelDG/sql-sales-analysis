import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

# =========================
# CONFIG
# =========================
DATA_PATH = "data/Superstore.csv"
DB_PATH = "sales.db"
IMAGES_DIR = "images"

os.makedirs(IMAGES_DIR, exist_ok=True)

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv(DATA_PATH, encoding="latin1")

# =========================
# 2. LOAD TO SQLITE
# =========================
conn = sqlite3.connect(DB_PATH)
df.to_sql("sales", conn, if_exists="replace", index=False)

# =========================
# 3. QUERIES
# =========================
query_category = """
SELECT Category, SUM(Profit) as total_profit
FROM sales
GROUP BY Category
ORDER BY total_profit DESC;
"""

query_region = """
SELECT Region, SUM(Profit) as total_profit
FROM sales
GROUP BY Region
ORDER BY total_profit DESC;
"""

query_products = """
SELECT [Product Name] as Product, SUM(Profit) as total_profit
FROM sales
GROUP BY [Product Name]
ORDER BY total_profit DESC
LIMIT 10;
"""

category = pd.read_sql_query(query_category, conn)
region = pd.read_sql_query(query_region, conn)
products = pd.read_sql_query(query_products, conn)

# =========================
# 4. VISUALIZATIONS
# =========================

# Profit by Category
plt.figure()
category.set_index("Category")["total_profit"].plot(kind="bar")
plt.title("Profit by Category")
plt.tight_layout()
plt.savefig(f"{IMAGES_DIR}/profit_by_category.png")
plt.show()

# Profit by Region
plt.figure()
region.set_index("Region")["total_profit"].plot(kind="bar")
plt.title("Profit by Region")
plt.tight_layout()
plt.savefig(f"{IMAGES_DIR}/profit_by_region.png")
plt.show()

# Top Products
plt.figure()
products.set_index("Product")["total_profit"].plot(kind="bar")
plt.title("Top 10 Products by Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{IMAGES_DIR}/top_products.png")
plt.show()

conn.close()

print("✅ Analysis completed successfully")
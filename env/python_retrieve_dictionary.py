import psycopg2
import psycopg2.extras
import matplotlib as plt
import numpy as np

hostname = "localhost"
database = "postgres"
username = "postgres"
pwd = "Cowsrule1!"
port_id = 5432

conn = None
curr = None

try:
    conn = psycopg2.connect(
        host = hostname, 
        dbname = database, 
        user = username, 
        password = pwd,
        port = port_id,
    )

    curr = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    curr.execute(
        "Select COUNT(price) AS total_homes_sold, date_trunc('month', datesold) as sales_per_month, SUM(price) AS total_sales_monthly FROM \"House_Sales\" GROUP BY Date_trunc('month', datesold) Order By Date_trunc('month', datesold)")

    for month in curr.fetchall():
        x = np.linspace(month.total_homes_sold)
        plt.plot(x, month.sales_per_month)
        plt.show
 
    conn.commit()

except Exception as error:
    print(error)

finally:
    if curr is not None:
        curr.close()
    if conn is not None:
        conn.close()

import psycopg2
import matplotlib.pyplot as plt
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

    curr = conn.cursor()

    curr.execute(
        "Select COUNT(price) AS total_homes_sold, date_trunc('month', datesold) as sales_per_month, SUM(price) AS total_sales_monthly FROM \"House_Sales\" GROUP BY Date_trunc('month', datesold) Order By Date_trunc('month', datesold)")
    
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.plot(
        [month[0] for month in curr.fetchall()], 
        #[month[1] for month in curr.fetchall()], 
    )
#plt.figure(figsize=(9, 3))
#plt.subplot(131)
#plt.bar(names, values)
#plt.subplot(132)
#plt.scatter(names, values)
#plt.subplot(133)
#plt.plot(names, values)
#plt.suptitle('Categorical Plotting')
#plt.show()
    plt.show()
 
    conn.commit()

except Exception as error:
    print(error)

finally:
    if curr is not None:
        curr.close()
    if conn is not None:
        conn.close()

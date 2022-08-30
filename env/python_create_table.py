import psycopg2

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

    curr.execute("DROP TABLE IF EXISTS emplyee")
    create_script = '''CREATE TABLE IF NOT EXISTS employee (
        id  int PRIMARY KEY,
        name varchar(40) NOT NULL,
        salary int,
        dep_id varchar(30)
    )
    '''
    curr.execute(create_script)

    insert_script = 'INSERT INTO employee (id, name, salary, dep_id) VALUES (%s, %s, %s, %s)'
    insert_value = [(1, "James", 12000, "D1"), (2, "Darth", 1200, "D1"), (3, "Vader", 10000, "D1")]

    for record in insert_value:
        curr.execute(insert_script, record)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if curr is not None:
        curr.close()
    if conn is not None:
        conn.close()

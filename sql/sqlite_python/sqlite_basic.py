import sqlite3

conn = sqlite3.connect('vehicles.db')

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

def writeData(data):

    f = open('cars.sql', 'w')

    with f:
        f.write(data)

def readData():

    f = open('cars.sql', 'r')

    with f:

        data = f.read()

        return data

# 1. Create a table 'Cars' with the above records. 
with conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS cars")
    c.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    c.executemany("INSERT INTO cars VALUES(?,?,?)", cars)

# 2. Fetch all the data in tabular form
    c.execute("SELECT * FROM cars")
    items = c.fetchall()
    print('Fetch all the data in tabular form')
    for item in items:
        print(item)

# 3. Update the price of a record to different value
    c.execute("UPDATE cars SET price = ? WHERE id = ?",(62300, 1))
    c.execute("SELECT * FROM cars WHERE id = 1")
    print('\nUpdate the price of Audi car to 62300')
    print(c.fetchone())

# 4. Select a name and a price of a car using named placeholders
    c.execute("SELECT name, price FROM cars WHERE id=:id", {"id": 5})
    print('\nSelect 5th car name and price in the table')
    print(c.fetchone())

# 5. Delete a record or field
    c.execute("DELETE FROM cars WHERE price < 30000")
    c.execute("SELECT * FROM cars")
    print('\nDelete cars whose price < 30k')
    print(c.fetchall())

# 6. Dump data in an SQL format
    data = '\n'.join(conn.iterdump())
    writeData(data)

# 7. Read Data (dumped data) from sql
    #sql = readData()
    #c.executescript(sql)

    #c.execute("SELECT * FROM cars")
    #print(c.fetchall())

conn.close()


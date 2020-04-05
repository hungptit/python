import sqlite3
from os import remove

dbfile = 'example.db'
# remove(dbfile)

conn = sqlite3.connect(dbfile)
c = conn.cursor()

# Create table
try:
    c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
except:
    pass

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO stocks VALUES ('2006-01-06','BUY','RHAT',200,36.14)")

purchases = [
    ('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
    ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
    ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
]

for i in range(10000):
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# Save (commit) the changes
conn.commit()

# Display written data
for row in conn.execute('select * from stocks'):
    print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

import sqlite3

conn = sqlite3.connect('example.db')

# Create table

cur = conn.cursor()

#cur.execute('''CREATE TABLE IPsDefined
               #(IP_Address text, System_Name text,  Date text, Correspondence text)''')
# Insert a row of data

#cur.execute("INSERT INTO IPsDefined VALUES ('10.101.101.10','Computer1','2020-08-21','matching')")
for row in cur.execute("SELECT * FROM IPsDefined"):
    print(row[0])


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
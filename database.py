import psycopg2

# Parse the database URL
DATABASE_URL = "postgresql://myuser:512627@localhost:5432/marketseon"
protocol, rest = DATABASE_URL.split("://")

user, two, three = rest.split(":")

password, host = two.split("@")

port, dbname = three.split("/")


print(protocol, user, password, host, port, dbname)


# Connect to the database
conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    dbname=dbname
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM User")

# Fetch the data from table User
rows = cur.fetchall()
print("rows", rows)

# Fetch the results
results = cur.fetchall()

# Print the results
print("res", results)

# Close the cursor and connection
cur.close()
conn.close()


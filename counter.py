import sqlite3

# Connect to the SQLite database file
connection = sqlite3.connect('realestate_data.db')
cursor = connection.cursor()

# Execute a query to get the row count
cursor.execute('SELECT COUNT(*) FROM realestate')
row_count = cursor.fetchone()[0]

# Print the number of rows
print("Number of rows:", row_count)

# Close the cursor and connection
cursor.close()
connection.close()
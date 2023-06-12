import sqlite3

# Connect to the SQLite database file
connection = sqlite3.connect('by_id_info.db')
cursor = connection.cursor()

# Execute a query to get the row count
cursor.execute('SELECT COUNT(*) FROM highmark_homes')
row_count = cursor.fetchone()[0]

# Print the number of rows
print("Number of rows:", row_count)

# Close the cursor and connection
cursor.close()
connection.close()
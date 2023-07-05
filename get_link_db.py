import sqlite3

def create_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('realestate_data.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS realestate (
            id TEXT,
            address TEXT,
            aerial_photos TEXT,
            transferors TEXT,
            transferee TEXT,
            site TEXT,
            description TEXT,
            consideration TEXT,
            broker_agent TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_data(id,address, aerial_photos, transferors, transferee, site, description, consideration, broker_agent):
    # Connect to the SQLite database
    conn = sqlite3.connect('realestate_data.db')
    cursor = conn.cursor()

    # Insert the data into the table
    data = [(id,address, ", ".join(aerial_photos), ", ".join(transferors[:4]), transferee, ", ".join(site[:4]), description, consideration, broker_agent)]
    cursor.executemany('INSERT INTO realestate VALUES (?,?,?,?,?,?,?,?,?)', data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
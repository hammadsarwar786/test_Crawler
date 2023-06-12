import sqlite3


def create_database():
    # Connect to the SQLite database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('test4.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Define the create table query
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS highmark_homes (
        NAME TEXT,
        ACCOUNTNUMBER TEXT,
        Umbrella TEXT,
        UmbrellaID TEXT,
        VB_NAME TEXT,
        OPERATINGNAME TEXT,
        CITY TEXT,
        HCRA_INITIALLICENSEDATE TEXT,
        LICENCE_STATUS TEXT,
        HCRA_LICENSERENEWEDON TEXT,
        ExpiryDate TEXT,
        RENL_IN_PROCESS_FLAG TEXT,
        MEMBERVBNUM TEXT,
        MEMBERNAME TEXT,
        MEMBEROPERATINGNAME TEXT,
        MEMBERLICENCESTATUS TEXT,
        ADDRESS TEXT,
        TELEPHONE TEXT,
        FAX TEXT,
        WEBSITEURL TEXT,
        EMAIL TEXT,
        TotalOutstandingAmount REAL,
        TAB REAL,
        BREACH TEXT,
        SUMM_FREEHOLD INTEGER,
        SUMM_CONDO INTEGER,
        SUMM_TOTAL INTEGER,
        SUMM_CC INTEGER,
        SUMM_MINOR INTEGER,
        SUMM_MINOR_AMT INTEGER,
        SUMM_MAJOR INTEGER,
        SUMM_MAJOR_AMT INTEGER,
        SUMM_TOTAL_CLAIMS INTEGER
    );
'''
    # Execute the create table query
    cursor.execute(create_table_query)

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()


def insert_data(data):

    conn = sqlite3.connect('test4.db')
    cursor = conn.cursor()
    insert_query = '''
        INSERT INTO highmark_homes (
            NAME,
            ACCOUNTNUMBER,
            Umbrella,
            UmbrellaID,
            VB_NAME,
            OPERATINGNAME,
            CITY,
            HCRA_INITIALLICENSEDATE,
            LICENCE_STATUS,
            HCRA_LICENSERENEWEDON,
            ExpiryDate,
            RENL_IN_PROCESS_FLAG,
            MEMBERVBNUM,
            MEMBERNAME,
            MEMBEROPERATINGNAME,
            MEMBERLICENCESTATUS,
            ADDRESS,
            TELEPHONE,
            FAX,
            WEBSITEURL,
            EMAIL,
            TotalOutstandingAmount,
            TAB,
            BREACH,
            SUMM_FREEHOLD,
            SUMM_CONDO,
            SUMM_TOTAL,
            SUMM_CC,
            SUMM_MINOR,
            SUMM_MINOR_AMT,
            SUMM_MAJOR,
            SUMM_MAJOR_AMT,
            SUMM_TOTAL_CLAIMS
        ) VALUES (?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_query, (
        data["NAME"],
        data["ACCOUNTNUMBER"],
        data["Umbrella"],
        data["Umbrella ID"],
        data["VB_NAME"],
        data["OPERATINGNAME"],
        data["CITY"],
        data["HCRA_INITIALLICENSEDATE"],
        data["LICENCE_STATUS"],
        data["HCRA_LICENSERENEWEDON"],
        data["Expiry Date"],
        data["RENL_IN_PROCESS_FLAG"],
        data["MEMBERVBNUM"],
        data["MEMBERNAME"],
        data["MEMBEROPERATINGNAME"],
        data["MEMBERLICENCESTATUS"],
        data["ADDRESS"],
        data["TELEPHONE"],
        data["FAX"],
        data["WEBSITEURL"],
        data["EMAIL"],
        data["Total Outstanding Amount"],
        data["TAB"],
        data["BREACH"],
        data["SUMM_FREEHOLD"],
        data["SUMM_CONDO"],
        data["SUMM_TOTAL"],
        data["SUMM_CC"],
        data["SUMM_MINOR"],
        data["SUMM_MINOR_AMT"],
        data["SUMM_MAJOR"],
        data["SUMM_MAJOR_AMT"],
        data["SUMM_TOTAL_CLAIMS"]
    ))
    conn.commit()


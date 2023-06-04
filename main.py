import sqlite3

# Function to create the database and table
def create_database():
    conn = sqlite3.connect('cybersecurity.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS security_logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 event TEXT NOT NULL,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(event):
    conn = sqlite3.connect('cybersecurity.db')
    c = conn.cursor()

    c.execute("INSERT INTO security_logs (event) VALUES (?)", (event,))
    conn.commit()

    print("Data inserted successfully!")

    conn.close()

# Function to retrieve data from the table
def retrieve_data():
    conn = sqlite3.connect('cybersecurity.db')
    c = conn.cursor()

    c.execute("SELECT * FROM security_logs")
    rows = c.fetchall()

    for row in rows:
        print("ID:", row[0])
        print("Event:", row[1])
        print("Timestamp:", row[2])
        print("")

    conn.close()

# Function to delete data from the table
def delete_data(event_id):
    conn = sqlite3.connect('cybersecurity.db')
    c = conn.cursor()

    c.execute("DELETE FROM security_logs WHERE id = ?", (event_id,))
    conn.commit()

    print("Data deleted successfully!")

    conn.close()

# Function to filter data within a date or time range
def filter_data(start_date, end_date):
    conn = sqlite3.connect('cybersecurity.db')
    c = conn.cursor()

    c.execute("SELECT * FROM security_logs WHERE timestamp BETWEEN ? AND ?", (start_date, end_date))
    rows = c.fetchall()

    for row in rows:
        print("ID:", row[0])
        print("Event:", row[1])
        print("Timestamp:", row[2])
        print("")

    conn.close()

# Function to count the total number of logs
def count_logs():
    conn = sqlite3.connect('cybersecurity.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM security_logs")
    count = c.fetchone()[0]

    print("Total number of logs:", count)

    conn.close()

# Function to update an existing log
def update_log(event_id, new_event):
    conn = sqlite3.connect('cybersecurity.db')
    c = conn.cursor()

    c.execute("UPDATE security_logs SET event = ? WHERE id = ?", (new_event, event_id))
    conn.commit()

    print("Log updated successfully!")

    conn.close()

# Main program
if __name__ == '__main__':
    create_database()

    insert_data("Login attempt from unauthorized IP")
    insert_data("SQL injection detected")
    insert_data("Firewall breach")

    retrieve_data()

    delete_data(1)

    filter_data('2023-05-01 00:00:00', '2023-05-31 23:59:59')

    count_logs()

    update_log(2, "Potential malware infection detected")

    retrieve_data()

import mysql.connector

DEFAULT_TODOS = ["Buy groceries", "Walk the dog", "Read a book"]

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456aB",
    "database": "todo_assignment",
}

def create_database():
    """
    Method creates the database if it doesn't exist
    """
    config = {k: v for k, v in DB_CONFIG.items() if k != "database"}
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    cursor.close()
    conn.close()

def create_table():
    """
    Creates todos table in the created database
    """
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            body VARCHAR(255) NOT NULL,
            status ENUM('unfinished', 'finished') NOT NULL DEFAULT 'unfinished'
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def seed_todos():
    """
    Seed tables with default todos, but only if the table is currently empty
    """
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM todos")
    count = cursor.fetchone()[0]

    if count == 0:
        for index, todo in enumerate(DEFAULT_TODOS):
            status = "unfinished" if index % 2 == 0 else "finished"
            cursor.execute(
                "INSERT INTO todos (body, status) VALUES (%s, %s)", (todo, status)
            )
        conn.commit()
        print(f"Seeded {len(DEFAULT_TODOS)} default todos.")
    else:
        print("Todos table already has data — skipping seed.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
    create_table()
    seed_todos()

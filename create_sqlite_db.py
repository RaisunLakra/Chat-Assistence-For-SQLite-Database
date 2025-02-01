# Name: Raisun Lakra
# Description: Creating database and tables to store employees and departments data in database.

import sqlite3
import os

def create_database(db_path=os.path.join(os.getcwd(), 'sqlite3.db')):
    """
    Creates a SQLite database at the specified path or in the current working directory if no path is provided.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create department database if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL UNIQUE,
                            manager TEXT NOT NULL
                        )''')
        
        # Create employee database if not exits
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            department TEXT NOT NULL,
                            salary REAL NOT NULL,
                            hire_date DATE NOT NULL,
                            FOREIGN KEY(department) REFERENCES departments(name)
                        )''')
        
        # create sample data
        employee_data = [
            (1, "Alice", "Sales", 50000, "2021-01-15"),
            (2, "Bob", "Engineering", 70000, "2020-06-10"),
            (3, "Charlie", "Marketing", 60000, "2022-03-20")
        ]

        department_data = [
            (1, "Sales", "Alice"),
            (2, "Engineering", "Bob"),
            (3, "Marketing", "Charlie")
        ]

        # Insert Data
        cursor.executemany("INSERT INTO departments VALUES (?,?,?)", department_data)
        cursor.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", employee_data)
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print(f"Database '{os.path.basename(db_path)}' created successfully.")
        
        conn.commit()

        print(f"Database '{os.path.basename(db_path)}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()
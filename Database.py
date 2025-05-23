from abc import ABC, abstractmethod
import sqlite3

class DatabaseOperationInterface(ABC):
    @abstractmethod
    def create_table(self):
        pass
    
    @abstractmethod
    def insert_data(self):
        pass

    @abstractmethod
    def update_record(self):
        pass
    
    @abstractmethod
    def delete_table(self):
        pass

    @abstractmethod
    def delete_record(self):
        pass
    
    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def close(self):
        pass


class DatabaseManager(DatabaseOperationInterface):
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str, schema: str):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_table(self, table_name: str):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name: str, columns: str, values: tuple):
        placeholders = ', '.join(['?'] * len(values))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def user_exists(self, table, user, password):
        query = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE username = ? AND password = ?)"
        cursor = self.cursor.execute(query, (user, password))
        row = cursor.fetchone()
        return row[0]
    
    def username_exist(self, table, username):
        query = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE username = ?)"
        cursor = self.cursor.execute(query, (username,))
        row = cursor.fetchone()
        return row[0]
    
    def update_record(self, table_name: str, set_columns: str, record_id: int, values: tuple):
        set_cols = set_columns.split(", ")
        set_clause = ', '.join(f"{col}=?" for col in set_cols)
        query = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
        self.cursor.execute(query, values + (record_id,))
        self.conn.commit()

    def get_record(self, table_name: str, conditions: dict):
        where_clause = " AND ".join(f"{col}=?" for col in conditions)
        values = tuple(conditions.values())
        query = f"SELECT * FROM {table_name} WHERE {where_clause}"
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def get_user_role(self, table, username):
        query = f"SELECT role FROM {table} WHERE username = ?"
        cursor = self.cursor.execute(query, (username,))
        row = cursor.fetchone()
        return row[0] if row else None

    def set_user_role(self, table, username, role):
        query = f"UPDATE {table} SET role = ? WHERE username = ?"
        self.cursor.execute(query, (role, username))
        self.conn.commit()

    def delete_record(self, table_name: str, columns: str, values: tuple):
        self.cursor.execute(f'''
        DELETE FROM {table_name}
        WHERE {columns} = ?
        ''', values)

        self.conn.commit()

    def record_exists(self, table, columns, values):
        # Create WHERE clause dynamically
        where_clause = " AND ".join([f"{col} = ?" for col in columns])
        
        query = f"SELECT 1 FROM {table} WHERE {where_clause} LIMIT 1"
        self.cursor.execute(query, values)
        return self.cursor.fetchone() is not None

    def fetch_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()


# c = DatabaseManager(":memory:")
# c.create_table("users", """id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT NOT NULL,
#                 password TEXT NOT NULL
#                 """)

# c.insert_data("users", "username, password", ("admin", "admin"))
# print(c.user_exists("users", "adasdmin", "admin"))
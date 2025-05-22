from Database import DatabaseManager

class Model:
    def __init__(self):
        self.db = DatabaseManager("example.db")
        self.db.create_table("users", """id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
                """)
        self.db.create_table("People", """id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone TEXT,
                birth_date TEXT,
                role TEXT NOT NULL,
                salary INTEGER
                """)
        self.db.create_table("Product", """id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NULL,
                code INTEGER NULL,
                buy_price INTEGER,
                commercial_price INTEGER,
                barcode INTEGER,
                quantity INTEGER
                """)
        
        self.roles = ["admin", "manager", "salesperson"]

        if not self.user_exist("admin", "admin"):
            self.db.insert_data("users", "username, password, role", ("admin", "admin", "admin"))

        self.signed_in_user = None
        self.user_permissions = None

    def user_exist(self, user, password):
        return self.db.user_exists("users", user=user, password=password)
    
    def username_exist(self, user):
        return self.db.username_exist("users", username=user)
    
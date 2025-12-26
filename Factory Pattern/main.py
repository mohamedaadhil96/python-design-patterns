class Database:
    def connect(self):
        raise NotImplementedError


class PostgresDB(Database):
    def connect(self):
        return "Connected to PostgreSQL"

class MySQLDB(Database):
    def connect(self):
        return "Connected to MySQL"

class DatabaseFactory:
    @staticmethod
    def get_database(db_type: str) -> Database:
        if db_type == "postgres":
            return PostgresDB()
        elif db_type == "mysql":
            return MySQLDB()
        else:
            raise ValueError("Unsupported database")
        
        
db = DatabaseFactory.get_database("postgres")
print(db.connect())

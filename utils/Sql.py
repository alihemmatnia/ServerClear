import pyodbc
import env

class SQL:
    def __init__(self) -> None:
        self.connection_string =  (
            f'DRIVER={env.SQL_DRIVER};'
            f'SERVER={env.SQL_HOST};'
            'DATABASE=master;'  
            'Trusted_Connection=yes;'
            #f'UID={env.SQL_USER};'
            #f'PWD={env.SQL_PASSWORD};'
        )
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def drop_all_database(self):
        try:
            db_names = """
            SELECT name 
            FROM sys.databases 
            WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')
            """
            self.cursor.execute(db_names)
            databases = self.cursor.fetchall()
            for db in databases:
                db_name = db[0]
                drop_database_sql = f"DROP DATABASE IF EXISTS [{db_name}]"
                self.cursor.execute(drop_database_sql)
                print(f"Database {db_name} has been dropped successfully.")
            self.cursor.close()
            self.conn.commit()
            self.conn.close()
            print(f"Done drop sql database.")
        except:
            print("Error in SqlServer")
            
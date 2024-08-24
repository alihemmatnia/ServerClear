from pymongo import MongoClient
import env

class Mongo:
    def __init__(self) -> None:
        self.client = MongoClient(env.MONGO_HOST)
        self.db = self.client.list_database_names()
    
    def remove_collections(self):
        for db_name in self.db:
            if db_name not in ["admin", "local", "config"]: 
                self.client.drop_database(db_name)
            print(f"Database '{db_name}' and all its collections have been removed.")
        print(f"All collections have been removed")
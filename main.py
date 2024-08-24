from utils.Docker import Docker
from utils.Sql import SQL
from utils.Mongo import Mongo
from shutil import rmtree
import env
import time

def tasks():
    if env.DOCKER_REGISTRY:
        docker = Docker()
        docker.remove_containers()
        docker.remove_images()
        docker.logout()

    if env.SQL_HOST:
        sql = SQL()
        sql.drop_all_database()

    if env.MONGO_HOST:
        mongo = Mongo()
        mongo.remove_collections()

    if(env.FOLDERS_PATH):
        dirs = str(env.FOLDERS_PATH).split(",")
        for i in dirs:
            rmtree(i)

initial_delay_seconds = 3 * 24 * 60 * 60  # 3 days
time.sleep(initial_delay_seconds)
tasks()

while True:
    time.sleep(1 * 24 * 60 * 60) # 1 day
    tasks()
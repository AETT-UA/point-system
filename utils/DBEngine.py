from loguru import logger
import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

db_port= os.getenv("MYSQL_PORT",3306)
db_name= os.getenv("MYSQL_DATABASE","point_system")
db_username= os.getenv("MYSQL_USER","root") 
db_password= os.getenv("MYSQL_PASSWORD","root")
db_host=os.getenv("MYSQL_HOST","127.0.0.1")
mysql_url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"


Base = declarative_base()

class DBEngine():
    def __init__(self,connect_args={}):
        try:
            self.engine = create_engine(mysql_url, connect_args=connect_args)
            Base.metadata.create_all(self.engine)        
        except Exception as e:
            logger.debug(mysql_url)
            logger.error(e)

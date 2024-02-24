import psycopg2 as dbase
import os
from dotenv import load_dotenv

load_dotenv()



class Base:
    @staticmethod
    def connect(query,type):
        d_base = dbase.connect(
           database=os.getenv("BASE"),
            host=os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD")
        )
        cursor = d_base.cursor()
        cursor.execute(query)
        data_type = ["create","insert","update","delete","select"]
        if type in data_type:
            d_base.commit()
            if type == "create":
                d_base.commit()
                return "created done"
            if type == "insert":
                d_base.commit()
                return "inserted done"

            if type == "update":
                d_base.commit()
                return "updated done"

            if type == "delete":
                d_base.commit()
                return "deleted done"
        else:
            return cursor.fetchall()
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PW = os.environ.get('DB_PW')

conn = pymysql.connect(host='127.0.0.1', user=DB_USER, password=DB_PW, db='PURUN', charset='utf8')
sql = conn.cursor()

def SelectAllData():
    sql.execute("SELECT * FROM PURUN_TB")
    return sql.fetchall()

def SelectSpecialData(id):
    sql.execute(f"SELECT * FROM PURUN_TB WHERE id={id}")
    return sql.fetchall()

def InsertData(data):
    sql.execute(f"INSERT INTO PURUN_TB (STAMP, TEMP, PH, WATER_LEV, LIGHT_LEV, LAST_FEED, PLANT_HEIGHT, PLANT_WIDTH) VALUES ({data})")
    conn.commit()
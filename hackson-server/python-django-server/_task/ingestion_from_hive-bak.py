
%pip install pymysql sqlalchemy
import pandas as pd
import pymysql
from pyhive import hive
from sqlalchemy import create_engine
from IPython.display import display
import spark

db = pymysql.connect(host="pingpong.mysql.database.azure.com",user="pingpong",passwd="Pingpong_123456",db="pingpong" )

def get_df_from_mysql(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    columnDes = cursor.description
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    df = pd.DataFrame([list(i) for i in data], columns=columnNames)
    cursor.close()
    db.close()
    display(df)
    return df

def get_df_from_hive(table_name):
    res = spark.sql("select * from default.{table_name}")
    df = res.pandas()
    display(df)
    return df

def run_ingestion():
    sql = "select * from cusotmer"
    df = get_df_from_mysql(sql)
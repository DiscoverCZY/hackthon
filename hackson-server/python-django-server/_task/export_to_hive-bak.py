%pip install pymysql sqlalchemy
import pandas as pd
import pymysql
from pyhive import hive
from sqlalchemy import create_engine
import spark

def export_data_to_hive(df, table_name):
    df2 = spark.createDataFrame(df)
    df2.write.mode("overwrite").saveAsTable(f"default.{table_name}")
    spark.sql(f"select * from default.{table_name}").show()


def export_data_to_mysql(df, table_name):
    pymysql.install_as_MySQLdb()
    db_string = 'mysql+mysqldb://pingpong:Pingpong_123456@pingpong.mysql.database.azure.com/pingpong?charset=utf8'
    engine = create_engine(db_string)
    df.to_sql("",con=engine,chunksize=10000,if_exists='replace')



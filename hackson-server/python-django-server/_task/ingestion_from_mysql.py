%pip install pymysql IPython sqlalchemy
import pandas as pd
import pymysql
from pyhive import hive
from sqlalchemy import create_engine
from IPython.display import display
import spark


sql = "select * from cusotmer"
db = pymysql.connect(host="pingpong.mysql.database.azure.com",user="pingpong",passwd="Pingpong_123456",db="pingpong" )
cursor = db.cursor()
cursor.execute(sql)
data = cursor.fetchall()

columnDes = cursor.description
columnNames = [columnDes[i][0] for i in range(len(columnDes))]
df = pd.DataFrame([list(i) for i in data], columns=columnNames)
cursor.close()
db.close()
display(df)

df2 = spark.createDataFrame(df)
df2.write.mode("overwrite").saveAsTable(f"default.ingested_customer")
spark.sql(f"select * from default.ingested_customer").show()
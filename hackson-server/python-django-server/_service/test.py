import pandas as pd
import pymysql
from IPython.display import display
# from tabulate import tabulate
import spark
import numpy as np
from sqlalchemy import create_engine

db = pymysql.connect(host="localhost",user="root",passwd="xiaowoniu@23",db="sakila" )

sql = "SELECT * FROM customer"

cursor = db.cursor()
cursor.execute(sql)
data = cursor.fetchall()

columnDes = cursor.description  # 获取连接对象的描述信息
columnNames = [columnDes[i][0] for i in range(len(columnDes))]
df = pd.DataFrame([list(i) for i in data], columns=columnNames)
cursor.close()
db.close()

print("cursor.description中的内容：", columnNames)

df.query("customer_id>595")

display(df.query("customer_id>595"))



df2 = spark.createDataFrame(df)
# Save df to a new table in Hive
df.write.mode("overwrite").saveAsTable("test_db.test_table2")
# Show the results using SELECT
spark.sql("select * from test_db.test_table2").show()

# pymysql.install_as_MySQLdb()
# DB_STRING = 'mysql+mysqldb://root:xiaowoniu%4023@localhost/sakila?charset=utf8'
# engine = create_engine(DB_STRING)

# db = pymysql.connect(host="localhost",user="root",passwd="xiaowoniu@23",db="sakila" )

# df.query("customer_id>595").to_sql('test3',con=engine,chunksize=10000,if_exists='replace')



# 将data写入数据库，如果表存在就替换，将data的index也写入数据表，写入字段名称为id_name
# df.to_sql('table_name',con='engine',chunksize=10000,if_exists='replace',index=True,index_label='id_name')
# 将data写入数据库，如果表存在就追加
# df.to_sql('table_name',con='engine',chunksize=10000,if_exists='append')
# 将data写入数据库，如果表存在就替换，指定col_1的字段类型为char(4)
# df.to_sql('table_name',con='engine',chunksize=10000,if_exists='replace,dtype={'col_1':CHAR(4)})
# 如果data数据量大，需要设置合理的chunksize值，这和数据库缓存大小有关，
# 可以设置在50000-10000，如果提示数据库连接超时错误，就将size值调小。
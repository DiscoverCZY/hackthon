
import pandas as pd
import pymysql #该库用于python和mysql的连接
#打开数据库连接，db为数据库名称
import spark

db = pymysql.connect(host="localhost",user="root",passwd="xiaowoniu@23",db="sakila" )

def get_df_from_db(sql):
    cursor = db.cursor()  # 使用cursor()方法获取用于执行SQL语句的游标
    cursor.execute(sql)  # 执行SQL语句
    """
    使用fetchall函数以元组形式返回所有查询结果并打印出来
    fetchone()返回第一行，fetchmany(n)返回前n行
    游标执行一次后则定位在当前操作行，下一次操作从当前操作行开始
    """
    data = cursor.fetchall()

    # 下面为将获取的数据转化为dataframe格式
    columnDes = cursor.description  # 获取连接对象的描述信息
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]  # 获取列名
    df = pd.DataFrame([list(i) for i in data], columns=columnNames)  # 得到的data为二维元组，逐行取出，转化为列表，再转化为df

    """
    使用完成之后需关闭游标和数据库连接，减少资源占用,cursor.close(),db.close()
    db.commit()若对数据库进行了修改，需进行提交之后再关闭
    """
    cursor.close()
    db.close()

    print("cursor.description中的内容：", columnDes)
    return df


def get_df_from_file(filepath):
    df = (spark.read
      .format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load("/databricks-datasets/samples/population-vs-price/data_geo.csv")
    )
    return df


def get_df_from_pandas():
    data = [[1, "Elia"], [2, "Teo"], [3, "Fang"]]
    pdf = pd.DataFrame(data, columns=["id", "name"])
    df1 = spark.createDataFrame(pdf)
    df2 = spark.createDataFrame(data, schema="id LONG, name STRING")
    df2.filter


def join_data(df1, df2, id):
    joined_df = df1.join(df2, how="inner", on=id)
    return joined_df


# def filter_data(df):




sql1 = "SELECT * FROM customer"
df1 = get_df_from_db(sql1)

sql2 = "SELECT * FROM payment"
df2 = get_df_from_db(sql2)




print(join_data(df1,df2,"customer_id"))
# display(dff)
# print(dff.filter("store_id = 2"))

# dff.write
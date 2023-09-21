%pip install pymysql sqlalchemy IPython
from IPython.display import display
from pyspark.python.pyspark.shell import spark

res = spark.sql("select * from default.ingested_customer")
df = res.pandas()
display(df)

df = df.query("age > 75")
df = df.dropna()
display(df)

df2 = spark.createDataFrame(df)
df2.write.mode("overwrite").saveAsTable(f"default.transformed_customer")
spark.sql(f"select * from default.transformed_customer").show()
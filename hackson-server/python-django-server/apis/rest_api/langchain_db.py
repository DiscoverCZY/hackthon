# 导入LangChain模块
from langchain import OpenAI, SQLDatabase
from urllib.parse import quote_plus
import os
import ast

from .models_location import Location

import json
# 创建一个SQLDatabaseChain的实例，连接到本地mysql数据库
# db = lc.SQLDatabaseChain(
#     database="world", # 数据库名称
#     user="xiaowoniu", # 用户名
#     password="xiaowoniu@2023", # 密码
#     host="localhost", # 主机地址
#     port=3306, # 端口号
#     dialect="mysql" # 数据库方言
# )

from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

pwd="xiaowoniu@23"

# pwd="!9840925CzYY@"
print(quote_plus(pwd))
# db = SQLDatabase.from_uri("mysql+pymysql://pingpong:%219840925CzYY%40@20.239.220.118/test")
db = SQLDatabase.from_uri("mysql+pymysql://root:xiaowoniu%4023@localhost/world")
os.environ["OPENAI_API_KEY"]="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"
llm = OpenAI(temperature=0, verbose=True)

from langchain.prompts.prompt import PromptTemplate

_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Use the following format:

Answer: "Final answer here"

Only use the following tables:

{table_info}

If someone asks for the table foobar, they really mean the employee table.

Question: {input}"""
PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE
)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, return_direct=True, use_query_checker=True)
# response = db_chain.invoke({"question":"how many data in inventory"})
# print(response)


# result = db_chain("get all data in the inventory")
output = db_chain.run("get cities from california district and show all columns in city")


# return_intermediate_steps=True
# output = db_chain("get cities from USA and show all columns in city")
# output = db_chain("get cities from california district and show all columns in city")


print(output)

data = ast.literal_eval(output)

# Convert the data into a list of dictionaries
converted_data = [{'ID': item[0],
                   'City': item[1],
                   'Country': item[2],
                   'State': item[3],
                   'Population': item[4]} for item in data]
locations = [Location(*item) for item in data]
# Print the converted data
# for location in converted_data:
#     print(location)

for location in locations:
    print(location.ID)
    print(location.City)
    print(location.Country)
    print(location.State)
    print(location.Population)



# result['intermediate_steps']

# db_chain.atransform

# # 启动sql检查特性，自动修复错误sql
# db.enable_sql_check()

# # 设施返回GPT迭代思考的中间步骤
# db.enable_intermediate_steps()

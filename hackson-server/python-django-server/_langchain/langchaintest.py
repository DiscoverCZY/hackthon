# 导入LangChain模块
from langchain import OpenAI, SQLDatabase
from urllib.parse import quote_plus
import os
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

pwd="xiaowoniu@2023"
db = SQLDatabase.from_uri("mysql+pymysql://xiaowoniu:xiaowoniu%402023@localhost/world")
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

db_chain = SQLDatabaseChain.from_llm(llm, db,prompt=PROMPT, verbose=True)

db_chain.run("统计所有说英语的国家")

# db_chain.atransform

# # 启动sql检查特性，自动修复错误sql
# db.enable_sql_check()

# # 设施返回GPT迭代思考的中间步骤
# db.enable_intermediate_steps()

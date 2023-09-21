from  _langchain.langchain_db import main
from _databricks.workspace import connect_workspace
# main()

workspace = connect_workspace()
cls=workspace.cluster.list_clusters()
print(cls)
from .workspace import connect_workspace
from _tools.db import connector

mock_run={"id":"xxxxxx"}

job_id=636491053601361

job_run={
  "job_id": job_id,
  "idempotency_token": "string",
  "jar_params": [
    "string"
  ],
  "notebook_params": {
    "property1": "string",
    "property2": "string"
  },
  "python_params": [
    "string"
  ],
  "spark_submit_params": [
    "string"
  ],
  "python_named_params": {
    "property1": "string",
    "property2": "string"
  },
  "pipeline_params": {
    "full_refresh": True
  },
#   "sql_params": {
#     "property1": "string",
#     "property2": "string"
#   },
#   "dbt_commands": [
#     "string"
#   ]
}

  
def save_run(params):
      run_id=params.get('run_id')
      data = {"run_id":run_id,"job_id":job_id}

      connector.insert('workflow_run',data)

def start(params):
      print(f'start {params}')
      db = connect_workspace()
      resp = db.jobs.run_now(**job_run)
      save_run(resp)
      
      return resp


def load_list(params):
    db = connect_workspace()
    resp = db.jobs.list_runs({})
    runs=resp.get('runs')
    return runs
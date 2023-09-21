import base64
import datetime
import json

from _tools.db import connector

CLUSTER_DICT = {
    "0920-121348-dddiu2sz": "MASTER-CLUSTER-COMPUTER"
}


def deploy(workflow_id: int):
    workflow = connector.query_one("SELECT * FROM workflow WHERE id = %d", workflow_id)
    if workflow is None:
        raise Exception("workflow definition not found")
    tasks = connector.execute(
        "SELECT * FROM workflow_task wt INNER JOIN data_funcs af ON wt.func_id = af.id WHERE wt.workflow_id = %d",
        workflow_id)
    if tasks is None or len(tasks) == 0:
        raise Exception("workflow's tasks definition not found")

    deployed = []
    for task in tasks:
        definition = task['definition']
        single = {
            'task_key': task['name'],
            'run_if': 'ALL_SUCCESS',
            'existing_cluster_id': workflow['cluster_id'],
            'depends_on': ''
        }


def create(name: str, cluster_id: str):
    # check workflow existed
    existed_id = get_workflow_id(name)
    if existed_id is not None:
        raise Exception(f"workflow {name} has been existed, cannot create it")
    # add workflow
    if len(name) == 0 or len(cluster_id) == 0:
        raise Exception("missing the required parameters of creating the workflow")
    data = {'name': name, 'cluster_id': cluster_id,
            'cluster_name': CLUSTER_DICT[cluster_id],
            'status': 1, 'create_time': datetime.datetime.now()}
    connector.insert('workflow', data)
    created_id = get_workflow_id(name)
    if created_id is None:
        raise Exception(f"create workflow {name} failed")
    # add tasks / only create the default tasks now
    __create_default_tasks(created_id)


def get_workflow_id(name: str):
    if len(name) == 0:
        return
    result = connector.query_one("SELECT * FROM workflow WHERE name = %s", name)
    if result is None:
        return
    return result['id']


def __create_default_tasks(workflow_id: int):
    __create_task('ingestion', workflow_id, 1, [])
    __create_task('transformation', workflow_id, 2, ['ingestion'])
    __create_task('quantity_check', workflow_id, 3, ['transformation'])
    __create_task('process_failed', workflow_id, 4, ['process_failed'])
    __create_task('process_success', workflow_id, 5, ['process_success'])


def __create_task(name: str, workflow_id: int, func_id: int, depends_on: []):
    if len(name) == 0 or workflow_id is None or func_id is None:
        raise Exception("missing the required parameters of creating the task")
    depends_on_joined = None if len(depends_on) == 0 else ','.join(depends_on)
    data = {'name': name, 'workflow_id': workflow_id, 'func_id': func_id,
            'depends_on': depends_on_joined, 'create_time': datetime.datetime.now()}
    connector.insert('workflow_task', data)


def __create_default_funcs():
    __create_func('ingestion_module'
                  , json.dumps({'notebook_task': {'notebook_path': '/Shared/ingestion.py', 'source': 'WORKSPACE'}}))
    __create_func('transformation_module', ''
                  ,
                  json.dumps({'notebook_task': {'notebook_path': '/Shared/transformation.py', 'source': 'WORKSPACE'}}))
    __create_func('quantity_check_module', ''
                  ,
                  json.dumps({'notebook_task': {'notebook_path': '/Shared/quantity_check.py', 'source': 'WORKSPACE'}}))
    __create_func('process_failed_module', ''
                  ,
                  json.dumps({'notebook_task': {'notebook_path': '/Shared/process_failed.py', 'source': 'WORKSPACE'}}))
    __create_func('process_success_module', ''
                  ,
                  json.dumps({'notebook_task': {'notebook_path': '/Shared/process_success.py', 'source': 'WORKSPACE'}}))


def __create_func(name: str, definition: str, func_type='CODE'):
    data = {'name': name, 'func_type': func_type,
            'definition': base64.b64encode(definition.encode('utf-8')).decode('utf-8'),
            'create_time': datetime.datetime.now()}
    connector.insert('data_funcs', data)


__create_default_funcs()

# create('first workflow', '0920-121348-dddiu2sz')

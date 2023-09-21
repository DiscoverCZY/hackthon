import datetime

from _tools.db import connector

CLUSTER_DICT = {
    "0920-121348-dddiu2sz": "MASTER-CLUSTER-COMPUTER"
}


def deploy(workflow_id: int):
    list = connector.execute(f"SELECT * FROM workflow WHERE id = %d", workflow_id)
    if list is None or len(list) == 0:
        raise Exception("workflow defined not found")


def create(name: str, cluster_id: str):
    # add workflow
    if len(name) == 0 or len(cluster_id) == 0:
        raise Exception("workflow name and cluster id are required")
    data = {'name': name, 'cluster_id': cluster_id,
            'cluster_name': CLUSTER_DICT[cluster_id],
            'status': 1, 'create_time': datetime.datetime.now()}
    connector.insert('workflow', data)
    # add tasks



# def __create_tasks():


create('first workflow', '0920-121348-dddiu2sz')

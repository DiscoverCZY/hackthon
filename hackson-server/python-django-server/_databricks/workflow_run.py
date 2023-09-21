from .workspace import connect_workspace

mock_run={"id":"xxxxxx"}


def start_workspace(params):
      id = params.get('id')
      name = params.get('name')
      print(f'start {id} {name}')

      return params


def load_list(params):
    db = connect_workspace()
    runs = db.jobs.list_runs({})
    return runs
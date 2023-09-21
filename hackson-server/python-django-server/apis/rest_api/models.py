import json


def wrap(data=None, code=200, message='success'):
    payload = None
    if data is not None:
        payload = json.loads(json.dumps(data, ensure_ascii=False, default=lambda obj: obj.__dict__))
    return {'data': payload, 'code': code, 'message': message}


class ChatModal:
    def __init__(self):
        self.modal = "chart"
        self.type = "bar"
        self.name = "seris-1"
        self.categories = [1991, 1992]
        self.data = [30, 40]


class Location:
    def __init__(self, ID, City, Country, State, Population):
        self.ID = ID
        self.City = City
        self.Country = Country
        self.State = State
        self.Population = Population


class Workflow:
    def __init__(self, name: str, cluster_id: str) -> None:
        self.name = name
        self.cluster_id = cluster_id



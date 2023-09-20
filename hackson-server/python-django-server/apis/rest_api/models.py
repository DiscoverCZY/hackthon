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

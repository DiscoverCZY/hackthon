class ChatModal:
    def __init__(self):
        self.modal = "chart"
        self.type = "bar"
        self.name = "seris-1"
        self.categories = [1991, 1992]
        self.data = [30, 40]


class Customer:
    def __init__(self, id, name, phone, email, address, postal, region, country, sex, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.postal = postal
        self.region = region
        self.country = country
        self.sex = sex
        self.age = age
        # self.currency = currency
        # self.level = level
        # self.bank_count = bank_count
        # self.description = description
        # self.register_date = register_date

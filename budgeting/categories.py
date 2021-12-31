class categories:
    def __init__(self, name, money_allocated):
        self.name = name
        self.money_allocated = money_allocated

categories_list = [
    categories("bills", 0.0),
    categories("food", 0.0),
    categories("shopping", 0.0),
    categories("luxuries", 0.0),
    categories("savings", 0.0)
]
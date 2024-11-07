class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args:
            cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors = None):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print (f"{self.name} снесен, но он останется в истории")

h1 = House('ЖК Эльбрус',30)
print(House.houses_history)
h2 = House('ЖК Акация', 25)
print(House.houses_history)
h3 = House('ЖК Аргентина', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)



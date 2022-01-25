

class Planet:
    def __init__(self, name, diameter_km):
        self.name = name
        self.diameter_km = diameter_km

e = Planet("Earth" , 12742)

print(e.name, e.diameter_km)


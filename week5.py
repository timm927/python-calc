class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level  

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power} at level {self.level}!")

    def action(self):
        print(f"{self.name} is ready to act!")

class Flyer(Superhero):
    def __init__(self, name, power, level, wing_span):
        super().__init__(name, power, level)
        self.wing_span = wing_span 

    def action(self):  
        print(f"{self.name} is flying with a wingspan of {self.wing_span}m!")

class Speedster(Superhero):
    def __init__(self, name, power, level, top_speed):
        super().__init__(name, power, level)
        self.top_speed = top_speed  

    def action(self): 
        print(f"{self.name} is running at {self.top_speed} km/h!")

class Strongman(Superhero):
    def __init__(self, name, power, level, strength_tons):
        super().__init__(name, power, level)
        self.strength_tons = strength_tons 

    def action(self): 
        print(f"{self.name} lifts {self.strength_tons} tons effortlessly!")

# Create superhero objects
heroes = [
    Flyer("SkyWing", "Air Control", 90, 15),
    Speedster("FlashBolt", "Super Speed", 85, 350),
    Strongman("Herculex", "Super Strength", 95, 50)
]

# Introduce heroes
for hero in heroes:
    hero.introduce()
    hero.action()
 
    
class Ship:
    def __init__(self, name, power, armour):
        self.name = name
        self.power = power
        self.armour = armour
    
    def info(self):
        return f"Name: {self.name}, Power: {self.power}, Armour: {self.armour}"

class Squad:
    def __init__(self):
#        super().__init__(power, armour)
        self.ships = []

    def add_ship(self, name, power, armour):
        ship = Ship(name, power, armour)
        self.ships.append(ship)

    def show_squad_info(self):
        for i, ship in enumerate(self.ships, 1):
            print(f"{ship.info()}")

class Player:
    def __init__(self, name):
        self.name = name
        self.squad = Squad()

    def show_player_squad_info(self):
        print (f"{self.name}'s squad:")
        self.squad.show_squad_info()

print()

Player1 = Player("Player1")

Player1.squad.add_ship("aircraft11", 5, 5)  
Player1.squad.add_ship("combat11", 4, 4)  
Player1.squad.add_ship("submarine11", 3, 3)
Player1.squad.add_ship("submarine12", 3, 3)
Player1.squad.add_ship("patrol11", 2, 2)
Player1.squad.add_ship("patrol12", 2, 2)
Player1.squad.add_ship("usv11", 1, 1)
Player1.squad.add_ship("usv12", 1, 1)
Player1.squad.add_ship("usv13", 1, 1)
Player1.squad.add_ship("usv14", 1, 1) 

Player1.show_player_squad_info()

print()

Player2 = Player("Player2")

Player2.squad.add_ship("aircraft21", 5, 5)  
Player2.squad.add_ship("combat21", 4, 4)  
Player2.squad.add_ship("submarine21", 3, 3)
Player2.squad.add_ship("submarine22", 3, 3)
Player2.squad.add_ship("patrol21", 2, 2)
Player2.squad.add_ship("patrol22", 2, 2)
Player2.squad.add_ship("usv21", 1, 1)
Player2.squad.add_ship("usv22", 1, 1)
Player2.squad.add_ship("usv23", 1, 1)
Player2.squad.add_ship("usv24", 1, 1) 

Player2.show_player_squad_info()

print()
import random
import json

class Ship:
    def __init__(self, name, power, armour):
        self.name = name
        self.power = power
        self.armour = armour

    def info(self):
        return f"Name: {self.name}, Power: {self.power}, Armour: {self.armour}"

    def take_damage(self, amount):
        self.armour = max(0, self.armour - amount)
        print(f"{self.name} takes {amount} damage, armour left: {self.armour}")

    def is_destroyed(self):
        return self.armour <= 0

    def dict_for_json(self):
        return {
            "Name": self.name,
            "Power": self.power,
            "Armour": self.armour
        }


class Squad:
    def __init__(self):
        self.ships = []

    def add_ship(self, name, power, armour):
        ship = Ship(name, power, armour)
        self.ships.append(ship)

    def get_alive_ships(self):
        return [ship for ship in self.ships if not ship.is_destroyed()]

    def dict_for_json(self):
        return [ship.dict_for_json() for ship in self.ships]


class Player:
    def __init__(self, name):
        self.name = name
        self.squad = Squad()

    def show_player_squad_info(self):
        print(f"{self.name}'s squad:")
        for ship in self.squad.get_alive_ships():
            print(f"{ship.name} - Power: {ship.power}, Armour: {ship.armour}")

    def dict_for_json(self):
        return {
            "name": self.name,
            "Squadlist": self.squad.dict_for_json()
        }

def log_battle(log_data, filename="battle_log.json"):
    try:
        with open(filename, "r") as file:
            battle_data = json.load(file)  
    except FileNotFoundError:
        battle_data = []  

    battle_data.append(log_data)  

    with open(filename, "w") as file:
        json.dump(battle_data, file, indent=4) 

def battle_round(player1, player2, round_num):
    print(f"\n--- Battle Round ---")
    alive_ships_p1 = player1.squad.get_alive_ships()
    alive_ships_p2 = player2.squad.get_alive_ships()

    log_data = {"round": round_num, "attacks": []}

    for ship in alive_ships_p1:
        if alive_ships_p2:
            target = random.choice(alive_ships_p2)
            damage = round(random.uniform(0.25*ship.power, ship.power), 3)
            target.take_damage(damage)
            
               # Логування атаки
            log_data["attacks"].append({
                "attacker": ship.name,
                "attacker_player": player1.name,
                "target": target.name,
                "target_player": player2.name,
                "damage": damage,
                "target_armour_left": target.armour
            })

            if target.is_destroyed():
                alive_ships_p2.remove(target)

    for ship in alive_ships_p2:
        if alive_ships_p1:
            target = random.choice(alive_ships_p1)
            damage = round(random.uniform(0.25*ship.power, ship.power), 3)
            target.take_damage(damage)
            
            log_data["attacks"].append({
                "attacker": ship.name,
                "attacker_player": player1.name,
                "target": target.name,
                "target_player": player2.name,
                "damage": damage,
                "target_armour_left": target.armour
            })

            if target.is_destroyed():
                alive_ships_p1.remove(target)

    log_battle(log_data)

player1 = Player("Player1")
player1.squad.add_ship("Aircraft1", 120, 400)
player1.squad.add_ship("Combat1", 100, 300)
player1.squad.add_ship("Submarine11", 90, 200)
player1.squad.add_ship("Submarine12", 90, 200)
player1.squad.add_ship("Patrol11", 60, 140)
player1.squad.add_ship("Patrol12", 60, 140)
player1.squad.add_ship("Usv11", 70, 80)
player1.squad.add_ship("Usv12", 70, 80)
player1.squad.add_ship("Usv13", 70, 80)
player1.squad.add_ship("Usv14", 70, 80)

player1.show_player_squad_info()

print()

player2 = Player("Player2")
player2.squad.add_ship("Aircraft2", 120, 400)
player2.squad.add_ship("Combat2", 100, 300)
player2.squad.add_ship("Submarine21", 90, 200)
player2.squad.add_ship("Submarine22", 90, 200)
player2.squad.add_ship("Patrol21", 60, 140)
player2.squad.add_ship("Patrol22", 60, 140)
player2.squad.add_ship("Usv21", 70, 80)
player2.squad.add_ship("Usv22", 70, 80)
player2.squad.add_ship("Usv23", 70, 80)
player2.squad.add_ship("Usv24", 70, 80)

player2.show_player_squad_info()

round_count = 1
while player1.squad.get_alive_ships() and player2.squad.get_alive_ships():
    print(f"\n--- Round {round_count} ---")
    battle_round(player1, player2, round_count)
    round_count += 1

if player1.squad.get_alive_ships():
    print("\nPlayer 1 wins!")
elif player2.squad.get_alive_ships():
    print("\nPlayer 2 wins!")
else:
    print("\nIt's a draw!")

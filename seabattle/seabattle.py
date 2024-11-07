import random

class Ship:
    def __init__(self, power, armour):
        self.power = power
        self.armour = armour

class Squad(Ship):
    def __init__(self):
        super.__init__()

    aircraft = Ship(5,5)
    combat = Ship(4,4)
    submarine1 = Ship(3,3)
    submarine2 = Ship(3,3)
    patrol1 = Ship(3,3)
    patrol2 = Ship(3,3)
    usv1 = Ship(1,1)
    usv2 = Ship(1,1)
    usv3 = Ship(1,1)
    usv4 = Ship(1,1)

    Squadlist = [aircraft, combat, submarine1, submarine2, patrol1,
                  patrol2, usv1, usv2, usv3, usv4]

Squad1 = Squad
print(Squad1.Squadlist) 


class Player(Squad):
    def __init__(self, player1, player2):
        super.__init__()
        self.player1 = player1
        self.player2 = player2

    def hit(self):
        self.armour.player2 = self.armour.player2 - (self.power.player1*random(0.2 - 1))
        self.armour.player1 = self.armour.player1 - (self.power.player2*random(0.2 - 1))
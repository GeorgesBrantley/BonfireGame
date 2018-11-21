#imports


class hero:
    name = ""
    heroID = ""
    level = 1
    xp = 0
    nextLevel = 3

    carryLimit = 2
    actionLimit = 2
    conserve = 0
    
    # Power Decks
    strDeck = []
    intDeck = []
    agiDeck = []
    godDeck = [] 

    # Weapons
    weapons = []
    currentCarry = 0
    # Power Dice
    pwrDice = []

    def __init__(self,name,ID,lvl):
        # NAME and init hero
        self.name = name
        self.heroID = ID
        self.level = level
        self.xp = 0
        self.nextLevel = 3
        # TODO generate DECKS
        currentCarry = 0
        # TODO get weapons
        # TODO generate DICE

    def getWeapon(self,weapon):
        if weapon.weight + self.currentCarry <= self.carryLimit:
            # space in inventory
            self.weapons.append(weapon)
            return 1
        elif weapon.weight > carryLimit:
            # no space, refuse!
            return 0
        else:
            # item needs to be swapped!
            # Discard Weapon/s try again

    def levelUp(self):
        # decrease current xp
        self.xp -= self.nextLevel 
        # increase requireents for next level
        self.nextLevel += 2
        # TODO improve yourself


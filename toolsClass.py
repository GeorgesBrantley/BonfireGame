#imports

class card:
    name = ""
    # ID contains tags for what the card's aciton does
    # dodge,move,hurt....
    cID = ""
    lvl = 0
    pwr = ""

    # amount of power it gives
    pwrLvl = 0
    # if it is reusable
    reuse = False
    # action String
    actStr = ""

    # integer used for damage/movement/anything
    usedNumber = 0

    def __init__(self,name,cID,lvl,pwr,pwrLvl,reuse,actStr,usedNumber):
        self.name = name
        self.cID = cID
        self.lvl = lvl
        self.pwr = self.pwr
        self.pwrLvl = pwrLvl
        self.reuse = reuse
        self.actStr = actStr
        self.usedNumber = usedNumber 


class weapon:
    name = ""
    wID = ""
    wLvl = 0
    majorPwr = []

    weight = 0
    actionList = []

    def __init__(self, name, wID, wLvl, majorPwr, weight, actions):
        self.name=name
        self.wID = wID
        self.wLvl = wLvl
        self.majorPwr = majorPwr
        self.weight = weight
        self.actionList = actions

class weapon_action:
    # needs work
    name = ""
    waID = ""
    strEffect = ""

    # requirements needed to play
    strReq = 0
    intReq = 0
    agiReq = 0
    godReq = 0

    damage = 0
    secondNum = 0

    def __init__(self,name,waID,strEffect,\
            damage,strReq,intReq,agiReq,godReq,secondNum):
        self.name = name
        self.waID = waID
        self.strEffect = strEffect
        self.damage = damage
            
        self.strReq = strReq
        self.intReq = intReq
        self.agiReq = agiReq
        self.godReq = godReq
        self.secondNum = secondNum 

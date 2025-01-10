

class HSRAction:
    def __init__(self, skillPoint, energyGeneration, special=False, ultimate=False, outsideTrigger=False):
        self.skillPoint = skillPoint
        self.energyGeneration = energyGeneration
        self.special = special # actions that cant be picked during a units action i.e fua, ult etc.
        self.ultimate = ultimate
        self.outsideTrigger = outsideTrigger # fua etc.

    def doNothing():
        pass



# a generic basic attack for fallback
basicAttack = [HSRAction(1, 20)]

# class to handle data related to characters
class HSRCharacter:
    def __init__(self, name, baseSpd, bonusSpd, maxEnergy, maxCycleCount, actionList=basicAttack, percentSpeed=0, startingEnergy=0):
        self.name = name
        self.baseSpd = baseSpd
        self.bonusSpd = bonusSpd
        self.ratioSpd = percentSpeed/100
        self.maxEnergy = maxEnergy
        self.energy = 0
        self.actionValue = 0
        self.actionsTakenCycle = [0]*maxCycleCount
        self.possibleActions = basicAttack
        self.enegyPerCycle  = [0]*maxCycleCount

    def baseActionValue(self):
        self.actionValue =  10000/(self.baseSpd*(1+self.ratioSpd)+self.bonusSpd)
herta = HSRCharacter("The Herta", 99, 5, 220, 10, percentSpeed=33)



# values for local testing

# g_maxCycleCount = 10
# the first cycle (the "0 cycle") is 50% longer
# g_cycleActionValues = [150] + [100] * (g_maxCycleCount-1)
# g_characterList = [HSRCharacter("The Herta", 99, 5, 220, g_maxCycleCount, percentSpeed=33),
                 # HSRCharacter("Robin", 102, 0, 0, 160, g_maxCycleCount),
                 # HSRCharacter("Aventurine", 106, 0, 0, 110, g_maxCycleCount),
                 # HSRCharacter("Jade", 103, 0, 0, 140, g_maxCycleCount),
                 # ]

# local testing

# g_characterList[0].baseActionValue()
# print(g_characterList[0].actionValue)
# print(len(g_characterList[0].actionsTakenCycle))

# doesnt simulate enemy actions because thats unreasonable
def simulateActionOrder(maxCycleCount, cycleActionValues, characterList):
    print(characterList[0].possibleActions[0].energyGeneration)
    # setup phase
    for character in characterList:
        # set each characters action value
        character.baseActionValue()

    # cycle Loop
    for cycle in range(maxCycleCount):

        print("\ncycle:", cycle, "\n")
        # set the cycle action value
        cycleActionValue = cycleActionValues[cycle]

        # the cycle ends when 150 or 100 action value has elapsed
        while(cycleActionValue>0):
            actingCharacter = None # next character to act
            lowestActionValue = 200 # no character should ever be this slow

            # checks which character has the lowest action value
            for character in characterList:
                if character.actionValue < lowestActionValue:
                    lowestActionValue = character.actionValue
                    actingCharacter = character

            # checks whether the cycle ends before the character acts
            if lowestActionValue>cycleActionValue:
                for character in characterList:
                    character.actionValue -= cycleActionValue
                break

            # moving cycle action value forward
            cycleActionValue -= lowestActionValue

            # moves every character forward by the lowest action value
            for character in characterList:
                character.actionValue -= lowestActionValue

            # reset the actionvalue of the acting character and increment their action count

            # pick and execute Action
            # TODO
            actingCharacter.energy += actingCharacter.possibleActions[0].energyGeneration

            actingCharacter.baseActionValue()
            actingCharacter.actionsTakenCycle[cycle] += 1

            print(actingCharacter.name, actingCharacter.actionsTakenCycle[cycle])

        for character in characterList:
            character.enegyPerCycle[cycle] = character.energy

    # count the total amount of actions
    for character in characterList:
        sum = 0
        for cycleCount in character.actionsTakenCycle:
            sum += cycleCount
        print(f"Total actions taken by {character.name}:", sum)

    # aggregate all lists of actions per cycle into one big list of lists
    aggregatedCycleLists = []
    for character in characterList:
        aggregatedCycleLists.append(character.actionsTakenCycle)
    aggregatedEnergyLists = []
    for character in characterList:
        aggregatedEnergyLists.append(character.enegyPerCycle)

    return aggregatedCycleLists, aggregatedEnergyLists


# local testing
# simulateActionOrder(g_maxCycleCount, g_cycleActionValues, g_characterList)


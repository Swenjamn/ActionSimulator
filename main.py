from draw import *
from actionCalculator import *


maxCycleCount = 10
# the first cycle (the "0 cycle") is 50% longer
cycleActionValues = [150] + [100] * (maxCycleCount-1)
characterListValues = [HSRCharacter("The Herta", 99, 5, 220, maxCycleCount, percentSpeed=33),
                 HSRCharacter("Robin", 102, 0, 160, maxCycleCount),
                 HSRCharacter("Aventurine", 106, 0, 110, maxCycleCount),
                 HSRCharacter("Jade", 103, 0, 140, maxCycleCount),
                 ]

def main():
    cycles, energy = simulateActionOrder(maxCycleCount, cycleActionValues, characterListValues)
    g_characterNameList = []
    for character in characterListValues:
        g_characterNameList.append(character.name)

    draw(maxCycleCount, g_characterNameList, cycles, energy)

#TODO energy and ults as well as other out of action effects
#TODO advance forward and mid combat speed changes
#TODO timeline drawing of actions
main()

'''
Necessary Evil
Random Adventure Generator

Implementation and enhancement of the table on p80
of the Necessary Evil setting book.

'''

import random

# General types of missions to select from
MissionType = ['Recovery 1','Recovery 2','Reconnaissance','Recruitment','Sabotage','Search and Destroy']

# Dictionary of Specific Missions for each mission type
Missions = {
    'Recovery 1' : [10,'Standard Mission',
                    12,'Colonel Clones Legacy (p106)',
                    14,'Robotic Doom (p112)',
                    16,'The Safe (p133)',
                    18,'Ep 2: The Underground Irregulars (p85)',
                    20,'Ep 4: The Hanged Man (p88)'],
    'Recovery 2' : [10,'Standard Mission',
                    12,'Red Cross (p131)',
                    14,'Midnight in the Garden of Dr. Devolution (p114)',
                    16,'Parallel Lives (p117)',
                    18,'Ep 5: Crossbreeds (p90)',
                    20,'Ep 6: Raiders of the Lost Temple (p92)'],
    'Reconnaissance' : [10,'Standard Mission',
                        12,'Beware the Sleeper (p100)',
                        14,'The Trouble at Hydrobase 11 (p103)',
                        16,'A Day in the Life of a Hero (p118)',
                        18,'The Return of 4-Star and Lucky (p128)',
                        20,'Ep 3: The First Family (p86)'],
    'Recruitment' : [10,'Standard Mission',
                    12,'Return of the Monolith (p101)',
                    14,'Vendetta (p104)',
                    16,'Blood Cult (p111)',
                    17,'The Rescue (p122)',
                    18,'My Enemys Enemy (p123)',
                    19,'The Alien Objector (p130)',
                    20,'Ep 7: Turncoat (p94)'],
    'Sabotage' : [10,'Standard Mission',
                    12,'Fire From The Sky (p109)',
                    14,'Pulling the Plug (p108)',
                    16,'The Chamber (p119)',
                    17,'The Dogs of War (p121)',
                    18,'Alien Bloodsport (p116)',
                    19,'Terror in Tarrytown (p126)',
                    20,'Ep 8: Assault on Satellite 15 (p95)'],
    'Search and Destroy' : [12,'Standard Mission',
                    14,'Cult of the Space Gods (p100)',
                    16,'Hunting the Hunters (p133)',
                    18,'Stalker in Star City (p124)',
                    20,'Ep 9: And a Villain Shall Lead Them (p96)']     
    }

# Additional information for standard missions

Location = ['Factory','Laboratory','Detention Camp','Vsori Base','Sewers',
            'Monorail Station','City Intersection','Park','Office Building','Restaurant',
            'Store/Mall','Truck Convoy']
Opposition = [2,'Rogue Supervillain, Hyper-Drones, Infiltrators, Groks',
              4,'Warlord, Battle-Master, Solo with Fin Soldiers and Drones',
              6,'1 Commander per 10 Fins',
              9,'3 Ktharen Troopers per 10 Drones',
              11,'Heavy Opposition',
              12,'Very Heavy Opposition'
              ]
# List of completed missions
# If a mission is on this list, the program will randomly pick another mission
Completed_Missions = ['Ep 2: The Underground Irregulars (p85)']

# Dice rolling function.  Can add multiple dice such as 2D6
def DiceRole (diceType=6, diceNum=1):
    finalRole = 0
    for toss in range(0,diceNum):
        finalRole += random.randrange(1,diceType+1)
    return finalRole

def SearchList (inputList = [],searchString = ''):
    for item in inputList:
        if item == searchString:
            return True
            break
    return False

def GenerateMission ():
    # Pick Mission Type
    PickType = MissionType[DiceRole(diceType=6,diceNum=1)-1]
    MissionOptions = Missions[PickType]

    # Select a specific mission
    rollTheDice = DiceRole(diceType=20,diceNum=1)
    selectCnt = 0
    while selectCnt < 21:
        if rollTheDice <= MissionOptions[selectCnt]:
            PickMission = MissionOptions[selectCnt+1]
            break
        else:
            selectCnt += 2
    return PickMission,PickType


def WriteToFile(PickMission,PickType):        
    if PickMission == 'Standard Mission':
        saveFile.write('Mission Type: ' + PickType + '\n')
        saveFile.write('Location: ' + Location[DiceRole(12,1)-1] + '\n')

        selectCnt = 0
        rollTheDice = DiceRole(diceType=6,diceNum=2)
        while selectCnt < 13:
            if rollTheDice <= Opposition[selectCnt]:
                PickOpposition = Opposition[selectCnt+1]
                break
            else:
                selectCnt += 2
        
        saveFile.write('Opposition: ' + PickOpposition + '\n')
    else:    
        # Output Result    
        saveFile.write('Mission Type: ' + PickType + '\n')
        saveFile.write("Selected Mission: " + PickMission + '\n')

# Generate output file with adventures.
saveFile = open('NE_Adventures.txt','w')
saveFile.write("Necessary Evil\n")
saveFile.write("Random Adventure Generator\n\n")

for i in range(1,11):
    saveFile.write("Adventure: " + str(i) + '\n')

    PickMission,PickType = GenerateMission()
    while SearchList(Completed_Missions,PickMission):
        PickMission,PickType = GenerateMission()
        
    if PickMission != 'Standard Mission':
        Completed_Missions.append(PickMission)

    WriteToFile(PickMission,PickType)
    saveFile.write('\n')

print('Done')
print(Completed_Missions)
saveFile.close()

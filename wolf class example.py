from random import randint

# these variables are modifiable for whatever you like haha
maplimit = 40
areaForEachWolf = 9

while True:
    try:
        mapsize = int(input("Map size: "))
        break
    except ValueError:
        print("Error | Invalid input.")

if mapsize > maplimit:
    mapsize = maplimit
    print(f"{maplimit} limit (edit code if required to adjust).")

Map = []                          # \
for x in range(mapsize):           # \
    text = ""                       # \
    if x == 0 or x == mapsize - 1:   # build base and top
        text = []                     # \
        for x in range(mapsize):       # \
            text.append('*')            # | define and visualise area
    else:                              # /
        text = ['*']                  # build lines in between
        for x in range(mapsize - 2): # /
            text.append(' ')        # /
        text.append('*')           # /
    Map.append(text)              # /

class NewWolf: 
    def __init__(self):
        self.lowerbound, self.upperbound = mapsize - mapsize + 1, mapsize - 2 # edge limits
        self.x = randint(self.lowerbound, self.upperbound) # generate random pos
        self.y = randint(self.lowerbound, self.upperbound) # generate random pos
        Map[self.y][self.x] = 'W' # 'W' represents wolf

    def getPos(self):
        return (self.x, self.y)

    def changePos(self, x, y):
        if isCoordDuplicate(self.getPos()):
            pass # leave 'W' on map because duplicate coord
        else:
            Map[self.y][self.x] = ' ' # remove 'W' from map
        self.x = x
        self.y = y
        Map[self.y][self.x] = 'W' # newpos

    def randmove(self):        
        working = True
        while working:
            option = randint(1, 4) # select a random direction
            if option == 1:
                if self.x + 1 > self.upperbound: # prevent edge breach
                    continue
                else:
                    self.changePos(self.x + 1, self.y) # move 1 in random direction
                    working = False
            elif option == 2:
                if self.x - 1 < self.lowerbound: # prevent edge breach
                    continue
                else:
                    self.changePos(self.x - 1, self.y) # move 1 in random direction
                    working = False
            elif option == 3:
                if self.y + 1 > self.upperbound: # prevent edge breach
                    continue
                else:
                    self.changePos(self.x, self.y + 1) # move 1 in random direction
                    working = False
            else:
                if self.y - 1 < self.lowerbound: # prevent edge breach
                    continue
                else:
                    self.changePos(self.x, self.y - 1) # move 1 in random direction
                    working = False

def isCoordDuplicate(selfwolf):  # \
    data = {}                     # \
    for wolf in wolves:            # \
        if wolf.getPos() in data:   # analyse coords
            data[wolf.getPos()] += 1 # \
        else:                         # | check for duplicate wolves in coords
            data[wolf.getPos()] = 1  # /
    if data[selfwolf] > 1:          # analyse if parsed coord is shared
        return True                # /
    else:                         # /
        return False             # /

def printMap():
    for x in range(mapsize): # print each line of the map
        line = ""
        for y in range(mapsize): # get each character of the line
            line += Map[x][y]
        print(line)

wolfDensity = int((mapsize - 2) * (mapsize - 2) / areaForEachWolf)
wolves = []
for x in range(wolfDensity): # generate number of wolves based on desired density
     wolves.append(NewWolf())
    
dupsum = 0
for wolf in wolves: # count duplicate coords
    if isCoordDuplicate(wolf.getPos()):
        dupsum += 1

printMap()
print(f"{len(wolves)} wolves.")
print(f"{dupsum} share a coord with at least one other wolf.")

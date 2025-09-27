class Driver:
    def __init__(self,name,team):
        self.name = name
        self.team = team
        self.points = 0
        self.positionAmount = [0]*20
        self.wins = 0
        self.podiums = 0
        self.poles = 0
        self.fastestLaps = 0
        self.raceStarts = 0
        self.raceFinishes = 0
        self.dnf = 0
        self.dsq = 0
    def updateStats(self,pos,points,isPole,isFastest):
        self.points += points
        self.poles += isPole
        self.fastestLaps += isFastest
        self.raceStarts += 1
        if pos == 'DNF':
            self.dnf += 1
        elif pos == 'DSQ':
            self.dsq += 1
        elif pos != 'DNS':
            self.positionAmount[pos-1] += 1
            self.wins += (pos == 1)
            self.podiums += (pos <= 3)
            self.raceFinishes += (pos != 21)
    def addStats(self,driver):
        self.points += driver.points
        for i in range(len(self.positionAmount)):
            self.positionAmount[i] += driver.positionAmount[i]
        self.wins += driver.points
        self.podiums += driver.podiums
        self.poles += driver.poles
        self.fastestLaps += driver.fastestLaps
        self.raceStarts += driver.raceStarts
        self.raceFinishes += driver.raceFinishes
        self.dnf += driver.dnf
        self.dsq += driver.dsq
    def reset(self):
        self.points = 0
        self.positionAmount = [0]*20
        self.wins = 0
        self.podiums = 0
        self.poles = 0
        self.fastestLaps = 0
        self.raceStarts = 0
        self.raceFinishes = 0
        self.dnf = 0
        self.dsq = 0
    def __repr__(self):
        return self.name
    def __str__(self):
        return f'{self.name} | Points: {self.points}'
    def __eq__(self, d):
        if d == None:
            return False
        return (d.name == self.name)*(d.team == self.team)
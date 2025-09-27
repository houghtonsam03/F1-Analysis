class Team:
    def __init__(self,name):
        self.name = name
        self.drivers = []
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
    def addDriver(self,driver):
        self.drivers.append(driver)
    def updateStats(self):
        for driver in self.drivers:
            self.points += driver.points
            self.wins += driver.wins
            self.podiums += driver.podiums
            self.poles += driver.poles
            self.fastestLaps += driver.fastestLaps
            self.raceStarts += driver.raceStarts
            self.raceFinishes += driver.raceFinishes
            self.dnf += driver.dnf
            self.dsq += driver.dsq
            for i in range(len(self.positionAmount)):
                self.positionAmount[i] += driver.positionAmount[i]
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
        if isinstance(d,Team):
            return d.name == self.name
        elif isinstance(d,str):
            return d == self.name
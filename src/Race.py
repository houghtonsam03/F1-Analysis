class Race:
    def __init__(self,name):
        self.name = name
        self.raceResults = {}
        self.sprintResults = {}
        self.pole = None
        self.fastest = None
    def addRaceResult(self,driver,racePosition):
        key = driver.name+driver.team
        self.raceResults[key] = {
            'Driver':driver,
            'Position':racePosition
        }
    def addSprintResult(self,driver,racePosition):
        key = driver.name+driver.team
        self.sprintResults[key] = {
            'Driver':driver,
            'Position':racePosition
        }
    def setFastest(self,driver):
        self.fastest = driver
    def setPole(self,driver):
        self.pole = driver
    def updateStats(self,driver,year):
        key = driver.name + driver.team
        RACEPOINTS = [25,18,15,12,10,8,6,4,2,1]
        SPRINTPOINTS = [8,7,6,5,4,3,2,1]
        racePos = 'DNS'
        totalPoints = 0
        isPole = (self.pole == driver)
        isFastest = (self.fastest == driver)
        if self.sprintResults:
            sprintPos = self.sprintResults.get(key)['Position']
            if sprintPos == 'DNF':
                driver.updateStats('DNF',0,False,False)
            elif sprintPos != 'DNS':
                sprintPos = int(sprintPos)
                if sprintPos <= 8:
                    totalPoints += SPRINTPOINTS[sprintPos-1]
        if self.raceResults:
            racePos = self.raceResults.get(key)['Position']
            if racePos == 'DNF':
                driver.updateStats('DNF',0,isPole,isFastest)
            elif racePos == 'DSQ':
                driver.updateStats('DSQ',0,isPole,isFastest)
            elif racePos != 'DNS':
                racePos = int(racePos)
                if racePos <= 10:
                    totalPoints += RACEPOINTS[racePos-1]
                    totalPoints += isFastest * ((2019 <= year <= 2024) or (1950 <= year <= 1959))
        driver.updateStats(racePos,totalPoints,isPole,isFastest)
    def getDriver(self,driver):
        if self.raceResults:
            return self.raceResults[driver.name+driver.team]['Driver']
        if self.sprintResults:
            return self.sprintResults[driver.name+driver.team]['Driver']
    def getDrivers(self):
        drivers = []
        if self.raceResults:
            for driverDict in self.raceResults.values():
                driver = driverDict['Driver']
                position = driverDict['Position']
                if position != 'DNS' and driver not in drivers:
                    drivers.append(driver)
        if self.sprintResults:
            for driverDict in self.sprintResults.values():
                driver = driverDict['Driver']
                position = driverDict['Position']
                if position != 'DNS' and driver not in drivers:
                    drivers.append(driver)
        return drivers
    def hasDriver(self,driver):
        drove = False
        if self.raceResults:
            if self.raceResults[driver.name+driver.team]['Position'] != 'DNS':
                drove = True
        if self.sprintResults:
            if self.sprintResults[driver.name+driver.team]['Position'] != 'DSN':
                drove = True
        return drove
        
    def hasResults(self):
        for (driverKey,driverDict) in self.raceResults.items():
            if driverDict['Position'] != 'DNS':
                return True
        return False
    def __eq__(self, value):
        return value == self.name
    def __repr__(self):
        return self.name
    def __str__(self):
        s =  "| " + self.name
        if self.pole:
            s += " | Pole: " + self.pole.name
        if self.fastest:
            s += " | Fastest: " + self.fastest.name + " |\n"
        for driver in self.raceResults.values():
            s += driver['Driver'].name + " > " + driver['Position'] + "\n"
        return s
    
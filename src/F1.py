import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from Driver import Driver
from Race import Race
from Team import Team
def findRace(raceName,races):
    if raceName == 'First':
        return races[0]
    if raceName == 'Last':
        foundRace = races[0]
        for i in range(1,len(races)):
            if races[i].hasResults():
                foundRace = races[i]
        return foundRace
    for race in races:
        if race == raceName:
            return race
def findTeam(teamName,teams):
    for team in teams:
        if team == teamName:
            return team
def initialise():
    teamNames = raceData.Team.tolist()
    driverNames = raceData.Driver.tolist()
    #Initialise Driver[] drivers
    drivers = []
    for i in range(len(driverNames)):
        drivers.append(Driver(driverNames[i],teamNames[i]))
    #Initialise Race[] races
    races = []
    races.append(Race(''))
    for col in raceData.columns:
        if col.endswith(' Race'):
            race = Race(col.replace(' Race',''))
            races.append(race)
    readData(drivers,races)
    return drivers,races
def readData(drivers,races):
    for col in raceData.columns:
        data = raceData[col]
        if col.endswith(' Race'):
            race = findRace(col.replace(' Race',''),races)
            for i in data.index:
                if isinstance(data[i],str):
                    position = data[i]
                elif isinstance(data[i],np.float64) and pd.notna(data[i]):
                    position = str(data[i].astype(int))
                else:
                    position = 'DNS'
                race.addRaceResult(drivers[i],position)
        if col.endswith(' Sprint'):
            race = findRace(col.replace(' Sprint',''),races)
            for i in data.index:
                if isinstance(data[i],str):
                    position = data[i]
                elif isinstance(data[i],np.float64) and pd.notna(data[i]):
                    position = str(data[i].astype(int))
                else:
                    position = 'DNS'
                race.addSprintResult(drivers[i],position)
        if col.endswith(' Pole'):
            race = findRace(col.replace(' Pole',''),races)
            for i in data.index:
                if data[i] == 1:
                    race.setPole(drivers[i])
                    break
        if col.endswith(' Fastest'):
            race = findRace(col.replace(' Fastest',''),races)
            for i in data.index:
                if data[i] == 1:
                    race.setFastest(drivers[i])
                    break
def sumToRace(drivers,raceName):
    raceNumber = races.index(raceName)+1
    for i in range(raceNumber):
        race = races[i]
        for driver in drivers:
            race.updateStats(driver,year)
    return drivers
def sortDrivers(data):
    sorted_data = dict(sorted(data.items(), key=lambda item: (
        -sum(d.points for d in item[1]['Drivers']),
        -sum(d.positionAmount[0] for d in item[1]['Drivers']),
        -sum(d.positionAmount[1] for d in item[1]['Drivers']),
        -sum(d.positionAmount[2] for d in item[1]['Drivers']),
        -sum(d.positionAmount[3] for d in item[1]['Drivers']),
        -sum(d.positionAmount[4] for d in item[1]['Drivers']),
        -sum(d.positionAmount[5] for d in item[1]['Drivers']),
        -sum(d.positionAmount[6] for d in item[1]['Drivers']),
        -sum(d.positionAmount[7] for d in item[1]['Drivers']),
        -sum(d.positionAmount[8] for d in item[1]['Drivers']),
        -sum(d.positionAmount[9] for d in item[1]['Drivers']),
        -sum(d.positionAmount[10] for d in item[1]['Drivers']),
        -sum(d.positionAmount[11] for d in item[1]['Drivers']),
        -sum(d.positionAmount[12] for d in item[1]['Drivers']),
        -sum(d.positionAmount[13] for d in item[1]['Drivers']),
        -sum(d.positionAmount[14] for d in item[1]['Drivers']),
        -sum(d.positionAmount[15] for d in item[1]['Drivers']),
        -sum(d.positionAmount[16] for d in item[1]['Drivers']),
        -sum(d.positionAmount[17] for d in item[1]['Drivers']),
        -sum(d.positionAmount[18] for d in item[1]['Drivers']),
        -sum(d.positionAmount[19] for d in item[1]['Drivers']),
    )))
    return sorted_data
def resetDrivers(dr):
    for driver in dr:
        driver.reset()
def getRaceNames(startIndex,endIndex):
    raceNames = []
    for i in range(startIndex,endIndex):
        race = races[i]
        raceNames.append(race.name)
    return raceNames
def combineTeams(teams):
    for team in teams:
        team.updateStats()
    return teams
def combineDrivers(drivers):
    combined = {}
    for driver in drivers:
        if driver.name not in combined.keys():
            combined[driver.name] = Driver(driver.name,driver.team)
        combined[driver.name].addStats(driver)
    combinedList = list(combined.values())
    return combinedList
def correctTeams(drivers,races):
    for driver in drivers:
        for race in races:
            if race.hasDriver(driver):
                driver.team = race.getDriver(driver).team
        print(driver)
        print(driver.team)
def createTeams(drivers):
    teams = []
    for driver in drivers:
        if driver.team not in teams:
            team = Team(driver.team)
            teams.append(team)
        else:
            team = findTeam(driver.team,teams)
        team.addDriver(driver)
    for team in teams:
        team.updateStats()
    return teams
def driverPosition(driverName,data):
    sorted_driver_names = list(data.keys())
    return sorted_driver_names.index(driverName) + 1 
def driverProgression(drivers,startRace,endRace):
    TEAM_COLORS_MAP = {
    'Red Bull Racing': '#0600EF', # Dark Blue
    'Mercedes': '#00D2BE',        # Teal/Silver
    'Ferrari': '#DC0000',         # Red
    'McLaren': '#FF8700',         # Papaya Orange
    'Aston Martin': '#006F62',    # British Racing Green
    'Alpine Renault': '#0090FF',          # Blue
    'Williams': '#005AFF',        # Dark Blue/White
    'RB': '#6692FF',              # Light Blue (for Visa Cash App RB)
    'Kick Sauber': '#52E252',     # Green (for Stake F1 Team Kick Sauber)
    'Haas': '#FFFFFF',            # White (Haas's main color, might need black lines/text for contrast)
    'Alfa Romeo': '#900000',      # Dark Red (for Alfa Romeo)
    'AlphaTauri': '#6692FF',      # Light Blue (for AlphaTauri)
}
    plot_data = {}
    startRace = findRace(startRace,races)
    endRace = findRace(endRace,races)
    startIndex = races.index(startRace)
    endIndex = races.index(endRace)+1

    for i in range(startIndex,endIndex):
        race = races[i]
        resetDrivers(drivers) # Removing all stats from all drivers
        sumToRace(drivers,race) # Summing the stats of all drivers up to race
        for driver in drivers:
            driverName = driver.name
            teamName = driver.team
            points = driver.points
            if driverName not in plot_data.keys():
                    plot_data[driverName] = {}
                    plot_data[driverName]['Points'] = [0]*(endIndex-startIndex)
                    plot_data[driverName]['Drivers'] = []
            plot_data[driverName]['Points'][i] += points
            plot_data[driverName]['Drivers'].append(driver)
            if race.hasDriver(driver):
                plot_data[driverName]['Team'] = teamName

    raceNames = getRaceNames(startIndex,endIndex) # Getting the raceNames for the x-axis

    plot_data = sortDrivers(plot_data) # Sorting the drivers based on F1-Sorting
    plt.figure()
    for (driverName,driverDict) in plot_data.items():
        teamName = driverDict['Team']
        pointList = driverDict['Points']
        lineColor = TEAM_COLORS_MAP.get(teamName)
        if lineColor == '#FFFFFF':
            lineColor = '#000000'
        label = driverName + ' > ' + str(pointList[-1]) + ' (+' + str(pointList[-1]-pointList[-2]) + ')'
        plt.plot(raceNames,pointList,label=label,marker='s',markeredgecolor='black',markerfacecolor=TEAM_COLORS_MAP.get(teamName),color=lineColor)
    plt.title(str(year)+ ' F1 Drivers Championship')
    plt.xlabel('Race')
    plt.ylabel('Points')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True,linestyle='--',alpha=0.7)
    plt.legend(bbox_to_anchor=(1.05,1),loc='upper left')
    plt.tight_layout()
    plt.get_current_fig_manager().window.wm_state('zoomed')
def teamProgression(drivers,startRace,endRace):
    TEAM_COLORS_MAP = {
    'Red Bull Racing': '#0600EF', # Dark Blue
    'Mercedes': '#00D2BE',        # Teal/Silver
    'Ferrari': '#DC0000',         # Red
    'McLaren': '#FF8700',         # Papaya Orange
    'Aston Martin': '#006F62',    # British Racing Green
    'Alpine Renault': '#0090FF',          # Blue
    'Williams': '#005AFF',        # Dark Blue/White
    'RB': '#6692FF',              # Light Blue (for Visa Cash App RB)
    'Kick Sauber': '#52E252',     # Green (for Stake F1 Team Kick Sauber)
    'Haas': '#FFFFFF',            # White (Haas's main color, might need black lines/text for contrast)
    'Alfa Romeo': '#900000',      # Dark Red (for Alfa Romeo)
    'AlphaTauri': '#6692FF',      # Light Blue (for AlphaTauri)
}
    plot_data = {}
    startRace = findRace(startRace,races)
    endRace = findRace(endRace,races)
    startIndex = races.index(startRace)
    endIndex = races.index(endRace)+1
    teams = createTeams(drivers) # Creating the teams based on the drivers

    for i in range(startIndex,endIndex):
        race = races[i]
        resetDrivers(drivers) # Removing all stats from all drivers
        resetDrivers(teams) # Removing all stats from all teams
        sumToRace(drivers,race.name) # Summing the stats of all drivers up to race
        combineTeams(teams) # Summing the stats of all teams up
        for team in teams:
            teamName = team.name
            points = team.points
            if teamName not in plot_data.keys():
                plot_data[teamName] = {}
                plot_data[teamName]['Points'] = [0]*(endIndex-startIndex)
                plot_data[teamName]['Drivers'] = [team]
            plot_data[teamName]['Points'][i] += points

    raceNames = getRaceNames(startIndex,endIndex)

    plot_data = sortDrivers(plot_data) # Sorting the teams based on F1-Sorting

    plt.figure()
    for (teamName,teamDict) in plot_data.items():
        pointList = teamDict['Points']
        lineColor = TEAM_COLORS_MAP.get(teamName)
        if lineColor == '#FFFFFF':
            lineColor = '#000000'
        label = teamName + ' > ' + str(pointList[-1]) + ' (+' + str(pointList[-1]-pointList[-2]) + ')'
        plt.plot(raceNames,pointList,label=label,marker='s',markeredgecolor='black',markerfacecolor=TEAM_COLORS_MAP.get(teamName),color=lineColor)
    plt.title(str(year)+ ' F1 Constructors Championship')
    plt.xlabel('Race')
    plt.ylabel('Points')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True,linestyle='--',alpha=0.7)
    plt.legend(bbox_to_anchor=(1.05,1),loc='upper left')
    plt.tight_layout()
    plt.get_current_fig_manager().window.wm_state('zoomed')
def showProgression(drivers,startRace,endRace):
    driverProgression(drivers,startRace,endRace)
    teamProgression(drivers,startRace,endRace)
def showStandings(drivers,startRace,endRace):
    driverStandings(drivers,startRace,endRace)
    teamStandings(drivers,startRace,endRace)
def driverStandings(drivers,startRace,endRace):
    startRace = findRace(startRace,races)
    endRace = findRace(endRace,races)
    startIndex = races.index(startRace)
    endIndex = races.index(endRace)+1

    race_data = {}
    text_table = []
    color_table = []
    column_headers = []
    for i in range(startIndex,endIndex):
        race = races[i]
        race_data[i] = {}
        resetDrivers(drivers)
        sumToRace(drivers,race)
        for driver in drivers:
            driverName = driver.name
            points = driver.points
            if driverName not in race_data.keys():
                race_data[i][driverName] = {}
                race_data[i][driverName]['Points'] = 0
                race_data[i][driverName]['Drivers'] = []
            race_data[i][driverName]['Points'] += points
            race_data[i][driverName]['Drivers'].append(driver)
        race_data[i] = sortDrivers(race_data[i]) # Sorting the drivers based on F1-Sorting
    
        column_headers.append(race.name)
        text_col = []
        color_col = []
        for (driverName,driverDict) in race_data[i].items(): # Get the first driver
            lastName = driverName.split(' ')[1][:6]  # Get the first 5 characters of the last name
            points = driverDict['Points']
            text = str(driverPosition(driverName,race_data[i])) + '. ' + lastName + ' > ' + str(points)
            if i > startIndex:
                standingsChange = driverPosition(driverName,race_data[i-1]) - driverPosition(driverName,race_data[i])
            else:
                standingsChange = 0
            if standingsChange == 0:
                color_col.append('white')
            elif standingsChange > 0:
                color_col.append('green')
                text += '\n(+' + str(standingsChange) + ')'
            else:
                color_col.append('red')
                text += '\n( -' + str(-standingsChange) + ')'
            text_col.append(text)
        text_table.append(text_col)  # Add the text column to the table
        color_table.append(color_col) # Add the color column to the table
    
    text_table = [list(x) for x in zip(*text_table)]  # Transpose the text table
    color_table = [list(x) for x in zip(*color_table)]  # Transpose the color table
    plt.figure()
    table_plot = plt.table(cellText=text_table,cellColours=color_table, colLabels=column_headers, cellLoc='center', loc='center')
    table_plot.auto_set_font_size(False)
    base_fontsize = 11
    font_Scale = max(1,(endIndex - startIndex) / 14)  # Scale font size
    table_plot.set_fontsize(base_fontsize/font_Scale)  # Adjust font size based on number
    table_plot.scale(1.0, 1.0)
    plt.axis('off')
    plt.xlabel('Race')
    plt.ylabel('Standings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.get_current_fig_manager().window.wm_state('zoomed')
def teamStandings(drivers,startRace,endRace):
    startRace = findRace(startRace,races)
    endRace = findRace(endRace,races)
    startIndex = races.index(startRace)
    endIndex = races.index(endRace)+1

    teams = createTeams(drivers) # Creating the teams based on the drivers

    race_data = {}
    text_table = []
    color_table = []
    column_headers = []
    for i in range(startIndex,endIndex):
        race = races[i]
        race_data[i] = {}
        resetDrivers(drivers)
        resetDrivers(teams)
        sumToRace(drivers,race)
        combineTeams(teams) # Summing the stats of all teams up
        for team in teams:
            teamName = team.name
            points = team.points
            if teamName not in race_data.keys():
                race_data[i][teamName] = {}
                race_data[i][teamName]['Points'] = 0
                race_data[i][teamName]['Drivers'] = []
            race_data[i][teamName]['Points'] += points
            race_data[i][teamName]['Drivers'].append(team)
        race_data[i] = sortDrivers(race_data[i]) # Sorting the drivers based on F1-Sorting

        column_headers.append(race.name)
        text_col = []
        color_col = []
        for (teamName,teamDict) in race_data[i].items(): # Get the first driver
            printNames = {'Red Bull Racing': 'RedBull',
                          'Mercedes': 'Merced',
                          'Ferrari': 'Ferrari',
                          'McLaren': 'McLaren',
                          'Aston Martin': 'Aston',
                          'Alpine Renault': 'Alpine',
                          'Williams': 'Williams',
                          'RB': 'RB',
                          'Kick Sauber': 'Sauber',
                          'Haas': 'Haas',
                          'Alfa Romeo': 'AlfaRom',
                          'AlphaTauri': 'AlpTau'}
            printName = printNames.get(teamName)
            points = teamDict['Points']
            text = str(driverPosition(teamName,race_data[i])) + '. ' + printName + ' > ' + str(points)
            standingsChange = 0
            if i > startIndex:
                standingsChange = driverPosition(teamName,race_data[i-1]) - driverPosition(teamName,race_data[i])
            if standingsChange == 0:
                color_col.append('white')
            elif standingsChange > 0:
                color_col.append('green')
                text += '\n(+' + str(standingsChange) + ')'
            else:
                color_col.append('red')
                text += '\n( -' + str(-standingsChange) + ')'
            text_col.append(text)
        text_table.append(text_col)  # Add the text column to the table
        color_table.append(color_col) # Add the color column to the table

    text_table = [list(x) for x in zip(*text_table)]  # Transpose the text table
    color_table = [list(x) for x in zip(*color_table)]  # Transpose the color table
    plt.figure()
    table_plot = plt.table(cellText=text_table,cellColours=color_table, colLabels=column_headers, cellLoc='center', loc='center')
    table_plot.auto_set_font_size(False)
    base_fontsize = 11
    font_Scale = max(1,(endIndex - startIndex) / 14)  # Scale font size
    table_plot.set_fontsize(base_fontsize/font_Scale)  # Adjust font size based on number
    table_plot.scale(1.0, 1.0)
    plt.axis('off')
    plt.xlabel('Race')
    plt.ylabel('Standings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.get_current_fig_manager().window.wm_state('zoomed')

if __name__ == "__main__":
    year = 2025 # Choose the year of interest.
    raceData = pd.read_csv("Data/"+str(year)+".csv") # Read the csv file
    drivers,races = initialise() # Create initial Driver[] without the information from csv and Race[] with the information from csv.
    showProgression(drivers,'First','Last')
    showStandings(drivers,'First','Last')
    plt.show()



    
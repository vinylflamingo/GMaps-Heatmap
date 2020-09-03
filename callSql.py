import pyodbc
import csv


def openConnection(city):
    if city == "New_Orleans":
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'              ### Server info has been remitted
                              'UID=;'                   ### for GitHub Public Repo. 
                              'PWD=;'
                              'Trusted_Connection=no;')
        return conn
    else:
        pass

def callServerAll(city):
    conn = openConnection(city)
    cursor = conn.cursor()
    allIncidents = cursor.execute(""" SELECT incidentLocation, incidentDate from ALARM_RESPONSES """)
    allIncidents = allIncidents.fetchall()
    cursor.close()
    conn.close()
    with open(f'datasets\\all_{city}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in allIncidents:
            writer.writerow(row)
        csvfile.close()

def callServerLastYear(city):
    conn = openConnection(city)
    cursor = conn.cursor()
    lastYearIncidents = cursor.execute(""" SELECT incidentLocation, incidentDate from ALARM_RESPONSES where incidentDate > DATEADD(year,-1,GETDATE())""")
    lastYearIncidents = lastYearIncidents.fetchall()
    cursor.close()
    conn.close()
    with open(f'datasets\\lastYear_{city}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in lastYearIncidents:
            writer.writerow(row)
        csvfile.close()

def callServerLastSixMonths(city):
    conn = openConnection(city)
    cursor = conn.cursor()
    lastSixMonthsIncidents = cursor.execute(""" SELECT incidentLocation, incidentDate from ALARM_RESPONSES where incidentDate > DATEADD(m, -6,GETDATE())""")
    lastSixMonthsIncidents = lastSixMonthsIncidents.fetchall()
    cursor.close()
    conn.close()
    with open(f'datasets\\lastSixMonths_{city}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in lastSixMonthsIncidents:
            writer.writerow(row)
        csvfile.close()

def callServerLastWeek(city):
    conn = openConnection(city)
    cursor = conn.cursor()
    lastWeekIncidents = cursor.execute(""" SELECT incidentLocation, incidentDate from ALARM_RESPONSES where incidentDate > DATEADD(DD, -7,GETDATE())""")
    lastWeekIncidents = lastWeekIncidents.fetchall()
    cursor.close()
    conn.close()
    with open(f'datasets\\lastWeek_{city}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in lastWeekIncidents:
            writer.writerow(row)
        csvfile.close()

def callServerLastTwentyFour(city):
    conn = openConnection(city)
    cursor = conn.cursor()
    lastTwentyFourHoursIncidents = cursor.execute(""" SELECT incidentLocation, incidentDate from ALARM_RESPONSES where incidentDate > DATEADD(DD, -1,GETDATE())""")
    lastTwentyFourHoursIncidents = lastTwentyFourHoursIncidents.fetchall()
    cursor.close()
    conn.close()
    with open(f'datasets\\lastTwentyFour_{city}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in lastTwentyFourHoursIncidents:
            writer.writerow(row)
        csvfile.close()

def refreshData(city):
    print(city)
    callServerAll(city)
    callServerLastYear(city)
    callServerLastSixMonths(city)
    callServerLastWeek(city)
    callServerLastTwentyFour(city)

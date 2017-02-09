import csv




with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/pdx_crime_data/data/crime_incident_data_2011.csv', 'r') as taco:
    data = csv.reader(taco)

    crime_stats = dict()
    for row in data:
        crime, date = row[3], row[1]

        if crime in crime_stats:
            crime_stats[crime].append(date)
        else:
            crime_stats[crime] = list([date])

    result = {crime: len(date) for crime, date in crime_stats.items()}
    result.pop('Major Offense Type', 1)
    most_common = sorted(result.items(), key=lambda crime:crime[1], reverse=True)
    most_common_crime = most_common[0]
    rarest_crime = most_common[-1]
    total_crime = sum(result.values())
    print("In 2011 there were {} crimes the most common of which was {} while {} was the rarest.".format(total_crime, most_common_crime, rarest_crime))

with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/pdx_crime_data/data/crime_incident_data_2012.csv', 'r') as taco:
    data = csv.reader(taco)

    crime_stats = dict()
    for row in data:
        crime, date = row[3], row[1]

        if crime in crime_stats:
            crime_stats[crime].append(date)
        else:
            crime_stats[crime] = list([date])

    result = {crime: len(date) for crime, date in crime_stats.items()}
    result.pop('Major Offense Type', 1)
    most_common = sorted(result.items(), key=lambda crime:crime[1], reverse=True)
    most_common_crime = most_common[0]
    rarest_crime = most_common[-1]
    total_crime = sum(result.values())
    print("In 2012 there were {} crimes the most common of which was {} while {} was the rarest.".format(total_crime, most_common_crime, rarest_crime))

with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/pdx_crime_data/data/crime_incident_data_2013.csv', 'r') as taco:
    data = csv.reader(taco)

    crime_stats = dict()
    for row in data:
        crime, date = row[3], row[1]

        if crime in crime_stats:
            crime_stats[crime].append(date)
        else:
            crime_stats[crime] = list([date])

    result = {crime: len(date) for crime, date in crime_stats.items()}
    result.pop('Major Offense Type', 1)
    most_common = sorted(result.items(), key=lambda crime:crime[1], reverse=True)
    most_common_crime = most_common[0]
    rarest_crime = most_common[-1]
    total_crime = sum(result.values())
    print("In 2013 there were {} crimes the most common of which was {} while {} was the rarest.".format(total_crime, most_common_crime, rarest_crime))

with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/pdx_crime_data/data/crime_incident_data_2014.csv', 'r') as taco:
    #data = csv.DictReader(taco)
    data = csv.reader(taco)

    crime_stats = dict()
    for row in data:
        crime, date = row[3], row[1]

        if crime in crime_stats:
            crime_stats[crime].append(date)
        else:
            crime_stats[crime] = list([date])

    result = {crime: len(date) for crime, date in crime_stats.items()}
    result.pop('Major Offense Type', 1)
    most_common = sorted(result.items(), key=lambda crime:crime[1], reverse=True)
    most_common_crime = most_common[0]
    rarest_crime = most_common[-1]
    total_crime = sum(result.values())
    #print(most_common)
    #print(total_crime)
    #print(most_common_crime)
    #print(rarest_crime)
    print("In 2014 there were {} crimes the most common of which was {} while {} was the rarest.".format(total_crime, most_common_crime, rarest_crime))

with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/pdx_crime_data/data/crime_incident_data_recent.csv', 'r') as taco:
    data = csv.reader(taco)

    crime_stats = dict()
    for row in data:
        crime, date = row[3], row[1]

        if crime in crime_stats:
            crime_stats[crime].append(date)
        else:
            crime_stats[crime] = list([date])

    result = {crime: len(date) for crime, date in crime_stats.items()}
    result.pop('Major Offense Type', 1)
    most_common = sorted(result.items(), key=lambda crime:crime[1], reverse=True)
    most_common_crime = most_common[0]
    rarest_crime = most_common[-1]
    total_crime = sum(result.values())
    print("Most recently there were {} crimes the most common of which was {} while {} was the rarest.".format(total_crime, most_common_crime, rarest_crime))

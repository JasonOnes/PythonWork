import datetime from datetime


with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/rain_data/sample.rain', 'r') as taco:
    rain = taco.read()
    scrubbed_rain = rain.split('\n')
    data = scrubbed_rain[9::]
    cols = data[0]
    data = data[2::]
    chopped_up = [d.split() for d in data]

#readline delete lines as needed
def helper(rain_measurement):
    try:
        return int(rain_measurement)
    except ValueError:
        return 0

rain_dict = {row[0]: list(map(helper, row[1::])) for row in chopped_up if row != []}
sorta_rainy = sorted(rain_dict.items(), key=lambda row:row[1], reverse=True)


#rain_dict = {row[0]: row[1::] for row in chopped_up if row != []}
#print(rain_dict)
#sorta_rainy = sorted(rain_dict.items(), key=lambda row:row[1], reverse=True)
max_rain_day = sorta_rainy[0]

#split key (ie date) into day month years
#combine all day totals for each years
#import datetime
#reformat dates
""" years = {2002:[],
            2003:[],
            2004:[],
            2005:[],
            2006:[],
            2007:[],
            2008:[],
            2009:[],
            2010:[],
            2011:[],
            2012:[],
            2013:[],
            2014:[],
            2015:[],
            2016:[]}

    years = {}
    for date, rain in sorta_rainy:
        year = date.split('-')[-1]

        if year in years:
            years[year].append(rain[0])
        else:
            years[year] = list([rain[0]])
    print(years)

    rain_totes = {date:sum(rain) for date, rain in years.items()}
    print(rain_totes)

    lotta_rain = sorted(rain_totes.items(), key=lambda year:year[1], reverse=True)

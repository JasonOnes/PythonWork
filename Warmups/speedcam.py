"""Find which vehicles are breaking the speed limit"""
from datetime import (datetime, timedelta)
from dateutil import parser


def get_data(file_name='speedcams_sm.txt'):
    try:
        with open(file_name, 'r') as file_to_read:
            text = file_to_read.read()
            #print(text)
            return text

    except FileNotFoundError:
        raise FileNotFoundError("Nope, no file by that name!")

def speeding():
    print("Vehicle {} broke the speed limit by {}.".format(plate, car_speed -
            speed_limit))



def speedy():
    data = get_data()
    data = data.replace('.', '')
    scrub_file = data.split("\n")
    print(scrub_file)
    speed_limit = scrub_file[0][15:20]
    distance_one = int(scrub_file[2][25:28])
    miles_one = distance_one * 0.000621371
    distance_two = int(scrub_file[3][25:28])
    miles_two = distance_two * 0.000621371
    distance_three = int(scrub_file[4][25:29])
    miles_three = distance_three * 0.000621371

    better_data = [line.split() for line in scrub_file[5::] if 'Start' not in line and line != '']

    cam_log = dict()
    for line in better_data:
        plate = line[1] + line[2]

        cam_num, vtime = line[5:8:2]
        vtime = parser.parse(vtime)
        vdata = (cam_num, vtime)


        if plate in cam_log.keys():
            cam_log[plate].append(vdata)
        else:
            cam_log[plate] = [vdata]

    #print(cam_log)

    for plate, vdata in cam_log.items():
        #vdata[n][1] = int
        for place, timestr in vdata:
            # import pdb; pdb.set_trace()
            dt = timestr
            x = vdata[1][1] - vdata[0][1]
            print(x)
            print(speed_limit)
            #print(plate, place, dt)
"""            if distance_one / (vdata[1][1] - vdata[0][1]) > speed_limit:
                car_speed = distance_one / (int(vdata[1][1]) - int(vdata[0][1]))
                speeding()
            elif distance_two / (int(vdata[2][1]) - int(vdata[1][1])) > speed_limit:
                car_speed = distance_two / (int(vdata[2][1]) - int(vdata[1][1]))
                speeding()
            elif distance_three / (int(vdata[3][1]) - int(vdata[2][1])) > speed_limit:
                car_speed = distance_three / (int(vdata[3][1]) - int(vdata[2][1]))
                speeding()
            else:
                print("Law abiding citizen!!")
"""

speedy()
    #
    #

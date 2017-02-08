""" program to find average time between two strings of time. REMEMBER base 60"""


def stop_time(x, y):
    scrub_time_x = x.split(":")
    scrub_time_y = y.split(":")
    scrux = (int(scrub_time_x[0]) * 60) + (int(scrub_time_x[1])) #+ (int(scrub_time_x[2] * 100))
    scruy = (int(scrub_time_y[0]) * 60) + (int(scrub_time_y[1])) #+ (int(scrub_time_y[2] * 100))
    average = (scrux + scruy) // 2

    minutes = average // 60
    seconds = (average % 60)
    miliseconds = seconds % 100

    time_out = str(minutes) + ":" + str(seconds) + ":" + str(miliseconds)
    print(time_out)


stop_time("01:33:45", "01:01:22")

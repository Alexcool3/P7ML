import math
# This python file contains all the functions for computing the necessary features.


# This function returns the total waiting time and number of times waited.
def waiting_info(x, z, time):
    """
    Parameters: x,z and time must each be a list and have the same size.
    Info: This function computes the Waiting Time, Number of Times waited, Waiting Time Percentage and Average Waiting Time.
    """
    start_time = 0
    total_time = 0
    count = 0
    found = False
    for i in range(len(x)-1):
        if not found:
            if x[i] == x[i+1] and z[i] == z[i+1]:
                found = True
                start_time = time[i]
        elif found:
            if x[i] != x[i+1] or z[i] != z[i+1] or i == len(x)-1:
                found = False
                count += 1
                total_time += time[i+1]-start_time
    #Total Waiting Time, Number of Times Waited, Waiting Time out of Total Play Time, Average Waiting Time.
    return [round(total_time, 2), count, round(total_time/max(time)*100, 2), round(total_time/count, 2)]


# This function returns the total distance between each data point.
def distance(x, z):
    """
    Parameters: x and z must each be a list and have the same size.
    Info: This function returns the total distance between each data point given as input.
    """
    dist = 0
    for i in range(len(x)-1):
        dist += math.sqrt(((x[i+1]-x[i])**2 + (z[i+1]-z[i])**2))
    return round(dist, 2)


# This function computes the instantaneous speed for each second.
def ispeed(x, z):
    """
    Parameters: x and z must each be a list and have the same size.
    Info: This function returns the minimum and maximum instantaneous speed in m/s.
    """
    tmp = []
    for i in range(math.floor(len(x)/10)+1):
        if i == int(len(x)/10):
            tmp.append(distance(x[i*10:i*10+len(x) % 10].values.tolist(), z[i*10:i*10+len(x) % 10].values.tolist()))
        else:
            tmp.append(distance(x[i*10:(i+1)*10].values.tolist(), z[i*10:(i+1)*10].values.tolist()))
    # Return Min Speed, Max Speed and Average Speed
    return [min(tmp), max(tmp)]


def average_speed(x, z, time):
    """
    Parameters: x,z and time must each be a list and have the same size.
    Info: This function returns the average speed in m/s.
    """
    # Return average speed.
    return round(distance(x, z) / max(time), 2)


def speed_info(x, z, time):
    """
    Parameters: x,z and time must each be a list and have the same size.
    Function: This function returns information regarding speed in terms of minimum, maximum and average speed in m/s.
    """
    tmp = ispeed(x, z)
    # Return Min Speed, Max Speed and Average Speed and Average Speed.
    return [tmp[0], tmp[1], average_speed(x, z, time)]


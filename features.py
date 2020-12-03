import math
# This python file contains all the functions for computing the necessary features.


# This function returns the total waiting time and number of times waited.
def waiting_info(x, z, time):
    start_time = 0
    count = 0
    total_time = 0
    found = False
    for i in range(len(x)-1):
        if i == 0:
            continue
        else:
            if not found:
                if x[i-1] == x[i] and z[i-1] == z[i]:
                    found = True
                    start_time = time[i-1]
            elif found:
                if x[i-1] != x[i] or z[i-1] != z[i] or i == len(x)-1:
                    found = False
                    count += 1
                    total_time += time[i]-start_time
    #Total Waiting Time, Number of Times Waited, Waiting Time out of Total Play Time, Average Waiting Time.
    return [round(total_time, 2), count, round(total_time/(len(time)/10), 2), round(total_time/count, 2)]


# This function returns the total distance between each data point.
def distance(x, z):
    dist = 0
    for i in range(len(x)-1):
        dist += math.sqrt((x[i+1]-x[i])**2 + (z[i+1]-z[i])**2)
    return dist


# This function computes the instantaneous speed for each second.
def ispeed(x, z, time):
    pass

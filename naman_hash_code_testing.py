import numpy as np

data=np.genfromtxt("a_example.in")
infos=data[0]
rows,cols,vehicles,rides,bonus,steps=infos[0],infos[1],infos[2],infos[3],infos[4],infos[5]
trajets=data[1]

"""
Returns the manhattan distance between two given points
"""
def distance_comput(a,b):
    return np.abs(a[0]-b[0])+np.abs(a[1]-b[1])

class Ride:
    def __init__(self, ride_info):
        self.start_point = (ride_info[0], ride_info[1])
        self.end_point = (ride_info[2], ride_info[3])
        self.earliest_start = ride_info[4]
        self.latest_finish = ride_info[5]

    def __str__(self):
        string = "Journey " + str(self.start_point) + " - " + str(self.end_point)
        string += " |  Between " + str(self.earliest_start) + " - " + str(self.latest_finish)
        return string 

print(data[0])
print(data[1:])

no_header_rides = data[1:]

for i in range(int(rides)):
    ride = Ride(no_header_rides[i])
    print(ride)

import numpy as np

data=np.genfromtxt("a_example.in")
infos=data[0]
rows,cols,vehicles,ride_count,bonus,steps=int(infos[0]), \
                                          int(infos[1]), \
                                          int(infos[2]), \
                                          int(infos[3]), \
                                          int(infos[4]), \
                                          int(infos[5])
trajets=data[1]

"""
Returns the manhattan distance between two given points
"""
def distance_comput(a,b):
    return np.abs(a[0]-b[0])+np.abs(a[1]-b[1])

class Ride:
    def __init__(self, ride_info, id):
        self.id = id
        self.start_point = (ride_info[0], ride_info[1])
        self.end_point = (ride_info[2], ride_info[3])
        self.earliest_start = ride_info[4]
        self.latest_finish = ride_info[5]

    def __str__(self):
        string = "Journey " + str(self.start_point) + " - " + str(self.end_point)
        string += " |  Between " + str(self.earliest_start) + " - " + str(self.latest_finish)
        string += " | ID " + str(self.id)
        return string 

print(data[0])
print(data[1:])

no_header_rides = data[1:]

rides = []

for i in range(ride_count):
    rides.append(Ride(no_header_rides[i], i))
    print(rides[i])

def earliest_start_key(ride):
    return ride.earliest_start

rides.sort(key=earliest_start_key)

for i in range(ride_count):
    print(rides[i])
    
class Vehicle():

    def __init__(self, id):
        self.id = id
        self.rides = []

    def add_ride(self, ride):
        self.rides.append(ride)

    def get_score_of_jounrey(self):
        time = 0
        pos = (0,0)
        score = 0
        
        for ride in self.rides:
            ride_score = 0
            
            #travel to start of the ride
            time += distance_comput(pos, ride.start_point)

            #wait until the earliest time to go 
            if (time <= ride.earliest_start):
                time = ride.earliest_start
                ride_score += bonus

            #travel the distance
            time += distance_comput(ride.start_point, ride.end_point)

            #if arrived on time
            if (time <= ride.latest_finish):
                ride_score += distance_comput(ride.start_point, ride.end_point)

            #if you have run out of time
            if (time > steps):
                break

            #otherwise update the score
            score += ride_score
            
            #set the final position after travelling
            pos = ride.end_point
    
        return score




import numpy as np
import pandas as pd


def reader(file):
    data = np.genfromtxt(file)
    infos = data[0]
    rows,cols,vehicles,rides,bonus,steps = infos[0],infos[1],infos[2],infos[3],infos[4],infos[5]
    return(data[1:],rows,cols,vehicles,rides,bonus,steps)

def distance_comput(a,b):
    return np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])

def score(start, finish, bonus):
    dist = distance_comput(start,finish)
    res = dist + bonus
    return res

def ride_info(ride):
    w,h = len(ride) ,5
    ride_dict = [[0 for x in range(h)] for y in range(w)]
    for i in np.arange(len(ride)):
        id = i
        ride_dict[i][0] = ride[i][0:2]
        ride_dict[i][1] = ride[i][2:4]
        ride_dict[i][2] = ride[i][4:5]
        ride_dict[i][3] = ride[i][5]
        ride_dict[i][4] = id
    return ride_dict



def greedy_approach (ride, bonus, steps, vehicles):
    vhicle_report = pd.DataFrame(columns =['id','ride','start','finish','score'])
    v = 0
    for s in range(0,int(steps)):
        if ride == []:
            break
        if v == int(vehicles):
            v = 0
        rdList = []
        idList = []
        Isbonus = False
        for r in ride:
            b = 0
            fin = 0
            if s == r[2]:
                Isbonus = True
            if Isbonus:
                b = bonus
                fin = v + 2
            else:
                b = 0
                fin = v + 3
            if fin <= r[3]:
                idList.append(r[4])
                rdList.append(score(r[0],r[1],b))
            else:
                rdList.append(0)
        ind = rdList.index(max(rdList))
        if Isbonus:
            fin = v + 1 + 1
        else:
            fin = v + 1 + 1 + 1
        vhicle_report = vhicle_report.append({'id':v,'ride': idList[ind], 'start': s,'finish': fin, 'score':rdList[ind]},ignore_index = True)
        ride.pop(ind)
        v +=1

    return vhicle_report




data = np.genfromtxt(r'C:\Users\USER\Desktop\GoogleHashCode\GoogleHashCode\Data\a_example.txt')
infos = data[0]
rows,cols,vehicles,rides,bonus,steps = infos[0],infos[1],infos[2],infos[3],infos[4],infos[5]
trajets = data[1:]
ride = ride_info(trajets)
report = greedy_approach (ride, bonus, steps, vehicles)
report



from collections import deque # double-ended queue
from numpy import random

import simpy
from simpy.util import start_delayed

# Hourly percentages of car traffic from national models
# Hourly rates begin with the midnight - 1:00 AM hour
#hourlyRates = [0.0081, 0.0052, 0.0047, 0.0057, 0.0099, 0.0230, 0.0489, 0.0679, 0.0629, 0.0531, 0.0509, 0.0538, 0.0560, 0.0574, 0.0635, 0.0733, 0.0804, 0.0775, 0.0579, 0.0437, 0.0338, 0.0280, 0.0205, 0.0138]

#Hourly rate from 8:00AM to 6:00PM
hourlyRates = [0.0629, 0.0531, 0.0509, 0.0538, 0.0560, 0.0574, 0.0635, 0.0733, 0.0804, 0.0775, 0.0579]

# From the Omaha Traffic Count PDF
# 67th & Pacific 31,938 8,752 13,514 18,594 23,016 09/17
# 50th & Underwood Ave 12,816 4,856 4,432 7,270 9,074
north = 8752//2
south = 13514//2
east = 18594//2
west = 23016//2

# Intersection Configuration
EW_Lanes = 4
NS_Lanes = 2

#Time lights are on
EW_Green = 60
NS_Green = 60
green_direction = "EW"
# Control Device can be a "Light" or "Sign"
# Stop signs cannot be used for intersections with more than 2 lanes
controlDevice = "Light"
departRate = 2 #how quickly can they go once it is their turn in seconds.
#Create an empty event log that will contain all the data for the simulation
eventLog = []
data_lib = []
#Output file
outFile = "output.csv"

#Useful Constants
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_DAY = SECONDS_PER_HOUR * 11

# Lists of cars in a row from the various directions. Only used if there is a line.
eastCars = []
westCars = []
northCars = []
southCars = []

carCount = 0
departCount = 0
signOrder = []

# Simulation for the traffic light. For simplicity, yellow is ignored.
def traffic_light(env):
    """
    Toggles the green direction between East-West to North-South.
    """
    global green_direction
    while True:
        green_direction = "EW"
        yield env.timeout(EW_Green)
        green_direction = "NS"
        yield env.timeout(NS_Green)

def arrive(env, dir):
    """
    This function will place a new car at the intersection.
    Cars arrive at an equal rate based on the national averages per hour.
    """
    global carCount
    arrivalRate = 0

    while True:
        carCount += 1
        hour = int(env.now // SECONDS_PER_HOUR)
        logInfo = (carCount, env.now, dir)
        #print(len(signOrder))
        if len(signOrder) < 4:
            #print("added", dir)
            try:
                signOrder.index(dir)
            except Exception as e:
                signOrder.append(dir)
        if dir == "N":
            northCars.append(logInfo)
            arrivalRate = int(SECONDS_PER_HOUR / (north * hourlyRates[hour])  + .5)
        if dir == "W":
            westCars.append(logInfo)
            arrivalRate = int(SECONDS_PER_HOUR / (west * hourlyRates[hour])  + .5)
        if dir == "S":
            southCars.append(logInfo)
            arrivalRate = int(SECONDS_PER_HOUR / (south * hourlyRates[hour]) + .5)
        if dir == "E":
            eastCars.append(logInfo)
            arrivalRate = int(SECONDS_PER_HOUR / (east * hourlyRates[hour]) + .5)



        # determine delay time until the next car by the current hour
        yield env.timeout(arrivalRate)

def departSign(env):
    """
    Function that determines who is going to depart the stop sign.
    """
    while True:
        #print(signOrder)
        if len(signOrder) == 0:
            pass
        else:
            carDir = signOrder.pop(0)

            if carDir == "N":
                car = northCars.pop(0)
                eventLog.append((car[0], car[1], env.now, car[2]))
                if len(northCars) > 0:
                    signOrder.append("N")
            if carDir == "W":
                car = westCars.pop(0)
                eventLog.append((car[0], car[1], env.now, car[2]))
                if len(westCars) > 0:
                    signOrder.append("W")
            if carDir == "S":
                car = southCars.pop(0)
                eventLog.append((car[0], car[1], env.now, car[2]))
                if len(southCars) > 0:
                    signOrder.append("S")
            if carDir == "E":
                car = eastCars.pop(0)
                eventLog.append((car[0], car[1], env.now, car[2]))
                if len(eastCars) > 0:
                    signOrder.append("E")

        yield env.timeout(departRate)


def departLight(env):
    """
    Function that determines who will depart from a stop light
    """
    while True:
        if green_direction == "EW":
            #deque the east and west cars if there are any in the queue
            for lane in range(EW_Lanes//2):
                if len(eastCars) > 0:
                    car = eastCars.pop(0)
                    eventLog.append((car[0], car[1], env.now, car[2]))
                if len(westCars) > 0:
                    car = westCars.pop(0)
                    eventLog.append((car[0], car[1], env.now, car[2]))

        elif green_direction == "NS":
            #deque the north and south cars if there are any in the queue
            for lane in range(NS_Lanes//2):
                if len(northCars) > 0:
                    car = northCars.pop(0)
                    eventLog.append((car[0], car[1], env.now, car[2]))
                if len(southCars) > 0:
                    car = southCars.pop(0)
                    eventLog.append((car[0], car[1], env.now, car[2]))

        yield env.timeout(departRate)

def get_parameters(int):

  conditions_file = open("conditions.csv", 'r')
  conditions = []

  for row in conditions_file:
    condition_att = row.split(',')

    condition = []
    condition.append(condition_att[0]) #EW_lanes
    condition.append(condition_att[1]) #NS_lanes
    condition.append(condition_att[2]) #Device
    condition.append(condition_att[3]) #EW_lanes
    condition.append(condition_att[4]) #NS_lanes
    condition.append(condition_att[5]) #Device
    condition.append(condition_att[6]) #Device
    condition.append(condition_att[7]) #EW_lanes
    condition.append(condition_att[8]) #NS_lanes
    condition.append(condition_att[9]) #Test_No
    conditions.append(condition)
  
  
  conditions_file.close()
  return conditions[int]
  #conditions_file.close()

  #for row in condition_file:
    #condition_attribute = row.split('/n')
    #print(row)
  #print(len(row))
    #condition = []
    #condition.append(condition_attribute[0]) #EW_lanes
    #condition.append(condition_attribute[1]) #NS_lanes
    #condition.append(condition_attribute[2]) #Device

def clean_data(testNo, eventLog):

  hour = 1
  car_per_hour = 0
  totalWait = 0

  for e in eventLog:
        carNum, arrival, departure, direction = e #unpack the tuple to multiple variables.
      
        #format wait time to minutes
        waitTime = format(float(departure - arrival)/60, '.2f')

    
        #format arrival time in minutes
        arrival_hour = format(float(arrival)/3600, '.2f')

        car_per_hour += 1
        totalWait = float(waitTime) + float(totalWait)



        if float(arrival_hour) >= float(hour):
          data_line = []  
          #print("Cars in hour " + str(hour) + " is " + str(car_per_hour) + "  -- resetting.")
          avg_Wait = format(float(totalWait)/float(car_per_hour), '.2f')


          #data_line has testNo, hour, cars in that hour, average wait in hour
          data_line.append(testNo)
          data_line.append(int(hour))
          data_line.append(int(car_per_hour))
          data_line.append(avg_Wait)
          data_lib.append(data_line)
          print(data_line)

          hour += 1
          car_per_hour = 0
          totalWAit = 0


    

def main():
  

  for test in range(1,24): #54
    global north, south, east, west, EW_Lanes, NS_Lanes, controlDevice

    parameters = get_parameters(test)
    north = int(parameters[2])//2
    south = int(parameters[3])//2
    east = int(parameters[4])//2
    west = int(parameters[5])//2
    EW_Lanes = int(parameters[6])
    NS_Lanes = int(parameters[7])
    controlDevice = parameters[8]
    testNo = int(parameters[9])
    print(north, south, east, west, EW_Lanes, NS_Lanes, controlDevice, testNo)


    env = simpy.Environment()
    env.process(arrive(env, "N"))
    env.process(arrive(env, "S"))
    env.process(arrive(env, "E"))
    env.process(arrive(env, "W"))
    if controlDevice == "Light":
        env.process(traffic_light(env))
        env.process(departLight(env))
    else:
        env.process(departSign(env))

    env.run(until=SECONDS_PER_DAY)

    print("Simulation complete")

    #print(eventLog)
    if testNo == 1:
      file = open(outFile, 'w')
      file.write("Test_No,Hour,Total_Cars,Average_Wait\n")
      file.close()

    clean_data(testNo, eventLog)
    test = test + 1
  
  print(data_lib)

  #for i in range(len(data_lib)):
    #for j in range(len(data_lib[i])):
  file = open(outFile, 'a')
  for e in data_lib:
        Test_No, Hour, Total_Cars, Average_Wait = e #unpack the tuple to multiple variables.
        file.write(str(Test_No) + "," + str(Hour) + "," + str(Total_Cars) + "," + str(Average_Wait) + "\n")
  
  file.close()

if __name__ == '__main__':
    main()

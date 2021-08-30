#This program was written to compile a list of intersections and road modifications I want to test.

def main():

  EW_lanes = []
  NS_lanes = []
  control_Device = []

  intersection = [
    ["38th and Leavenworth", 21570, 1752, 428, 20178, 20782],
    ["42nd and Leavenworth", 41000, 16854, 18710, 22712, 23724],
    ["fake street", 1, 2, 3, 4, 5],
    ]
  

  for EW in range(2, 7, 2):
    for NS in range(2, 7, 2):
      EW_lanes.append(EW)
      NS_lanes.append(NS)
    
  print(EW_lanes)
  print(len(EW_lanes))

  
  device = "light"
  for e in range(len(EW_lanes)+len(NS_lanes)):
    if device == "light":
      control_Device.append(device)
      device = "sign"
    elif device == "sign":
      control_Device.append(device)
      device = "light"
  
  print(control_Device)

  file = open("conditions.csv", 'w')
  file.write("Intersection,EADT,N,S,E,W,EW_lanes,NS_lanes,device,TestNo\n")


  l = 0 #lane counter
  d = 0 #device counter
  i = 0 #intersection counter
  i_att = 0 #intersection_attribute counter
  test = 1
  
  #Calculate length to determine number of possible test groups
  length = len(EW_lanes)*2*len(intersection)

  for e in range(length):
    print(e)
    file.write(str(intersection[i][0]) + "," + str(intersection[i][1]) + "," + str(intersection[i][2]) + "," + str(intersection[i][3]) + "," + str(intersection[i][4]) + "," + str(intersection[i][5]) + "," + str(EW_lanes[l]) + "," + str(NS_lanes[l]) + "," + control_Device[d]+ "," + str(test) + "\n")
    
    test = test + 1
    d = d + 1 #To change device
    if d%2 == 0: 
      l = l + 1 #To change lane #s
    if d == len(control_Device): #To start over with a new intersections
      d = 0 
      l = 0
      i = i + 1
     
  file.close()



if __name__ == '__main__':
    main()
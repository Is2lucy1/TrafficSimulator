def main():

  file = open("output.csv", 'r')  
  datalib = []

  for row in file:
    data_point = row.split(',')
    data = []
    data.append(int(data_point[2])//3600)
    data.append(data_point[4])
    datalib.append(data)
  
  
  
  file.close()



if __name__ == '__main__':
    main()
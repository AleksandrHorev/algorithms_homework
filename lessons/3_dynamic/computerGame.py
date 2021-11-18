# https://acmp.ru/index.asp?main=task&id_task=29

fileRead = open("/Users/aleksandr/Documents/Projects/algorithms_homework/3/INPUT.TXT", "r")
# fileRead = open("INPUT.TXT", "r")
count = int(fileRead.readline())
coordinatesString = fileRead.readline()
coordinates = [int(i) for i in coordinatesString.split()]
values = []
values[0] = abs(coordinates[1] - coordinates[0])
values[1] = min(abs(coordinates[1] - coordinates[0]), abs(coordinates[2] - coordinates[0] * 3))

for i in range(2,count):
  jump = abs(values[i-1] - coordinates[i])
  superJump = abs(values[i-2] - coordinates[i] * 3)
  values.append(min(jump, superJump))


fileWrite = open("/Users/aleksandr/Documents/Projects/algorithms_homework/3/OUTPUT.TXT", "w")
# fileWrite = open("OUTPUT.TXT", "w")
fileWrite.write(str(values(n-1)))
fileWrite.close()
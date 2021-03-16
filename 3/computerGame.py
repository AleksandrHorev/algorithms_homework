# https://acmp.ru/index.asp?main=task&id_task=29

fileRead = open("/Users/aleksandr/Documents/Projects/algorithms_homework/3/INPUT.TXT", "r")
# fileRead = open("INPUT.TXT", "r")
count = int(fileRead.readline())
coordinatesString = fileRead.readline()
coordinates = [int(i) for i in coordinatesString.split()]
result = 0
skip = False

for i in range(count-1):
  if (skip):
    skip = False
    continue
  jump = abs(coordinates[i + 1] - coordinates[i])
  if (i + 2 < count):
    superJump = abs(coordinates[i + 2] - coordinates[i]) * 3
  else:
    superJump = jump + 1

  if (superJump <= jump):
    result += superJump
 #   print(superJump)
    skip = True
  else:
 #   print(jump)
    result += jump

fileWrite = open("/Users/aleksandr/Documents/Projects/algorithms_homework/3/OUTPUT.TXT", "w")
# fileWrite = open("OUTPUT.TXT", "w")
fileWrite.write(str(result))
fileWrite.close()
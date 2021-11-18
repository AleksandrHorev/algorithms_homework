# https://acmp.ru/index.asp?main=task&id_task=29

fileRead = open("/Users/aleksandr/Documents/Projects/algorithms_homework/3/INPUT.TXT", "r")
# fileRead = open("INPUT.TXT", "r")
count = int(fileRead.readline())
numbersString = fileRead.readline()
numbers = [int(i) for i in numbersString.split()]
result = 1
tempResult = 1

for j in range(0, count - 1):
  last = numbers[j]
  for i in range(j,count - 1):
    if(numbers[i + 1] > last):
      tempResult += 1
      last = numbers[i + 1]
      print(last)

  if (tempResult > result):
    result = tempResult
  print('tempResult ' + str(tempResult))
  tempResult = 1

fileWrite = open("/Users/aleksandr/Documents/Projects/algorithms_homework/3/OUTPUT.TXT", "w")
# fileWrite = open("OUTPUT.TXT", "w")
fileWrite.write(str(result))
fileWrite.close()

import math
import csv

with open('class1.csv',newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)


def mean(data):
    n = len(data)
    total = 0
    for marks in data:
        total += float(marks[1])
    mean = total/n
    print(mean)
    return mean

mean = mean(file_data)
sqauredList = []
for number in file_data:
    a  = int(number[1])-mean
    a = a**2
    sqauredList.append(a)

sum = 0
for number in sqauredList:
    sum = sum+number

result = sum/(len(file_data)-1)

std_deviation = math.sqrt(result)
print (std_deviation)
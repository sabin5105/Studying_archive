from asyncore import read
import csv

file = open("./Chapter10/students.csv","w")
reader = csv.reader(file)

for data in reader:
    print(data)

file.close()


from numpy import genfromtxt
import numpy as np
import csv
data = genfromtxt('data_files/example.txt', delimiter=',', dtype=str)

#stroka stolbetz row/colimn
print(data[0][0])
print(len(data))



with open('data_files/example.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    for j in range(len(data[0])):
        str = []
        for i in range(len(data)):
            str.append(data[i][j])
        write.writerow(str)

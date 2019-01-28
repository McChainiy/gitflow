import csv
import xlrd

with open('rez.xlsx', 'r') as xlfile:
    reader = csv.reader(xlfile)
    print(list(reader))
import os
import csv

csv_loc = os.path.join("data", "info.csv")

with open(csv_loc, mode="r") as csvfile:
    csvreader = csv.reader(csvfile,newLine="")

    for row in csvreader:
        print(row)
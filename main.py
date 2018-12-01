import os
import csv
#hey this is a comment
csv_loc = os.path.join("data", "info.csv")
# hey this is a comment, remember to close this file!
with open(csv_loc, mode="r") as csvfile:
    csvreader = csv.reader(csvfile,newLine="")

    for row in csvreader:
        print(row)

import csv

def matching(IP_address):
    with open('inputDataForTraining.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if row[0] == IP_address:
                return index

    return false

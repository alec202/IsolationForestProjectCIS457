import csv
def is_ip_not_trusted(ip):
    with open('outputModelWithPredictions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        # return false if it's not trusted
        # return true if it is trusted
        return any(ip == row[0] and row[5] == "-1" for row in reader)

# Test the function
if __name__ == '__main__':
    print(is_ip_not_trusted('122.130.01.20'))
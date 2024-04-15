import pandas as pd
import csv
from random import randint
from is_ip_trusted import is_ip_not_trusted
from capcha_generator import generate_captcha
from isolation_forest_function import trainModelAndUpdateOuputFile, modify_data_at_indices

def user():
    previousCommand = " "
    address = input("Please enter your IP address\n")
    is_ip_already_stored = is_ip_in(address)
    if is_ip_already_stored:
        #get info from csv
        print("ip is in list")
    else:
        #ask user for info
        print("ip is not in list")
        location = input("Enter your country location\n").upper()
        vpn = input("Enter y/n if you have a VPN\n").lower()
        if vpn == 'y':
            # if they have a vpn, we will set vpn to an absurdly high value so they'll be detected
            vpn = 100
        else:
            vpn = 0
        num_clicks = 0
        df = pd.read_csv("inputDataForTraining.csv")
        newUserData = {
            'IP_Address': address,
            'Location': location,
            'numberOfTimesClickedAD': num_clicks,
            'Vpn': vpn
        }
        # Create new row
        new_row = pd.DataFrame([newUserData])
        # add the row to the existing data frame
        df = pd.concat([df, new_row], ignore_index=True)
        # Write to the csv file
        df.to_csv('inputDataForTraining.csv', index=False)

    index_ip_address_is_at = indexIpIsAt(address)
    """if the user has a vpn we need to increment their score by 100 
     so they become an outlier and will be displayed the captcha"""
    captchas_passed = 0
    while (1):
        print("\nPlease choose a command")
        command = input("View ad | Stay | Go back | Help\n")
        if (command == 'View ad'):
            if is_ip_already_stored:
                # returns true if the ip is not trusted
                ip_not_trusted = is_ip_not_trusted(address)
                # if ip is not trusted we display the captcha
                if ip_not_trusted:
                    # if they appear to be a bot and still wasting our resources, yet they
                    # passed our captcha more than 3 times, we should filter them out.
                    if captchas_passed >= 3:
                        print("This person is wasting our resources, won't display ad")
                        continue
                        #restart the loop
                    captcha_passed = generate_captcha()
                    # keep displaying a captcha until they successfully get one correct
                    while not captcha_passed():
                        print("\nCaptcha failed, try again\n")
                        captcha_passed = generate_captcha()
                    print("Captcha passed, view ad:\n")
                    #ad
                    pickAdd()
                else:
                    # If the IP was trusted, then we just display an ad like normal
                    pickAdd()
            else:
                # if we don't have any data on the IP then we should show them the AD.
                pickAdd()

            previousCommand = "v"
        elif (command == 'Stay'):
            #stay
            print("staying and interacting with the ad in a meaningful way")
            previousCommand = "s"
        elif (command == 'Go back'):
            #go back
            """Gotta use a functino to incrememnt the number of clicks
            for the correct corresponding scenario"""
            if (previousCommand == "v"):
                changeScore(address, -0.10)
            elif (previousCommand == "s"):
                changeScore(address, 0.10)
            print("going back")
            previousCommand = "b"
        elif (command == 'Help'):
            #help
            print("Command list: \nView ad: type 'view ad' to see an ad \nStay: type 'stay' to stay on the ad page \nGo back: type 'go back' to go back")
        is_ip_already_stored = True
        trainModelAndUpdateOuputFile()

def indexIpIsAt(address):
    with open('inputDataForTraining.csv', 'r') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if row[0] == address:
                return index

def is_ip_in(ip):
    with open('inputDataForTraining.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return any(ip == row[0] for row in reader)
        
def changeScore(ip, value: float):
    counter = 0
    df = pd.read_csv("outputModelWithPredictions.csv")
    with open('outputModelWithPredictions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if (ip == row[0]):
                break
            counter = counter + 1
    df.iloc[counter, 4] = df.iloc[counter, 4] + value
    df.to_csv("outputModelWithPredictions.csv", index=False)

def pickAdd():
    company_and_college_names = [
        "Grand Valley State University",
        "Best Buy",
        "KMART",
        "Meijer",
        "Walmart",
        "University of Michigan",
        "Michigan State University",
        "Apple",
        "Walmart",
        "Home Depot",
        "Etsy"
        "Marshalls",
        "Celebration Cinema"
    ]
    random_index = randint(0, (len(company_and_college_names) - 1))
    print(f"Displaying Ad from {company_and_college_names[random_index]}")


if __name__ == "__main__":
    print(indexIpIsAt("13.133.1.20"))
    user()
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

    trainModelAndUpdateOuputFile()
    index_ip_address_is_at = indexIpIsAt(address)
    """if the user has a vpn we need to increment their score by 100 
     so they become an outlier and will be displayed the captcha"""
    num_captchas_passed = 0
    previousCommand = None
    while (1):
        print("\nPlease choose a command")
        command = input("View ad | Stay | Go back | Help\n").lower()
        if (command == 'view ad' or command == 'view' or command == 'v'):
            # returns true if the ip is not trusted
            ip_not_trusted = is_ip_not_trusted(address)
            # if ip is not trusted we display the captcha
            if ip_not_trusted:
                # if they appear to be a bot and still wasting our resources, yet they
                # passed our captcha more than 3 times, we should filter them out.
                if num_captchas_passed >= 3:
                    print("This person is wasting our resources, won't display ad")
                    continue
                    #restart the loop
                captcha_passed = generate_captcha()
                # keep displaying a captcha until they successfully get one correct
                while not captcha_passed:
                    print("\nCaptcha failed, try again\n")
                    captcha_passed = generate_captcha()
                print("Captcha passed, view ad:\n")
                num_captchas_passed += 1
                #ad
                pickAdd()
            else:
                # DON'T REMOVE THIS ELSE
                # If the IP was trusted, then we just display an ad like normal.
                pickAdd()
            previousCommand = "v"
        elif ((command == 'stay' or command == 's') and previousCommand is not None and previousCommand == "v"):
            #stay
            print("staying and interacting with the ad in a meaningful way")
            previousCommand = "s"
        elif (command == 'go back' or command == 'back' or command == 'b'):
            #go back
            """Gotta use a functino to increment the number of clicks
            for the correct corresponding scenario"""
            if (previousCommand == "v"):
                modify_data_at_indices(index_ip_address_is_at - 1, 2, 1)
            print("going back")
            previousCommand = "b"
        elif (command == 'help' or command == 'h'):
            #help
            print("Command list: \nView ad: type 'view ad', 'view', or 'v' to see an ad \nStay: type 'stay' or 's' to interact with the ad page \nGo back: type 'go back', 'back', or 'b' to go back")
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
        "Etsy",
        "Marshalls",
        "Celebration Cinema"
    ]
    random_index = randint(0, (len(company_and_college_names) - 1))
    print(f"Displaying Ad from {company_and_college_names[random_index]}")


if __name__ == "__main__":
    #print(indexIpIsAt("13.133.1.20"))
    user()
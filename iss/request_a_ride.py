#!/usr/bin/python3

# Shebang always goes on top

# Imports
import requests

# Define URL
bezos_mobile = 'http://api.open-notify.org/astros.json'

def main():
    # Runtime code

    # Call webservice
    elon_dust = requests.get(bezos_mobile)


    # Translate json into python list and dictionaries
    ground_ctrl = elon_dust.json()

    # Print The Data
    print(ground_ctrl["number"])
    for ground_ctrl_dict in ground_ctrl["people"]:
       print( f'{ground_ctrl["name"]} is on the {ground_ctrl["craft"]}') 




if __name__ == "__main__":
        main()

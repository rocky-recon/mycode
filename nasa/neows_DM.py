#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    start_date = "start_date=2021-06-13"
    #user_Input_SD = str("Please enter the start date: " + start_date)
    end_date = "end_date=" + input(END_DATE)
    #user_Input_ED = str("Please enter the end date: " + end_date)
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"
    
    # make a request with the request library
    neowrequest = requests.get(NEOURL + start_date + end_date + "&" + end_date +  "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    closest = 99999999999999999999999999999999999999999999999999
    size= 0
    speed = 0
    hazardcount= 0


    ## display NASAs NEOW data
    print("Asteroid count: ", neodata["element_count"])
    for dates in neodata["near_earth_objects"]:
        for x in neodata["near_earth_objects"][dates]:
            astersize=float(x["estimated_diameter"]["kilometers"]["estimadeted_diamete    r_max"])
            asterspeed=float(x ["close_approach_data"][0]["relative_velocity"]["kilomet    ers_per_hour"])
            asterclosest=float( x["close_approach_data"][0]["miss_distance"]["kilometers"    ])
            if astersize > size:
                size = astersize
            if asterspeed > speed:
                speed = asterspeed
            if asterclosest >
            closes:
                closes = asterclosest
print(f'''
        Biggest: {size}
        Speediest: {speed}
        Closest: {closes}
        {hazardcount} is almost here''')
                    



if __name__ == "__main__":
    main()


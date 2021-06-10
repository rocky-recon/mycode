#!/usr/bin/env python3

# always add shebang on top of page

"""The puropose of this program is to display every NFL players data. By: Damian Mercado"""

# standard library first!
import random
#import os
#import shutil
import csv

# This will print every line in a csv file
#def print_csv(data):
#    for row in data:
#        print(', '.join(row))

# This will print a random row
#def print_random_row(data):
#    nfl_data = data.read().split()
#    nfl_player = random.choice(nfl_data)
#    print(nfl_player)

# This will print a random column
def print_random_column(data):
    csv_reader = csv.reader(data)
    nfl_player_data = list(csv_reader)
    random_question = random.choice(nfl_player_data)
    print(random_question)
   #nfl_data = data.read().split()

def print_random_player(data):
    csv_reader = csv.reader(data)
    random_nfl_player = list(csv_reader)
    random_nfl_player_question = random.choice(random_nfl_player)
    print(random_nfl_player_question)

""" User Story: 
    The purpose of this function is to pull a random college a nfl player went to.
    When I'm viewing NFL spreadsheet ..."""
# open csv file that I want to loop across
with open("nflalltime.txt", "r") as nfl_file:
    # The user will type in the function print_random_player
    while True:
        user_input = input('Enter a print_random_player to pull random nfl player information: ')
        if user_input in locals() and callable(locals()[user_input]):
            user_input = locals()[user_input]
            break
        else:
            print("Invalid name, please try again...")
    
    # print_random_player grabs csv.reader and random.choice in order to print a random row. 
    def print_random_player(data):
        csv_reader = csv.reader(data)
        random_nfl_player = list(csv_reader)
        random_nfl_player_question = random.choice(random_nfl_player)
        print(random_nfl_player_question)
    """I want to print a random row..."""
    print_random_column(nfl_file)


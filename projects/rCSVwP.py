#!/usr/bin/env python3

# always add shebang on top of page

"""The puropose of this program is to display every NFL players data. By: Damian Mercado"""

# standard library first!
import random
import os
import shutil
import csv


"""The purpose of this function is to pull a random college a nfl player went to."""

"""When I'm viewing NFL spreadsheet ..."""
# open csv file that I want to loop across
with open("nflalltime.txt", "r") as nfl_file:
    """I want to print a random row..."""
    row_list= csv.reader(nfl_file)
    rand_row= random.choice(row_list)
    print(rand_row)
     
      #create a counter for files names
      #nfl_data = 0
     
      # creating a row_list from csv reader in order to get
      #row_list= csv.reader(nfl_file)
      # a random row through rand_row
      #rand_row= random.choice(row_list)
      
      # loop across open file line by line
      #for row in csv.reader(nfl_file):
       #   print(row)
           
          # increase nfl_data by 1 (to create unique admin.rc file)
          #nfl_data = nfl_data +1
          #rand_row= random.choice(row_list)
          #player_data = rand_row
          #print(player_data)
          
          # this f string says "fill in the value of nfl_data"
          #player_data = f"admin.rc{nfl_data}"
 
          # open admin.rc file to print data
          #with open(player_data, "w") as player_file:
              #print("college=" + row[], file=player_file)
        #   print("export college=" + row[0], file=nfl_file)

    



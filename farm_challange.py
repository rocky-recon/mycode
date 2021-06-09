#!/usr/bin/env python3


# Old Macdonald had a farm. Farm. 
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Write a for loop that returns all the animals from the NE Farm!

#for s in farms:
 #   print(farms[1])
yuck= ["carrots","celery", "apples", "bananas", "oranges"]

num= input("""
        Choose a farm by number:
        0. NE Farm
        1. W Farm
        2. SE Farm
        >""")


for critters in farms[num].get("agriculture"):
    if critters not in yuck:
        print(critters)

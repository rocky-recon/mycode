#!/usr/bin/python3

# Always add shebang on top of page


# Standard library first!
from random import randint
import dice
import os

"""User Story 
    The User will select a room based on direction and collect items through a maze
 based of a house footprint.  
    The User will be able to select multiple items in each room to defend himself f
rom the evil Dependapotamus """

'''The User health is low from working in the military.'''

humans = [{'name' : 'Dependapotamus', 'health' : 100, 'damage' : '1d6'},
          {'name' : 'Child', 'health' : 10, 'damage' : '1d4'}]
weapons = [{'dog poop' : {'damage' : '1d12'}},
           {'ps4' : {'damage' : '1d5'}}, 
           {'xbox' : {'damage' : '1d5'}}]
spell_lookup = [{'skoal wintergreen dip' : {'armor' : '1d12'}},
          {'white muscle shirt' : {'armor' : '1d24'}},
          {'self-esteem' : {'armor' : '1d5'}}]
health = [{'monster energy drink' : {'health' : '1d4'}},
        {'taco bell' : {'health' : '1d4'}}]

player_health = 5
inventory = []
spellbook = []
health_reserves = []

''' The User will face CQC throughout the house. Combat is random'''
def _CQC():
    combatant_ID = randint(0 , 2)

    global player_health, inventory, weapons, humans
    round = 1
    combatant_health = humans[combatant_ID]['health']

    print(f"You\'re ferocious {humans[combatant_ID]['name']} approaches! COMBAT HAS BEGUN!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Monster Health: [" + str(combatant_health) + "]")

        print("Type: RUN, CAST [health_reserves], or USE [weapons]") # gotta write code for cast
        move = input().lower().split() # converts move into a lower-case list to deal with each item in list separately
        combatant_damage = sum(dice.roll(humans[combatant_ID]['damage']))
        print("\n=========================")


        if move[0] == 'use': #
            if move[1] in inventory: # checks if weapon is in your inventory
                player_damage = dice.roll(armory[move[1]]['damage'])
                print(f"You hit a {humans[combatant_ID]['name']} for {player_damage} damage!")
            if move[1] not in inventory:
                print(f"There is no {move[1]} in your inventory!")

        if move[0] == 'cast': #
            if move[1] in spellbook: # checks if spell is in your spellbook
                if move[1].lower() == 'Skoal Wintergreen dip':
                    player_damage = sum(dice.roll(spell_lookup[move[1]]['damage']))
                    print(f"Take the dip {humans[combatant_ID]['name']} for {player_damage} damage!")
            if move[1] not in spellbook:
                print(f"You don't know the {move[1]} !")

        if move[0] == 'run': #
            escape_chance= randint(1,10) #+ player_speed # if I set this variable later, here's where it would work

            if escape_chance >= 10:
                print("Someone has been doing PT!")
                break
            if escape_chance >= 5:
                print("You expose your back as you turn and flee- the Dependa takes advantage.")
                print(f"A {humans[combatant_ID]['name']} hits you for {combatant_damage} damage!")
                player_health -= int(combatant_damage)
                if player_health >= 1:
                    print("You managed to escape.")
                    break
                if player_health < 1:
                    print("You have been slain.")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The Dependa out-maneuvers you and attacks! You do not escape.")

        try:
            combatant_health -= int(player_damage)
        except:
            pass
        if combatant_health <= 0:
            print(f"The {humans[combatant_ID]['name']} lies dead. You are victorious!\n")
            break

        print(f"A {humans[combatant_ID]['name']} hits you for {combatant_damage} damage!")
        print ("=========================\n")
        round += 1
        player_health -= int(combatant_damage)

        if player_health <= 0:
            print("You have been vanquished! You have re-enlisted.")
            sys.exit()



def show_Instructions():
  #print a main menu and the commands
  print('''
Surviving Enlisted Housing
=======
Commands:
  go [north, east, south, west]
  get [item, spell]
''')


def player_status():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + current_Room)
    print('You can go ' + current_Directions)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print the current spellbook
    print('Spellbook : ' + str(spellbook))
    print('You\'re current health levels is ' + str(current_Health_Levels)) 
    print("---------------------------")


def show_Status():
    if 'desc' in rooms[current_Room]:
        print(rooms[current_Room]['desc'])
    if 'item' in rooms[current_Room]:
        print('You see a ' + rooms[current_Room]['item'] + '.')
    if 'spell' in rooms[current_Room]:
        print('You see you\'re helpful "' + rooms[current_Room]['spell'] + '".')
    print('========================================')    

def random_encounter():
    if((int(rooms[current_Room]['random_CQC'])) + 5) > 10:
        _CQC()
    
#an inventory, which is initially empty
#inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Lifted F-150 Diesel' : {
                  'south' : 'Road',
                  'west'  : 'Yard',
                  'item'  : 'skoal wintergreen dip',
                  'item_desc' : 'back pocket of jeans',
                  'desc' : 'You\'re Affliction shirt matches with your truck. You can go south to the road or west to your yard',
                  'random_CQC' : 0, 
                },

            'Road' : {
                #you won the game
                'desc' : 'You have won the game',
                },

            'Yard' : {
                'south' : 'Shed',
                'west' : 'House',
                'item' : 'dog poop',
                'item_desc' : 'The chihuahua strikes again',
                'desc' : 'There are toys on the ground. You can go south to the Shed or west to the House.',
                'random_CQC' : 30,
                },

            'Shed' : {
                'west' : 'Shed',
                'item' : 'chair',
                'item_desc' : 'The chair is only here for moral support',
                'desc' : 'The Shed has been here for years and offers moral support.',
                'random_CQC' : 0,
                },
            

            #figure out how to make Taco Bell and Monster hurt your health'''
            'House' : {
                'north' : 'Kitchen',
                'south' : 'Living Room',
                'west' : 'Hall',
                'desc' : 'You\'re house was built before WWII and the mold is older than your grand-father. You can go north to the Kitchen, south to the Living room, or west to the hall.',
                'random_CQC' : 60,
                },

            'Kitchen' : {
                  'south' : 'Living Room',
                  'north' : 'Door',
                  'item'  : 'monster energy drink',
                  'item_desc' : 'Monster Energy Drink gives energy but hurts your health',
                  'desc' : 'The fride door is open and somehow there is PB&J on the ceiling. You can go south to the Living Room or north through a Door',
                  'random_CQC' : 50,
                },


            'Living Room' : {
                  'west' : 'Hall',
                  'north': 'Kitchen',
                  'east' : 'Yard',
                  'item' : 'taco bell',
                  'item_desc' : 'Taco Bell attacks your gut!!!',
                  'desc' : 'Live, Love, Laugh is on the wall. You can go west to the Hall',
                  'random_CQC' : 40,
               },

            'Hall' : {
                  'west' : 'Office',
                  'south' : 'Bedroom',
                  'east' : 'Living Room',
                  'item' : 'monster energy drink',
                  'item_desc' : 'Monster Energy Drink gives energy and health',
                  'desc' : 'A dark valley that takes you to your Bedroom or the office.',
                  'random_CQC' : 0,
               },

            'Office' : {
                    'north' : 'Kitchen',
                    'item' : 'xbox',
                    'desc' : 'You have decided to hide and play COD',
                    },
            
            
            'Bedroom' : { 
                  'item' : 'ps4',
                  'item_desc' : 'Play video games to avoid responsibilities',
                  'desc' : 'The place you lost your soul',
                  'random_CQC' : 100,

           },
         }

# Start the player in a Lifted F-150 Diesel
current_Room = 'Lifted F-150 Diesel'

# Show directions user can go to
current_Directions = 'north, east, south, and west'

# Show current health levels
current_Health_Levels = player_health


show_Instructions()

# loop forever
while True:
    player_status()
    show_Status()

   # get the player's next 'move'
   # .split() breaks it up into an list array
   # eg typing 'go east' would give the list:
   # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    os.system('clear')
    # if they type 'go' first
    if move[0] == 'go':
      # check that they are allowed wherever they want to go
      if move[1] in rooms[current_Room]:
          # set the current room to the new room
          current_Room = rooms[current_Room][move[1]]
          if 'desc' in rooms[current_Room]:
              print(rooms[current_Room]['desc'])
          random_encounter()
         #there is no door (link) to the new room
          else:
              print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get' :
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[current_Room] and move[1] in rooms[current_Room]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[current_Room]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
      
    # Define how a player can win
    if current_Room == 'Road':
        print('You escaped Enlisted Housing!!! You have now traded your truck for a 2006 Mustang with a 28% APR!!')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[current_Room] and 'monster' in rooms[current_Room]['item']:
        print('A monster has got you... GAME OVER!')
        break

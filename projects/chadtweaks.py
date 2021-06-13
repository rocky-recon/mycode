#!/usr/bin/python3

# Always add shebang on top of page


# Standard library first!
from random import randint
import dice

"""User Story 
    The User will select a room based on direction and collect items through a maze
 based of a house footprint.  
    The User will be able to select multiple items in each room to defend himself f
rom the evil Dependapotamus """

def showInstructions():
  #print a main menu and the commands
  print('''
Escaping Dependapotamus
=======
Commands:
  go [direction]
  get [item]
''')

''' The User needs to defend himself with weapons and health from the humans. 
    The User health is low from working in the military.'''

humans = [{'name' : 'Dependapotamus', 'health' : 100, 'damage' : '1d6'},
          {'name' : 'Child', 'health' : 10, 'damage' : '1d4'}]
weapons = [{'dog poop' : {'damage' : '1d12'}},
           {'PS4' : {'damage' : '1d5'}}, 
           {'Xbox' : {'damage' : '1d5'}}]
health = [{'Skoal Wintergreen dip' : {'armor' : '1d12'}},
          {'Whitebeater' : {'armor' : '1d24'}}
          {'self-esteem' : {'armor' : '1d5'}}]
player_health = 5
inventory = []
health_reserves = []



def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Lifted F-150 Diesel' : {
                  'south' : 'Road',
                  'west'  : 'Yard',
                  'item'  : 'Skoal Wintergreen dip'
                  'item_desc' : 'back pocket of jeans'
                  'desc' : 'You have a great yard. It is green and enjoyable'
                  
                },

            'Road' : {
                #you won the game
                'desc' : 'You have won the game'
                },

            'Yard' : {
                'south' : 'Shed',
                'west' : 'House',
                'item' : 'hose', #['hose', 'dog poop', 'toys', 'self-esteem']
                'item_desc' : 'The hose is long and flexible but welded to the faucet'}

            'Shed' : {
                'west' : 'Shed',
                'item' : 'chair',
                'item_desc' : 'The chair is only here for moral support'
            
            'House' : {
                'north' : 'Kitchen'
                'south' : 'Living Room'

                }


            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Living Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Lifted F-150 Diesel'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

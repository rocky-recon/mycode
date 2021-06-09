#!/usr/bin/python3

print('What is your Purity Score?')

questions= ["Had a crush? ","Held someone\'s hand? ","Talked about Star Wars to someone you liked? ","Do you know the Princess Bride? ","Do you like Anime? ","Do you like animals? ","Do you know the CSS"]

ycount = 0

ncount = 0

for x in questions:
    print(x)
    userInput = input('Yes/No').lower()
   # while userInput != "yes" or userInput != "no": 
    if userInput == "yes":
        ycount += 1
    elif userInput == "no":
        ncount +=1 
    #    else:
     #       print("You must type yes or no")
      #      print(x)
       #     userInput = input('Yes/No').lower()

if ycount == 6:
    print("Non-purity Expert")

    
if ycount == 4:
    print("Purity levels are decreasing")

if ycount == 2:
    print("DANGER HIGH PURITY LEVELS")

if ycount == 0:
    print("Soooooooooooooooooo PPPPPPPPPPPPPPPPPPPPPUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEE")

if ncount == 5:
    print("Purity levels increasing")

if ncount == 3:
    print("Purity levels  decreasing")

if ncount == 1:
    print("DANGER LOW PURITY LEVELS")
    
        
    
    #for x in questions():
#    if questions == 6:
#        print("Non-purity Expert")
#elif questions > 3:
  # print("Purity levels are decreasing")
#    else:
#        print("Sooooooooooooooooooooooooooo PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEE")



       

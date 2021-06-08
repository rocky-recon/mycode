char_name = input("Which character do youg want to know about?")

char_stat = input("What statistic do you want to know about?")


heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
{"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }


print( heroes["wolverine"] )
print( heroes["powers"] )

print( heroes.get(char_name, char_stat) ) 

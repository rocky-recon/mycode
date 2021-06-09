#!/usr/bin/env python3

# open file in read mode
with open("dnsserver.txt", "r") as dnsfile:
    
    # indent to keep the dnsfile object open
    #create list of lines
#    dnslist = dnsfile.readlines()
#this script does the same as showing dnslist = dnsfile.readlines()
    #loop over lines
#    for svr in dnslist:
     for svr in dnsfile:   
         # remove newline char if exists
         #would exists on all but last line
         svr = svr.rstrip('\n') 
         
         # IF the string svr ends with 'org'
         if svr.endswith('org'):
             with open("org-domain.txt", "a") as srvfile:
                 srvfile.write(svr + "\n")

        # ELSE-IF the string svr ends with 'com'
         elif svr.endswith('com'):
             with open("com-domain.txt", "a") as srvfile:
                 srvfile.write(svr + "\n")


         #print and end without a newline
         #print(svr, end=" ")


        #no need to close our file -closed automatically


# open file in read mode
#dnsfile = open("dnsservers.txt", "r")



# create list of lines
#dnslist = dnsfile.readlines()


# loop over lines
#for svr in dnslist:
    #print and end without a newline
 #   print(svr, end="")


# close your file
#dnsfile.close()


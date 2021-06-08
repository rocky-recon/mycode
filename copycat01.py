#!/usr/bin/env python3

import shutil

import os


# move into the working directory
os.chdir("/home/student/mycode/")

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")


# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")



# The following line will create the directory if it does not exist already


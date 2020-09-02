#!/usr/bin/env python3
######## EXPLORE READ ##########

import os 

print("get cwd", os.getcwd())
print("__file__", __file__)    
print("The file is at:", os.getcwd() + "/" +__file__)


print("dirname", os.path.dirname(__file__))   

print(os.getcwd() + "/" + os.path.dirname(__file__))

os.chdir(os.getcwd() + "/" + os.path.dirname(__file__))


## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate thrhough configlist
for x in configlist:
    print(x)

## Always close your file
configfile.close()


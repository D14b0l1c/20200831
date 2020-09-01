#!/usr/bin/env python3
# create a list of strings
farms = [
        {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["hens", "carrots", "celery"]}
         ]

# cycle through the list of farms
for farm in farms:
    print(farm.get("name")+": ", end="")
    
    for animal in farm.get("agriculture"):
        print(animal, end=" ")
    print()          
#for animals in farms:
#    print(animals.get("agriculture"))


print()
print()

for farm in farms:
    print(farm.get("name") + ": ", end="")
    animals = farm.get("agriculture")
    
    # unpacking
    print(*animals, sep=" ")
    print(*animals, sep=" Ei Ei Oh ")



print()
print()

for farm in farms:
    print(farm.get("name") + ": ", end="")
    print(" ".join(farm.get("agriculture")))

#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP", 60, 73]

#print("The items in the list are: ", end="")
#for montypython in my_list:
#   print(montypython, end=" ")
#print()



# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# print(f"This is a really cool way to deal with {mylist[0]} and {mylist[1]}")
# print(mylist[0], mylist[1])


# display the third item in the list
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("When I ssh into IP addresses " + new_list[3] + " or " + new_list[4] + "I am unable to ping ports" + str(new_list[0]) + ", " + new_list[1] + ", " + str(new_list[2]) + ".")

# example of a python f string (new in python 3.6)
print(f"WHen I ssh into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, {new_list[2]}.")

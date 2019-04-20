#!/usr/bin/python3

from Foodchain import foodchain

fc = foodchain("http://127.0.0.1",'corp','ftf')

#transfer assets in the car

#print(dir(foodchain))

print(fc.history("334565432"))


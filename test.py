#!/usr/bin/python3

from Foodchain import foodchain
import datetime
import time


fc = foodchain("http://127.0.0.1",'corp','ftf')


#print(datetime.datetime.now())
#print(dir(datetime.datetime))
#print(datetime.datetime.timestamp())

#fc.create("test","test","test")


fc.transfer("0cf25382262d26ea02c9798923e87e60e23870eafcfa6bba1ed1658e9b2fe206","DgtLE5EveLUpaKJ55KLWpvHutvuLYGmZfcC1Gw9stLHq")

#fc.view_asset("Food")
#print(dir(foodchain))

#print(fc.history("334565432"))


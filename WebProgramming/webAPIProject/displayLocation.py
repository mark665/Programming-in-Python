'''
Created on Feb 12, 2012

@author: mark
Given an address, this prints the lat/long cordinates of the address, as well as the address of the house across the street. s
'''

from pprint import pprint
import urllib2, json

requestLatLogAddress = "http://maps.googleapis.com/maps/api/geocode/json?%s%s"
sensor = "&sensor=false"

print "Enter street address (less city and state) :"
address = raw_input().split()
homeAddress = "address=" + "+".join(address)
print address
address[0] = str(int(address[0]) + 1)
neighborAddress = "address=" + "+".join(address)
print "Enter City : "
city = ",+" + raw_input ()
print "Enter State : "
state = ",+" + raw_input ()

print address
print city
print state

address_request = requestLatLogAddress % (homeAddress+city+state,sensor)
neighbor_request = requestLatLogAddress % (neighborAddress+city+state,sensor)

addressResult = urllib2.urlopen(address_request)
neighborResult = urllib2.urlopen(neighbor_request)
jsonDataAddress = json.load(addressResult)
jsonDataNeighbor = json.load(neighborResult)

print "Cordinates of your house: "
pprint("lat: " + str(jsonDataAddress['results'][0]['geometry']['location']['lat']))
pprint("lng: " + str(jsonDataAddress['results'][0]['geometry']['location']['lng']))

print "Cordinates of your Neighbor's house: "
pprint("lat: " + str(jsonDataNeighbor['results'][0]['geometry']['location']['lat']))
pprint("lng: " + str(jsonDataNeighbor['results'][0]['geometry']['location']['lng']))

'''Three mini-tasks:
1/ recursive permutations
2/ euromillions
3/ google route instructions - note - key would need to be added for use.
'''


import random
import googlemaps
from datetime import datetime


#mini task 1
def get_permutations(list_in):
    results = []
    if len(list_in) == 1:
        results.append(list_in)
        return results
    else:
        for char in list_in:
            inner_results = []
            inner_results = get_permutations([x for x in list_in if x != char])
            for item in inner_results:
                to_add = [char]
                to_add.extend(item)
                results.append(to_add)
        return results

print(get_permutations([1,2,3,4,5]))

#mini task 2
def gen_millions_selection():
    '''function that generates randomly every time you call it a correct euromillions draw to use for your next lottery ticket. lotto rules pick 5 numbers from 1 to 50 and 2 more from 1 to 12'''
    balls =[]
    thunderballs =[]
    choices = []
    balls.extend(random.sample(range(1,51),5))
    thunderballs.extend(random.sample(range(1,13),2))
    balls.sort()
    thunderballs.sort()
    choices.extend(balls)
    choices.extend(thunderballs)
    print(choices)

gen_millions_selection()


#mini task 3
gmaps = googlemaps.Client(key=###) #insert key

def get_lat_lng(address_in):
    geocode_result = gmaps.geocode(address_in)
    location = geocode_result[0]['geometry']['location']
    lat, lng = location['lat'],location['lng']
    return (lat,lng)

def reverse_geocode(lat_in, lng_in):
    addressdata = gmaps.reverse_geocode([lat_in,lng_in])
    return addressdata[0]['formatted_address']

def total_route_distance(list_of_addresses_in):
    '''contains list of 5 uk addresses. calculates total distance of visiting each of these addresses consecutively'''
    total_distance=0
    for i in range(0,4):
        print("Cumulative distance: ", total_distance)
        step_distance = get_route_instructions(list_of_addresses_in[i],list_of_addresses_in[i+1])[1]
        print("Distance from {} to {}: {}".format(list_of_addresses_in[i].title(), list_of_addresses_in[i + 1].title(), step_distance))
        total_distance += step_distance
    return total_distance

def get_route_instructions(address1, address2):
    '''takes 2 addresses and returns a list of shortest way of navigating from spot to spot'''
    direction_result = gmaps.directions(address1, address2, mode='transit',departure_time=datetime.now())
    instructions = []
    distance = direction_result[0]['legs'][0]['distance']['value']
    steps = direction_result[0]['legs'][0]['steps']
    for ministep in steps:
        instructions.append(ministep['html_instructions'])
    return (instructions,distance)
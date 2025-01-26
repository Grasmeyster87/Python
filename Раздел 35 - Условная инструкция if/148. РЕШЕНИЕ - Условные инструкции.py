my_dict = {
    'distance': 12,
}

my_dict1 = {

}

my_dict2 = {
    'speed': 10,
    'time': 10,
}


# def rout_info(dict):
#     if dict.get('distance') and (type(dict['distance']) is int):
#         return f"Distance to your destination is {dict['distance']}"
#     elif (type(dict.get('speed')) is int) and (type(dict.get('time')) is int):
#         return f"Distance to your destination is {dict['speed'] * dict['time']}"
#     else:
#         return "No distance info is available"


def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        route_info = f"Distance to your destination is {route['distance']}"
    elif ('speed' in route) and ('time' in route):
        route_info = f"Distance to your destination is {route['speed'] * route['time']}"
    else:
        route_info = "No distance info is available"
    return route_info

# print(rout_info(my_dict))
# print(rout_info(my_dict1))
#  print(my_dict1.get('time', 'null'))
# print(rout_info(my_dict2))

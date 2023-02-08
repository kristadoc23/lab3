import math
#1 kgr = 2.2046244202 lb
#1 km = 0.6213688756 miles
#1 m = 3.280839895 ft
def kilogram_pounds(x):
    print(x, "kilogram is", x*2.204, "pounds")

def kilometer_mile(x):
    print(x, "kilometer is", x*0.6214, "miles")

def meter_feet(x):
    print(x, "meter is", x*3.281, "feet")

kilogram_pounds(10)
kilometer_mile(10)
meter_feet(10)

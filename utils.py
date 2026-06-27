"""
Implementation of the Haversine formula to calculate the distance between
two geographic points based on their latitude and longitude coordinates.

The returned distance is expressed in kilometers.
"""

import math

def haversine_distance(lat1, lon1, lat2, lon2):
    EARTH_RADIUS_KM = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Apply the Haversine formula to obtain the angular distance.
    a = (math.sin(dlat/2)**2
         + math.cos(lat1)
         * math.cos(lat2)
         * math.sin(dlon/2)**2
    )

    # Calculate the central angle between the two points.
    c = 2 * math.asin(math.sqrt(a))

    distance = EARTH_RADIUS_KM * c

    return distance

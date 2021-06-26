import math


KM_RADIUS = 3960
OTHER_RADIUS = 6371


def distance_kilometers(latitude_a: float, longitude_a: float, latitude_b: float, longitude_b: float):
    latitude = radians(latitude_b - latitude_a)
    longitude = radians(longitude_b - longitude_a)

    a = math.sin(latitude/2) * math.sin(latitude/2) + \
        math.cos(radians(latitude_a)) * math.cos(radians(latitude_b)) * \
        math.sin(longitude/2) * math.sin(longitude/2)
    c = 2 * math.asin(math.sqrt(a))

    return KM_RADIUS * c


def distance_meters(latitude_a: float, longitude_a: float, latitude_b: float, longitude_b: float):
    latitude = radians(latitude_b - latitude_a)
    longitude = radians(longitude_b - longitude_a)

    a = math.sin(latitude/2) * math.sin(latitude/2) + \
        math.cos(radians(latitude_a)) * math.cos(radians(latitude_b)) * \
        math.sin(longitude/2) * math.sin(longitude/2)
    c = 2 * math.asin(math.sqrt(a))

    return KM_RADIUS * c * 1000


def radians(value: float):
    return (math.pi/180) * value

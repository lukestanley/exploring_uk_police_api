from geopy.geocoders import Nominatim

uk_suffix = ', UK'


def geocode(address_string):
    return Nominatim().geocode(address_string)


def get_lat_long_of_postcode(postcode):
    location = geocode(postcode + uk_suffix)
    return [location.latitude, location.longitude]

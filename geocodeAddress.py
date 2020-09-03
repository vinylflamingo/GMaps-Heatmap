import googlemaps
#import geocoder
from datetime import datetime
import pandas
import time


def geocodeAll(city):
    gmaps = googlemaps.Client(key='GOOGLE CLIENT KEY HERE')
    #coords = ""
    colnames = ['address', 'incidentDate']
    data = pandas.read_csv(f"datasets\\lastYear_{city}.csv", names=colnames)
    print(data.columns)
    file = list(data.address)
    print(file)
    latlist = []
    lonlist = []
    for address in file:
        try:
            geocode_result = gmaps.geocode(address)
            #geocode_result = geocode_result.json()
            coordinates = list(geocode_result[0]['geometry']['location'].values())

            lat=coordinates[0]
            lon=coordinates[1]
            #long = list(geocode_result[1]['geometry'])
            print(f"Address: {address}\nLatitude: {lat}\nLongitude:{lon} ")
            latlist.append(lat)
            lonlist.append(lon)

            #lat, lon = map(list, zip(*geocode_result)
            #data['lat'] = lat
            #data['lon'] = lon
        except:
            latlist.append(" ")
            lonlist.append(" ")

    print("\n\n::::Addresses::::\n", file)
    print("\n\n::::Latitudes::::\n", latlist)
    print("\n\n::::Longitudes::::\n", lonlist)
    data['lat'] = pandas.Series(latlist).values
    data['lon'] = pandas.Series(lonlist).values
    data.to_csv(f"datasets\\lastYear_{city}.csv", index=False, header=False)





##DISABLE AFTER TESTING
#geocodeAll("New_Orleans")

from gmplot import *
import numpy as np
import pandas
#import callSql
#import geocodeAddress

class DrawMap:
    def drawMap(self, city, lat, lon):
        print(city)
        gmap = gmplot.GoogleMapPlotter(lat, lon, 12)
        gmap.apikey = "AIzaSyCpKz_VVxBUDgc8_KDzQv5SPD_iu3rBBSc"
        colnames = ['address', 'incidentDate', 'latitudes', 'longitudes']
        data = pandas.read_csv(f"datasets\\lastYear_{city}.csv", names=colnames)
        print(data.columns)
        latlist = list([float(x) for x in(data.latitudes)])
        lonlist = list([float(x) for x in(data.longitudes)])
        print("::::: STARTING MAP CREATION ::::: \n\n")


        gmap.heatmap(latlist, lonlist, opacity=1, radius=30)
        gmap.draw(f"map_lastYear_{city}.html" )

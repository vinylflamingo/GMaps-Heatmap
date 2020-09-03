from drawMap import DrawMap
import time

cities = ["New_Orleans"]
class Init:
    def selectCity(self, city):
        print(f"Que Draw Map for city: {city}")
        if city == "Atlanta":
            pass
            DrawMap.drawMap(city, 33.7490308, -84.3918177)
            print(f"Drawing for city: {city} has been completed")
            return True

        elif city == "New_Orleans":
            DrawMap.drawMap(city, 29.9521747, -90.0773842)
            print(f"Drawing for city: {city} has been completed")
            return True
        else:
            print("There is no city in the cities list")
            return False

isCitySelected = False

while isCitySelected == False:
    for city in cities:
        app = Init()
        isCitySelected = app.selectCity(city)


#comment


#comment 2
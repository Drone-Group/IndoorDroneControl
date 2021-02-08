from pyproj import Transformer

def localize(pointX, pointY, pointZ):

#Coordinate Reference System
    inputEPSG = 3857
    outputEPSG = 4326
    
#Create an instance of the Transformer 
    transformer = Transformer.from_crs(inputEPSG, outputEPSG)

#Perform cartographic transformation
    geoCoordinate = transformer.transform(pointX, pointY, pointZ)

    return geoCoordinate[0], geoCoordinate[1], geoCoordinate[2]


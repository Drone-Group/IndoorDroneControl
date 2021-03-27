import sys
from pyproj import Transformer

def localize(pointX, pointY, pointZ):

#Coordinate Reference System
    inputEPSG = 6584
    outputEPSG = 4326
    
#Create an instance of the Transformer 
    transformer = Transformer.from_crs(inputEPSG, outputEPSG, always_xy=True)

#Perform cartographic transformation
    geoCoordinate = transformer.transform(pointX, pointY, pointZ)

    return geoCoordinate[0], geoCoordinate[1], geoCoordinate[2]

#Output

print(localize(sys.argv[1], sys.argv[2], sys.argv[3]))
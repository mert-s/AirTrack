from opensky_api import OpenSkyApi
import math
api = OpenSkyApi()
#s = api.get_states()
#print(s)
#print(math.atan2(-2, -1)) #y, x


userLat = input("Enter latitude of your location (e.g. 51.093132): ")
userLon = input("Enter longitude of your location (e.g. -0.129310): ")

distanceSetting = 0.1 #0.1 = ~11km, 0.01 = ~1km

def get_nearby_planes(userCoordinateX, userCoordinateY):
    planes = api.get_states(time_secs=0, icao24=None, serials=None, bbox=(userLat - 0.1, userLat + 0.1, userLon - 0.1, userLon + 0.1))
    for p in planes.states:
        print("Airplane detected: " + p.callsign)
        print(calcAngle(userLat, userLon, p.latitude, p.longitude))
    print(planes)

    return planes

def calcAngle(userCoordinateX, userCoordinateY, planeCoordinateX, planeCoordinateY):
    ang = math.atan2(planeCoordinateY - userCoordinateY, planeCoordinateX - userCoordinateX)
    ang = math.degrees(ang)
    if(ang < 0):
        ang = ang + 360

    #angN = 360 - ang + 90

    #if(angN > 360):
    #    angN = angN - 360

    print("angle calculated:" + str(ang))
   # print("angle from north (bearing): " + str(angN))
    return ang

#get_nearby_planes(0,0)
#calcAngle(0, 0, -1, -2)
#calcAngle(0, 0, 1, 2)

def get_planes_relative_angles(planes):
    print("INCOMPLETE")

def get_planes_near_bearing(bearing):
    planes = get_nearby_planes(0,0)

    for p in planes.states:
        if((abs(int(calcAngle(userLat, userLon, p.latitude, p.longitude)) - bearing)) < 30):
            print("Plane detected near bearing " + str(bearing) + ": " + str(p.callsign))


#def callsign_to_airline(callsign): 

get_planes_near_bearing(198)

#calcAngle(51.590439, -0.118943, 51.595560, -0.123273)

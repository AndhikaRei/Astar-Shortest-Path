from Graph import Node
import math
# Menghitung jarak antara dua node dengan latitude dan longitude nya
def haversine_distance(node1, node2):
    # Coordinates in decimal degrees (e.g. 2.89078, 12.79797)
    lon_1 = node1.longitude
    lat_1 = node1.latitude
    lon_2 = node2.longitude
    lat_2 = node2.latitude

    R = 6371000  # radius of Earth in meters
    lat_1_rad = math.radians(lat_1)
    lat_2_rad = math.radians(lat_2)

    delta_lat = math.radians(lat_2 - lat_1)
    delta_lon = math.radians(lon_2 - lon_1)

    a = math.sin(delta_lat / 2.0) ** 2 + math.cos(lat_1_rad) * math.cos(lat_2_rad) * math.sin(delta_lon / 2.0) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R*c
    meters = round(d, 3)  # output distance in meters
    return meters

# =======================================Main Program============================================
a = Node(latitude=-7.150334616558106 , longitude=111.87927513454805)
b = Node(latitude=-7.150435747822007 , longitude=111.8774619613502)
print(haversine_distance(a,b))
# ===============================================================================================



    

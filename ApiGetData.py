import json

import json
import boto3
import math
s3 = boto3.client('s3')

dynamodb = boto3.resource('dynamodb')
"""
@input: origin and destination coordinates as tuple
@return: distance between 2 coordinates in km
"""
def get_distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

def getHotspots(event, context):
    table = dynamodb.Table('ims_data_new')
    remaining_data = table.scan()["Items"]
    
    all_groups = []
    
    while len(remaining_data) > 0:
        tempdata = []
        item = remaining_data[0]
        original_x = float(item["x"])
        original_y =  float(item["y"])
        original_coordinate = (original_x, original_y)
        
        group = []
        for i in range(len(remaining_data)):
            item = remaining_data[i]          
    
            coordinate_x = float(item["x"])
            coordinate_y = float(item["y"]) 
            coordinate = (coordinate_x, coordinate_y)
            distance = get_distance(original_coordinate, coordinate)
            
            if distance <= 3:
                group.append({'coordinate':coordinate, 'name': item['lokalizacja']})
                tempdata.append(item)

        for el in tempdata:
            remaining_data.remove(el)  
            
        elem = group[0]
        all_groups.append({'group_Name': elem['name'], 'routers': group})
    
    return {
        'statusCode': 200,
        'body': json.dumps(all_groups)
    }

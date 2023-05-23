import json
from collections import defaultdict
import numpy as np

# Read the JSON file
with open('grid.geojson', 'r') as file:
    data = json.load(file)

# Create an empty dictionary to store the coordinates
coordinates_dict = defaultdict(list)

# Iterate over the features
for feature in data['features']:
    sector = feature['properties']['sector'];
    # Check if the feature is a polygon
    if feature['geometry']['type'] == 'Polygon':
        # Get the coordinates
        coordinates = feature['geometry']['coordinates']
        # Add the coordinates to the dictionary
        index = int(sector)
        for x, y in coordinates[0]:
            coordinates_dict[index].append((x, y))

# Print the coordinates dictionary
centroids = []
for index, polygon in coordinates_dict.items():
    nparray = np.asarray(polygon, dtype=np.float32)
    centroid = nparray.mean(axis=0)
    centroids.append((index, "{:.20f}".format(centroid[0]), "{:.20f}".format(centroid[1])))
print(centroids)

with open('centroids.csv', 'w') as file:
    file.write("sector,lat,long\n")
    for (sector, long, lat) in centroids:
        file.write(str(sector) + "," + lat + "," + long + "\n")

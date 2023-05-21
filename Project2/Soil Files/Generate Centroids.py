import json
from collections import defaultdict
import numpy as np

# Read the JSON file
with open('grid.json', 'r') as file:
    data = json.load(file)

# Create an empty dictionary to store the coordinates
coordinates_dict = defaultdict(list)

# Iterate over the features
for feature in data['features']:
    # Check if the feature is a polygon
    if feature['geometry']['type'] == 'Polygon':
        # Get the coordinates
        coordinates = feature['geometry']['coordinates']
        # Add the coordinates to the dictionary
        index = len(coordinates_dict) + 1
        for x, y in coordinates[0]:
            coordinates_dict[index].append((x, y))

# Print the coordinates dictionary
centroids = {}
for index, polygon in coordinates_dict.items():
    nparray = np.asarray(polygon, dtype=np.float32)
    centroid = nparray.mean(axis=0)
    centroids[index] = centroid
print(centroids)

with open('centroids.txt', 'w') as file:
    for centroid in centroids.values():
        centroid = centroid.tolist()
        file.write(str(centroid[0]) + ", " + str(centroid[1]) + "\n")

import math
import random

points = []
file = open("data.txt",'r')
for line in file:
    line.strip()
    if line:
        point = line.split(',')
        points.append((float(point[0]),float(point[1])))
file.close()

centroids = random.sample(points,2)

for i in range(50):
    clusters = [[]for i in range(2)]
    for p in points:
        distance = []
        for c in centroids:
            dis = abs((p[0]-c[0])**2 + (p[1]-c[1])**2)
            distance.append(dis)
        index = distance.index(min(distance))
        clusters[index].append(p)

    new_centroid = []
    for cluster in clusters:
        new_x = sum(c[0] for c in cluster)/len(cluster)
        new_y = sum(c[1] for c in cluster)/len(cluster)
        new_centroid.append([new_x,new_y])
print(new_centroid)
for c in clusters:
    print(c)
        
    
                               
            
    

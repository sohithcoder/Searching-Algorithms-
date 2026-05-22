'''
import random

# Distance Matrix (4 cities: 0, 1, 2, 3)
# matrix[i][j] is the distance from city i to city j
matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Initial population: 4 random routes
# Each route is a permutation of [0, 1, 2, 3]
temp = [0,1,2,3]
routes = []
for i in range(4):
    random.shuffle(temp)
    routes.append(temp[:])
# Your 'f' function: Total Distance
# We want this number to be SMALL (unlike N-Queens where 28 was big)
def f(route):
    d = 0
    for i in range(3): # For 4 cities, we check 3 connections
        d += matrix[route[i]][route[i+1]]
    d += matrix[route[3]][route[0]] # Back to start
    return d

# --- MAIN LOOP (Same as your N-Queen pattern) ---
for xdcfhjk in range(100):
    # Sort by distance (Smallest distance is best, so no reverse=True)
    routes = sorted(routes, key=f)
    p1, p2 = routes[0], routes[1]

    # Crossover + Mutation logic
    if random.random() < 0.5:
        z = random.randint(1, 2)
        
        # TSP-Safe Crossover: Take start from p1, fill rest from p2
        new_route = p1[:z]
        for city in p2:
            if city not in new_route:
                new_route.append(city)
        # Replace the worst route (the last one in sorted list)
        routes[-1] = new_route[:]

# Final result
routes = sorted(routes, key=f)
print("Best Route Found:", routes[0])
print("Total Distance:", f(routes[0]))
'''
import random
matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def f(route):
    d = 0
    for i in range(len(route) - 1):
        d += matrix[route[i]][route[i+1]]
    d+=matrix[route[3]][route[0]]
    return d
temp = [0,1,2,3]
routes = []
for i in range(4):
    random.shuffle(temp)
    routes.append(temp[:])

for asdfgh in range(50):
    routes = sorted(routes,key=f)
    p1,p2 = routes[0],routes[1]

    if random.random() < 0.3:
        z = random.randint(1,2)
        new_route = p1[:z]
        for m in p2:
            if m not in new_route:
                new_route.append(m)

        routes[-1] = new_route[:]
print("Best route till now : " )
routes = sorted(routes,key=f)
print(routes[0],f(routes[0]))
    

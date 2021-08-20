import csv
import pulp


def get_dist(tsp):
    with open(tsp, 'rb') as tspfile:
        r = csv.reader(tspfile, delimiter='\t')
        d = [row for row in r]

    d = d[1:] # skip header row
    locs = set([r[0] for r in d]) | set([r[1] for r in d])
    loc_map = {l:i for i, l in enumerate(locs)}
    idx_map = {i:l for i, l in enumerate(locs)}
    dist = [(loc_map[r[0]], loc_map[r[1]], r[2]) for r in d]
    return dist, idx_map


def dist_from_coords(dist, n):
    points = []
    for i in range(n):
        points.append([0] * n)
    for i, j, v in dist:
        points[i][j] = points[j][i] = float(v)
    return points


def find_tour():
    tsp_file = '/Users/test/' + 'my-waypoints-dist-dur.tsv'
    coords, idx_map = get_dist(tsp_file)
    n = len(idx_map)
    dist = dist_from_coords(coords, n)


    # Define the problem
    m = pulp.LpProblem('TSP', pulp.LpMinimize)


    # Create variables
    # x[i,j] is 1 if edge i->j is on the optimal tour, and 0 otherwise
    # Also forbid loops
    x = {}
    for i in range(n+1):
        for j in range(n+1):
            lowerBound = 0
            upperBound = 1

            # Forbid loops
            if i == j:
                upperBound = 0
                # print i,i

            # Create the decision variable and First constraint
            x[i,j] = pulp.LpVariable('x' + str(i) + '_' + str(j), lowerBound, upperBound, pulp.LpBinary)
            # x[j,i] = x[i,j]


    # Define the objective function to minimize
    m += pulp.lpSum([dist[i][j] * x[i,j] for i in range(1,n+1) for j in range(1,n+1)])


    # Add degree-2 constraint (3rd and 4th)
    for i in range(1,n+1):
        m += pulp.lpSum([x[i,j] for j in range(1,n+1)]) == 2


    # Add the last (5th) constraint (prevents subtours)
    u = []
    for i in range(1, n+1):
        u.append(pulp.LpVariable('u_' + str(i), cat='Integer'))
    for i in range(1, n-1):
        for j in range(i+1, n+1):
            m += pulp.lpSum([ u[i] - u[j] + n*x[i,j]]) <= n-1


    # status = m.solve()
    # print pulp.LpStatus[status]
    # for i in range(n):
    #   for j in range(n):
    #       if pulp.value(x[i,j]) >0:
    #           print str(i) + '_' + str(j) + ': ' + str( pulp.value(x[i,j]) )

find_tour()
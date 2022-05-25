def dfs_connections(AP,accessPoints,connections):
    for con in connections[AP]:
        if con in accessPoints:
            accessPoints.remove(con)
            dfs_connections(con,accessPoints,connections)

def get_minimum_connections(matrix):
    if(len(matrix) <= 1):
        return 0
    connections = {}
    accessPoints = set()

    #Collect information regarding the connections
    # and the accessPoints
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if(matrix[i][j]):
                if i not in connections:
                    connections[i] = set()
                if j not in connections:
                    connections[j] = set()
                connections[i].add(j)
                connections[j].add(i)
                accessPoints.add(i)
                accessPoints.add(j)
    
    #Essentially DFS through and count the number
    # of operations to hit every airport
    totalConnectionsNeeded = 0
    while len(accessPoints) > 0:
        AP = accessPoints.pop()
        dfs_connections(AP, accessPoints, connections)
        
        if len(accessPoints) > 0:
            totalConnectionsNeeded += 1
    return totalConnectionsNeeded
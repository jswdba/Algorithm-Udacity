# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    tour =[]
    l=len(graph)
    edges=[]
    edges.append(graph[0])
    graph.remove(graph[0])
    
    for i in range(l):
    	for j in range(i+1,l):
        	if edges[i][1] == graph[j][0]:
        		edges.append(graph[j])
        		graph.remove(graph[j])
        		l = len(graph)
        		break

    
    
    
    return edges

graph =[(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

print (find_eulerian_tour(graph))
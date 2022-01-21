

# time complexity for graph searches is O(vertices + edges)
# DFS to determine if path exists
# BFS to find shortest path

class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    # connections dictionary stores connections between individual vertices
    def add_connection(self, vertex, weight=0):
        self.connections[vertex] = weight

    def get_connections(self):
        # list of connected vertices
        return list(self.connections.keys())

class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    # dictionary stores every vertex
    # vertex data is key and vertex object is value  
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    # creates edge between two vertices
    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_connection(self.graph_dict[to_vertex.value], weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_connection(self.graph_dict[from_vertex.value], weight)

    # checks if path exists between two vertices
    def has_path(self, start_vertex, end_vertex):
        
        stack = [start_vertex]
        seen = set()
        
        while stack:
            current_vertex = stack.pop(0)
            seen.add(current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                # gets edges of current 
                vertices_to_visit = list(self.graph_dict[current_vertex.value].connections.keys())
                # adds vertex to vertices if not already visited
                for vertex in vertices_to_visit:
                    if vertex not in seen:
                        stack.append(vertex)
        
        return False

    def dfs(self, start):
        stack = [start]
        visited = set()
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                result.append(vertex.value)
                visited.add(vertex)
                vertices_to_visit = list(self.graph_dict[vertex.value].connections.keys())
                for vertex in vertices_to_visit:
                    stack.append(vertex)
        
        return result

    ## most basic dfs template
    # def dfs(start):
    #   res = []
    #   stack = [start]
    #   while stack:
    #       curr = stack.pop()
    #       res.append(curr)
    #       for neighbor in graph[curr]:
    #           stack.append(curr)
    #   return res


    def bfs(self, start):
        queue = [start]
        visited = set()
        visited.add(start)
        result = []

        while queue:
            vertex = queue.pop(0)
            result.append(vertex.value)
            vertices_to_visit = list(self.graph_dict[vertex.value].connections.keys())
            for vertex in vertices_to_visit:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)

        return result

    # most basic bfs template
    # def bfs(start):
    #   queue = [start]
    #   while queue:
    #     curr = queue.pop(0)
    #     res.append(curr)
    #     for neighbor in graph[curr]:
    #         queue.append(curr)
    #   return res

    def shortest_path(self, start, target):
        path = [start.value]
        queue = [(start, path)]
        visited = set()
        visited.add(start)
        
        while queue:
            vertex, path = queue.pop(0)
            vertices_to_visit = list(self.graph_dict[vertex.value].connections.keys())
            for vertex in vertices_to_visit:
                if vertex not in visited:
                    if vertex == target:
                        return path + [vertex.value]
                    else:
                        visited.add(vertex)
                        queue.append((vertex, path + [vertex.value]))

    def all_paths(self, start, end):

        stack = [(start, [start.value])]
        result = []
        
        while stack:
            vertex, path = stack.pop()
            if vertex == end:
                result.append(path)
            else:
                vertices_to_visit = list(self.graph_dict[vertex.value].connections.keys())
                for vertex in vertices_to_visit:
                    if vertex.value not in path:
                        stack.append((vertex, path + [vertex.value]))

        return result

    # cycle in undirected graph
    def has_cycle(self, start):

        stack = [start]
        visited = set()
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                return True
            else:
                visited.add(vertex)
                vertices_to_visit = list(self.graph_dict[vertex.value].connections.keys())
                for vertex in vertices_to_visit:
                    if vertex not in visited:
                        stack.append(vertex)
        
        return False

# cycle in directed graph?
# def dfs(crs, courses, visited):

#     # if node is marked as visited during search, then cycle found
#     if visited[crs] == -1:
#         return False
#     # if previously searched, no need to visit again 
#     if visited[crs] == 1:
#         return True
#     # mark node as being visited
#     visited[crs] = -1
#     # visit all the neighbors
#     for c in courses[crs]:
#         if not dfs(c, courses, visited):
#             return False
#     # after all neighbors visited, mark it as fully searched
#     visited[crs] = 1
#     return True



graph = Graph()
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
graph.add_vertex(A)
graph.add_vertex(B)
graph.add_vertex(C)
graph.add_vertex(D)
graph.add_vertex(E)
graph.add_edge(A, B)
graph.add_edge(A, C)
graph.add_edge(B, D)
graph.add_edge(C, D)
graph.add_edge(C, E)
graph.add_edge(D, E)
print(graph.graph_dict)
print('A: ', A.connections)
print('B: ', B.get_connections())
print(graph.has_path(A, D))
print(graph.dfs(A)) # ['A', 'C', 'E', 'D', 'B']
print(graph.bfs(A)) # ['A', 'B', 'C', 'D', 'E']
print(graph.shortest_path(A, E)) # ['A', 'C', 'E']
print(graph.all_paths(A, E)) # [['A', 'C', 'E'], ['A', 'C', 'D', 'E'], ['A', 'B', 'D', 'E'], ['A', 'B', 'D', 'C', 'E']]
print(graph.has_cycle(A)) # True
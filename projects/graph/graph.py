"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        1. create queue
        2. load starting index in queue
        - 
        While q is greater than 0
        3. pop off starting vertex
        4. add neighbors of starting vertex to queue
        5. repeat. 
        """


        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            
            if v not in visited:
                visited.add(v)
                # print("breadth first", v)
                print(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
                   


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        1.create a stack
        2.load stack with the starting vertex
        3. create visited set
        4. while the size of the stack is greater than zero
            pop value off the top  of stack
            if it is not in visited
                push to visited
                print it out
                check for neighbors
                    push neighbors to the stack
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                # print("depth first", v)
                print(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        """
        # if visited == None:
        #     visited = set()
            # if starting_vertex == None:
            #     return
        # print("***DFT_Recursive****")
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for g in self.get_neighbors(starting_vertex):
                self.dft_recursive(g, visited)
                    


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        
        q.enqueue([starting_vertex])
        # print(q)
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for n in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(n)
                    q.enqueue(new_path)


        # q = Queue()
        # path =[]
        # q.enqueue(path)
        # # l.push(starting_vertex)
        # path.append(starting_vertex)

        # visited = set()
        # while q.size() > 0:
        #     v = q.dequeue()
        #     if v not in visited:
        #         if v == destination_vertex:
        #             return path
        #         else:
        #             visited.add(v)
        #             print("breadth first", v)
                    # print(v)
                    # for next_vert in self.get_neighbors(v):
                    #     q.enqueue(next_vert)
   
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        
        s.push([starting_vertex])
        # print(s)
        visited = set()
        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for n in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(n)
                    s.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if path == None and visited == None:
            path = list()
            visited = set()
        # path = path + [starting_vertex]
        if starting_vertex not in visited:
            path.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path
            visited.add(starting_vertex)
            for n in self.get_neighbors(starting_vertex):
                new_path = list(path)
            return self.dfs_recursive(n, destination_vertex, new_path, visited)
            
                

        # if starting_vertex not in visited:
        #     print(starting_vertex)
        #     visited.add(starting_vertex)
        #     path = path + [starting_vertex]
        #     for g in self.get_neighbors(starting_vertex):
        #         self.dft_recursive(g, visited)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

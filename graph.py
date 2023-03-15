from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = ""

    # def __repr__(self):
    #     return 'key:' + str(self.id) #+ ', adj to: ' + str(self.adjacent_to)


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        # create list for all verts and list for all IDs
        self.adj_list = []
        self.adj_list_id = []
        # create list for visited verts (used in conn components)
        self.visited_vertex = []
        # open up input file for reading
        in_file = open(filename, "r")
        # split each line of the input file into the input of a list
        lines = in_file.readlines()
        # loop through each line
        for line in lines:
            # split each line into a list of the line's components (separated by space) to get both vertex
            line = line.split()
            # define both vertex
            v1 = line[0]
            v2 = line[1]
            # add both vertex to adj_list using the self.add_vertex(self, key) function
            self.add_vertex(v1)
            self.add_vertex(v2)
            # add edge between both v1 and v2 using self.add_edge(self, v1, v2) function
            self.add_edge(v1, v2)
        # close file since it will no longer be needed
        in_file.close()

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        # loop through the current adj_list to ensure the vertex is not already in the list
        for vertex in self.adj_list:
            if vertex.id == key:
                return
        # if function not already ended, means not already in list, add vertex to list and id to list
        self.adj_list.append(Vertex(key))
        self.adj_list_id.append(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        # loop through current adj_list to find the vertex's
        for vertex in self.adj_list:
            # create an edge between v1 and v2 (both ways)
            if vertex.id == v1:
                vertex.adjacent_to.append(v2)
            if vertex.id == v2:
                vertex.adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        # loop through current adj_list to find the vertex
        for vertex in self.adj_list:
            # if key found to equal a vertex's ID, return that ID
            if vertex.id == key:
                return vertex
        # if no vertex returned by now, return None
        return None

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        # rename adj_list_id to lst for simplicity
        lst = self.adj_list_id
        # sort the ID list
        for i in range(len(lst) - 1):
            smallest_i = i
            for j in range(i + 1, len(lst), 1):
                if lst[j] < lst[smallest_i]:
                    smallest_i = j
            temp = lst[i]
            lst[i] = lst[smallest_i]
            lst[smallest_i] = temp
        # return sorted ID list
        return lst

    def conn_components(self):
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        # This method MUST use Depth First Search logic!
        # initialize variables for stack, list, and iterators (i + j)
        s = Stack(len(self.adj_list))
        lst = []
        i = 0
        j = 0
        # while loop that goes until the last item in the adj_list is visited
        while i < len(self.adj_list):
            # ensure the current vertex was not already visited by DFS
            if not self.get_vertex(self.get_vertices()[i]).visited:
                # do a dept first search on the vertex
                self.dfs(self.get_vertices()[i], s)
                # add a new sublist to the list
                lst.append([])
                # pop all items on stack to sublist
                while not s.is_empty():
                    lst[j].append(s.pop().id)
                # increase j so that next time DFS runs, the new graph vertex's will be added to a new sublist
                j += 1
            i += 1
        # sort the list so that it is in ascending alphabetical order (insertion because list almost sorted, reversed)
        sorted_lst = []
        for sub_lst in lst:
            sub_lst = sub_lst[::-1]
            for i in range(1, len(sub_lst), 1):
                for j in range(i, 0, -1):
                    if sub_lst[j] < sub_lst[j - 1]:
                        temp = sub_lst[j - 1]
                        sub_lst[j - 1] = sub_lst[j]
                        sub_lst[j] = temp
                    else:
                        break
            sorted_lst.append(sub_lst)
        # set all vertex.visited to False so that conn_components can run again
        for vert_id in self.get_vertices():
            self.get_vertex(vert_id).visited = False
        # finally, return the sorted list of lists
        return sorted_lst

    # recursive Depth First Search (used by self.conn_components)
    def dfs(self, vert, stack):
        vert = self.get_vertex(vert)
        if not vert.visited:
            stack.push(vert)
            vert.visited = True
            for adj_vert in vert.adjacent_to:
                self.dfs(adj_vert, stack)

    def is_bipartite(self):
        for vert_id in self.get_vertices():
            self.get_vertex(vert_id).color = "2"
        # initialize a Queue object
        q = Queue(len(self.get_vertices()))
        # find the first vertex to start the search
        first_vert = self.get_vertex(self.get_vertices()[0])
        # set the first vertex to a color
        first_vert.color = "red"
        # enqueue the first vertex into the queue
        q.enqueue(first_vert)
        # loop while the queue is not empty
        while not q.is_empty():
            # dequeue to get the next vertex up in the queue
            current_vert = q.dequeue()
            # set the new color to the color that the "next vertex" is NOT
            if current_vert.color == "red":
                new_color = "blue"
            else:
                new_color = "red"
            # loop through the adjacent verts to the "next vertex"
            for adj_vert in current_vert.adjacent_to:
                adj_vert = self.get_vertex(adj_vert)
                # if the vert is already colored (with right color) go to next loop
                if adj_vert.color == new_color:
                    continue
                # if the adj vert is the same color as the "next vert", not bipartite
                elif current_vert.color == adj_vert.color:
                    return False
                # else means not already colored, so color the vertex and add it to the queue
                else:
                    adj_vert.color = new_color
                    q.enqueue(adj_vert)
        # set the color of all vertex back to "" so that it can run again
        # if went thought entire loop and False not yet returned, then return True because it IS bipartite
        return True

'''
Understanding:
    - Input data = parent/child relationships over multiple generations
    - Input = list formated as a [parent, child] 
    - Each individual is an integer and unique
    Objective: 
    - return the node that is farthest away from the starting node as the "earliest". 
    - If it is tied for earliest return the one with the lowest numeric value.
    - if input has no parents return -1

Planning:
    -To Do
        -find the parent child relationship and input that somewhere
        -
'''


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    # create the graph 
    # add the vertex's into the graph as one directional: child to parent direction
    # create search method
    # in the search method need to keep track of the paths and whateve path is longest return. 
    q = Queue() # queue of current nodes
    path = [starting_node] # add first node to path set
    q.enqueue(path)
    while q.size() > 0:# list of next layer nodes
        current_path = q.dequeue()
        new_path = []
        changed = False
        for node in current_path: # get begin node of path
            for ancestor in ancestors:# loop through ancestors for parents
                if ancestor[1] == node: # look into each ancestor parent with start_node as child
                    new_path.append(ancestor[0])
                    changed = True
                    q.enqueue(new_path)
                    
        if changed is False:  # loop through final path for largest value
            if current_path[0] == starting_node:
                return -1
            else: 
                return current_path[0]
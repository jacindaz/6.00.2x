# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#
import pdb

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        # prints self.src -> self.dest
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedDigraph(Digraph):

    def __init__(self):
        self.nodes = set([])

        # what kinds of info about edges do I need to store ???
        self.edges = {}  # key is src, value is destination
        self.weighted_edge_objects = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()

        # WHAT IS THE WEIGHT OF THE EDGE ???
        weight = None
        if not(src in self.nodes and dest in self.nodes):
            # can't create an edge without the src + dest nodes
            raise ValueError('Node not in graph')
        else:
        # if the src doesn't have any destinations yet ...
            if src not in self.edges:
                self.edges[src] = []
            self.edges[src].append(dest)
            self.weighted_edge_objects.append(edge)

    def childrenOf(self, node):
        return self.edges[node]

    def findWeightedEdge(self, src, dest):
        for weighted_edge in self.weighted_edge_objects:
            if weighted_edge.src == src and weighted_edge.dest == dest:
                return weighted_edge

    def __str__(self):
        # need to somehow call the WeightedEdge.__str__(self) method
        # and print out all weighted edges

        # looping over self.edges dictionary
        # each key in self.edges is a Node object

        # pdb.set_trace()

        res = ''
        for src_node in self.edges:
            for dest_node in self.edges[src_node]:
                # self.edges[node] returns list of node objects
                # somehow need to search weighted_edge_objects list
                # to find the WeightedEdge object
                weighted_edge_object = self.findWeightedEdge(src_node, dest_node)
                edge_total_distance = weighted_edge_object.total_distance
                edge_outdoor_distance = weighted_edge_object.outdoors_distance

                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, src_node, dest_node, edge_total_distance, edge_outdoor_distance)
        return res[:-1]


        # for weighted_edge in self.weighted_edge_objects:
        #     print "\n=================="
        #     print 'Weighted edge object: ', weighted_edge
        #     print "==================\n"
        #
        #     # pdb.set_trace()
        #
        #     if weighted_edge:
        #         try:
        #             weighted_edge.__str__()
        #         except TypeError:
        #             # pdb.set_trace()
        #             print "\n=================="
        #             print 'Inside WeightedDigraph class'
        #             print 'TypeError has been raised'
        #             print "==================\n"


class WeightedEdge(Edge):

    def __init__(self, src, dest, total_distance, outdoors_distance):
        Edge.__init__(self, src, dest)
        self.total_distance = total_distance
        self.outdoors_distance = outdoors_distance

    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.getTotalDistance()) + ", " + str(self.getOutdoorDistance()) + ")"

    def getTotalDistance(self):
        return self.total_distance

    def getOutdoorDistance(self):
        return self.outdoors_distance


# TESTING FOR WEIGHTED DIGRAPH CLASS---------------------------------------------

g = WeightedDigraph()
na = Node('a')
nb = Node('b')
nc = Node('c')

g.addNode(na)
g.addNode(nb)
g.addNode(nc)

e1 = WeightedEdge(na, nb, 15, 10)
# print e1
# # =>a->b (15, 10)

# print e1.getTotalDistance()
# # => 15

# print e1.getOutdoorDistance()
# # =>10

e2 = WeightedEdge(na, nc, 14, 6)
e3 = WeightedEdge(nb, nc, 3, 1)
# print e2
# # => a->c (14, 6)

# print e3
# # => b->c (3, 1)

g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)

g.childrenOf(na)                 # =>[b, c]

print g

# try:
#     print g
# except TypeError:
#     print "\n=================="
#     print 'Attempted to print g'
#     print 'TypeError has been raised'
#     print "==================\n"
# # => a->b (15.0, 10.0)
# # => a->c (14.0, 6.0)
# # => b->c (3.0, 1.0)

# pdb.set_trace()

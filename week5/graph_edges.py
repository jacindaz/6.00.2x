from graph import *
import pdb


# NODE OBJECT - name
# EDGE OBJECT - src, destination
# WEIGHTED EDGE - src, dest, weight
# DIGRAPH - nodes, edges


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(nodes[0], nodes[1]))
g.addEdge(Edge(nodes[0], nodes[2]))
g.addEdge(Edge(nodes[1], nodes[4]))
g.addEdge(Edge(nodes[2], nodes[3]))
g.addEdge(Edge(nodes[3], nodes[5]))
g.addEdge(Edge(nodes[4], nodes[5]))

edges = g.childrenOf(nodes[0])

print 'Printing edges...'
for n in nodes:

    # pdb.set_trace()

    print "\n=============="
    print 'Node: ', n.name
    for child_node in g.childrenOf(n):
        print 'Edges: ', child_node.name
    print "==============\n"

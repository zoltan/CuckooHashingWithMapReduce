import sys
import gv
from pygraph.classes.graph import graph
from pygraph.readwrite.dot import write
from pygraph.algorithms.accessibility import connected_components

def h1(x):
	return 5*(x + 5) % 11;

def h2(x):
	return 7*(x + 3) % 19;

gr = graph()

U = []
W = []
E = []
for i in range(30):
	x = 'u' + str(h1(i))
	y = 'w' + str(h2(i))
	U.append(x)
	W.append(y)
	E.append((x,y))

gr.add_nodes(list(set(U)))
gr.add_nodes(list(set(W)))
for edge in E:
	gr.add_edge(edge)

inv_map = {}
for k, v in connected_components(gr).iteritems():
    inv_map[v] = inv_map.get(v, [])
    inv_map[v].append(k)

nodemapping = {}

newmap = {}
for k in inv_map.keys():
	C = min(map(lambda x : x[1:], inv_map[k]))
	for v in inv_map[k]:
		nodemapping[v] = v + '__' + str(C)

newgraph = graph()
newgraph.add_nodes(map(lambda x : nodemapping[x], gr.nodes()))
for edge in E:
	Q = (nodemapping[edge[0]], nodemapping[edge[1]])
	newgraph.add_edge(Q)
#for edge in E:
#	print E
#	newgraph.add_edge((nodemapping[edge[0]], nodemapping[edge[1]]))

dot = write(newgraph)
gvv = gv.readstring(dot)
gv.layout(gvv, 'dot')
gv.render(gvv, 'png', 'x.png')

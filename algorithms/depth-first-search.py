import math
from collections import deque

#--------------------------------------------------------------------
# DEFINE COLORS
WHITE = 'WHITE'
GREY = 'GREY'
BLACK = 'BLACK'

#--------------------------------------------------------------------
class vertex:
	def __init__(self, id = None):
		self.id = id
		self.color = None
		self.distance = None
		self.predecessor = None
		self.cost = 1				# NOTE: THIS COST FUNCTION IS FOR A SPECIFIC IMPLEMENTATION.
		self.adj = {}
		self.finish = None
	
	def addAdjacency(self, vertex, weight = 0):
		self.adj[vertex] = weight

#--------------------------------------------------------------------
class graph:
	def __init__(self):
		self.vList = {}
		self.numVertices = 0
	
	def addVertex(self, id):
		self.numVertices += 1
		newVertex = vertex(id)
		self.vList[id] = newVertex

	def addEdge(self, start, end, weight = 0):
		self.vList[start].addAdjacency(self.vList[end], weight)

	def __iter__(self):
		return iter(self.vList.values())

#--------------------------------------------------------------------
def dfs_visit(graph, u, time):
	time += 1
	u.distance = time
	u.color = GREY
	for v in u.adj:
		if v.color == WHITE:
			v.predecessor = u
			dfs_visit(graph, v, time)
	u.color = BLACK
	time += 1
	u.finish = time

def dfs(graph):
	for u in graph:
		u.color = WHITE
		u.predecessor = None
	time = 0
	for u in graph:
		if u.color == WHITE:
			dfs_visit(graph, u, time)

#--------------------------------------------------------------------
def test_implementation():

	#SETUP GRAPH CONSISTING OF ADJACENCIES
	g = graph()
	
	g.addVertex(1)
	g.addVertex(2)
	g.addVertex(3)
	g.addVertex(4)

	g.addEdge(1,2,1)
	g.addEdge(1,3,2)
	g.addEdge(2,1,0.5)
	g.addEdge(2,3,2.5)
	g.addEdge(3,1,3)
	g.addEdge(3,2,1.2)
	g.addEdge(3,4,2)

	dfs(g)
	print(g.vList[2].finish)

#--------------------------------------------------------------------
test_implementation()


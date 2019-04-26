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
def bfs(g, start):
	for v in g:
		if v.id != start:
			v.color = WHITE
			v.distance = math.inf
			v.predecessor = None

	s = g.vList[start]
	s.color = GREY
	s.distance = 0
	s.predecessor = None

	Q = deque()
	Q.append(s)
	while len(Q) != 0:
		u = Q.pop()
		for v in u.adj:
			if v.color == WHITE:
				v.color = GREY
				v.distance = u.distance + 1
				v.predecessor = u
				v.cost = u.cost * u.adj[v]	# COST ACCUMULATION DEPENDS ON SPECIFIC IMPLEMENTATION GOALS
				Q.appendleft(v)
		u.color = BLACK

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

	bfs(g, 2)
	print(g.vList[4].cost)

#--------------------------------------------------------------------
test_implementation()


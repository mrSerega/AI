class Graph:

	storage = None

	# costs = None

	def __init__(self):
		self.storage = dict()
		self.cost = dict()
		pass

	def addNode(self, nodeName):
		try:
			self.storage[nodeName]
		except:
			self.storage[nodeName] = set()
			# self.costs[nodeName] = set()

	def addEdge(self, firstNode, secondNode, cost = 0, bi=False):
		self.addNode(firstNode)
		self.addNode(secondNode)
		self.storage[firstNode].add(secondNode)
		# self.costs[(firstNode,secondNode)] = cost
		if bi:
			self.storage[secondNode].add(firstNode)
			# self.costs[(secondNode,firstNode)] = cost

	def show(self):
		print (self.storage)
		print (self.costs)

	def showEdges(self):
		for key, value in self.storage.items():
			for v in value:
				print (key, v)

	def deleteNode(self,nodeName):
		try:
			del self.storage[nodeName]
			for values in self.storage.values():
				try:
					values.remove(nodeName)
				except:
					pass
		except:
			pirnt ('unknown node')

	def deleteEdge(self, firstNode, secondNode, bi=False):
		try:
			self.storage[firstNode].remove(secondNode)
			if bi: self.storage[secondNode].remove(firstNode)
		except:
			pass

	def isConnected(self, firstNode, secondNode):
		try:
			self.storage[firstNode]
		except:
			return False
            
		try:
			self.storage[secondNode]
		except:
			return False
            
		marks = []
		return self.BFS(firstNode, secondNode, marks)
	
	def BFS(self, firstNode, secondNode, marks):
		if secondNode in self.storage[firstNode]: return True
		marks.append(firstNode)
		for node in self.storage[firstNode]:
			if node not in marks: return self.BFS(node, secondNode, marks)
		return False
        
if __name__ == '__main__':
    graph = Graph()

    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('E')
    graph.addNode('F')

    graph.addEdge('A','B',1,True)
    graph.addEdge('B','C',2)
    graph.addEdge('C','D',3)
    graph.addEdge('D','B',4)
    graph.addEdge('C','E',5)
    graph.addEdge('D','F',5)
    graph.addEdge('F','A',5)
    
    graph.addNode('F')

    graph.show()

    firstNode = 'F'
    secondNode = 'E'

    print ('is {} connectd with {}'.format(firstNode, secondNode))
    print(graph.isConnected(firstNode,secondNode))
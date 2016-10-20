import sys
from graphviz import Digraph
import copy
import numpy

ZERO  = 0
POS  = 1
NEG = -1
MAX = 2

INF = 100000000

Expanded = []
ToExpand = []
Connection = []

AllStates = []
ValidStates = []
StableStates = []
UnstableStates =[]

class State ():
	def __init__(self, IF, DIF, V, DV):
		self.IF = IF
		self.DIF = DIF
		self.V = V
		self.DV = DV
	def toString(self):
		d = (self.IF + 1) * 1000 + (self.DIF + 1) * 100 + (self.V + 1) * 10 + (self.DV +1)
		return str(d)

	def status(self, index):
		s = str(index) + ' '

		if self.IF == ZERO:
			s += '0'
		else:
			s += '+' 

		# self.string += ' DIF: '
		if self.DIF == ZERO:
			s += '0'
		elif self.DIF == POS:
			s += '+' 
		else:
			s += '-'

		s += ' '

		# self.string += 'V: '
		if self.V == ZERO:
			s += '0'
		elif self.V == POS:
			s += '+' 
		else:
			s += 'M' 

		# self.string += ' DV: '
		if self.DV == ZERO:
			s += '0'
		elif self.DV == POS:
			s += '+' 
		else:
			s += '-'

		s += ' '

		# s += 'V: '
		if self.V == ZERO:
			s += '0'
		elif self.V == POS:
			s += '+' 
		else:
			s += 'M' 

		# self.string += ' DV: '
		if self.DV == ZERO:
			s += '0'
		elif self.DV == POS:
			s += '+' 
		else:
			s += '-'

		# s += '\n'
		return s


def isValid(s):
	if s.IF == ZERO and s.DIF == NEG:
		return False
	if (s.V == 0  and s.DV == NEG) or (s.OF == 0 and s.DOF == NEG):
		return False
	return True

def buildAllStates ():
	global AllStates
	AllStates.append(State(ZERO, ZERO, ZERO, ZERO))
	AllStates.append(State(ZERO, POS, ZERO, ZERO))
	AllStates.append(State(POS, NEG, POS, ZERO))
	AllStates.append(State(POS, ZERO, POS, ZERO))
	AllStates.append(State(POS, POS, POS, ZERO)) # 5
	AllStates.append(State(POS, NEG, MAX, ZERO))
	AllStates.append(State(POS, ZERO, MAX, ZERO))
	AllStates.append(State(POS, POS, MAX, ZERO)) # 8
	AllStates.append(State(POS, NEG, ZERO, POS))
	AllStates.append(State(POS, ZERO, ZERO, POS))
	AllStates.append(State(POS, POS, ZERO, POS))#11
	AllStates.append(State(POS, NEG, POS, POS))
	AllStates.append(State(POS, ZERO, POS, POS))
	AllStates.append(State(POS, POS, POS, POS))
	AllStates.append(State(ZERO, ZERO, POS, NEG))
	AllStates.append(State(ZERO, POS, POS, NEG))
	AllStates.append(State(POS, NEG, POS, NEG)) # 17
	AllStates.append(State(POS, ZERO, POS , NEG))
	AllStates.append(State(POS, POS, POS , NEG))
	AllStates.append(State(ZERO, ZERO, MAX , NEG))#20
	AllStates.append(State(ZERO, POS, MAX, NEG))
	AllStates.append(State(POS, NEG, MAX, NEG))
	AllStates.append(State(POS, ZERO, MAX, NEG))# 23
	AllStates.append(State(POS, POS, MAX, NEG))
def addConnection(i, j, Connection):
	global AllStates
	Connection.append((AllStates[i-1].toString(), AllStates[j-1].toString()))

def buildConnections ():
	global Connection
	addConnection(1,2, Connection)
	addConnection(2,11, Connection)
	addConnection(3,17, Connection)
	addConnection(4,5, Connection)
	addConnection(5,14, Connection)
	addConnection(6,22, Connection)
	addConnection(7,6, Connection)
	addConnection(7,8, Connection)
	addConnection(9,12, Connection)
	addConnection(10,13, Connection)
	addConnection(11,14, Connection)
	addConnection(12,13, Connection)
	addConnection(13,3, Connection)
	addConnection(13,7, Connection)
	addConnection(13,6, Connection)
	addConnection(13,7, Connection)
	addConnection(13,14, Connection)
	addConnection(13,4, Connection)
	addConnection(13,3, Connection)
	addConnection(14,7, Connection)
	addConnection(14,4, Connection)
	addConnection(15,1, Connection)
	addConnection(15,2, Connection)
	addConnection(15,16, Connection)
	addConnection(16,19, Connection)
	addConnection(17,1, Connection)
	addConnection(17,15, Connection)
	addConnection(17,4, Connection)
	# addConnection(17,15)
	addConnection(18,17, Connection)
	addConnection(18,19, Connection)
	addConnection(18,5, Connection)
	addConnection(18,4, Connection)
	addConnection(19,18, Connection)
	addConnection(19,5, Connection)
	addConnection(20,16, Connection)
	addConnection(20,15, Connection)
	addConnection(21,19, Connection)
	addConnection(22,17, Connection)
	addConnection(23,19, Connection)
	addConnection(23,18, Connection)
	addConnection(23,17, Connection)
	addConnection(24,19, Connection)

def draw():
	dot = Digraph (comment = 'test2')
	for i in range(len(AllStates)):
		s = AllStates[i]
		dot.node(s.toString(), s.status(i+1))
	for (s, t) in Connection:
		dot.edge(s, t)

	dot.render('test2.gv', view=True)

def trace (state, DIFlist):
	global Connection
	dot = Digraph (comment = 'trace')
	# now we expand and visit all the states 
	# Visited = [state]

	newConn = {}
	newConnInterLevel = {}
	rechableStates = {}
	CanAccess = {} 
	# CanAccess[state.DIF] = [state]
	for i in range(len(DIFlist)):
		newConn[i] = []
		newConnInterLevel[i] = []
		CanAccess[i] = []

	CanAccess[0] = [state]
	for i in range(len(DIFlist)):
		d = DIFlist[i]
		print 'I am currently dealing with ', i
		# denote a list of nodes to visit
		toVisit = copy.copy(CanAccess[i]) 
		print 'there are ', len(toVisit), ' states to visit'
		while len(toVisit) != 0: 
			s = toVisit [0] #pick a state
			print 'visiting ', s.toString()
			for t in AllStates:
				if (s.toString(), t.toString()) in Connection:
					if t.DIF == d:
						# this is the situation that we need to add to the accessible next states
						print '\t it has access to', t.toString()
						CanAccess[i].append(t) 
						toVisit.append(t)
						newConn[i].append((s, t))
			toVisit.remove(s) 
		# prepare the next d
		if (CanAccess[i] != [] and i+1 != len(DIFlist)):
			d_next = DIFlist[i+1] 
			for s in CanAccess[i]:
				print 'INTER-visiting ', s.toString()
				for t in AllStates:
					if (s.toString(), t.toString()) in Connection:
						if t.DIF == d_next:
							print '\t INTER ', s.toString(), ' has access to', t.toString()
							CanAccess[i+1].append(t)
							print '\t\tafter adding, it has ', len(CanAccess[i+1]) , ' to visit'
							newConnInterLevel[i].append((s, t))
			print 'from prediction, there are at least', len(CanAccess[i+1]), ' nodes to visit at the next level'
			# print '\t\t----prepare the next to visit-----'
			# for n in CanAccess[d_next]:
				# print '\t\t\tstates in preparation', n.status(0)
		# print '\n', d

		# for s in CanAccess[d]:
		rechableStates[i] = copy.copy(CanAccess[i]) 
		# visitedStates = list(set(visitedStates))
		# newConnection = list (set (newConnection))

	return (rechableStates, newConn, newConnInterLevel)

def drawTrace (states, conn, connInter):
	dot = Digraph (comment = 'trace')
	for s in sum(states.values(), []):
		dot.node(s.toString(), s.status(0))

	l = sum(conn.values(), [])
	k = sum(connInter.values(), [])
	for (s, t) in  list(set(l + k)):
		dot.edge(s.toString(), t.toString())

	dot.render('trace.gv', view=True) 

				

def shortestPath (s0, states, conn, connInter, DIFlist):
	backtrace = {} 
	m = []
	for d in DIFlist:
		distance = {}
		m.append(distance)

	for i in range(len(DIFlist)):
		for t in states[i]:
			m[i][t] = INF
	
	m[0][s0] = 0
	print 'start from ', s0.toString()
	for i in range(len(DIFlist)):
		d = DIFlist[i]
		print '---------- ', i
		print 'There are ', len(states[i]), ' states'
		print 'There are ', len(conn[i]), ' inner connections'
		print 'There are ', len(connInter[i]), ' inter connections'
		#initialise the
		# for t in states[d]:
		# 	if t not in m[i].keys():
		# 		m[i][t] = INF #initialise it's distance to infinity

		toVisit = copy.copy(states[i])
		nextVisit = toVisit[0] #a random state
		dis = INF
		for a in toVisit :
			if dis >= m[i][a]:
				dis = m[i][a]
				nextVisit = a
		#always visit the next closest one
		while len(toVisit) != 0:
			for (t1, t2) in conn[i]: 
				if (t1 == nextVisit):
					if m[i][t2] > m[i][t1] + 1:
						m[i][t2] = m[i][t1] + 1
						backtrace[t2] = t1
						print t1.toString() , ' -> ', t2.toString(), 'distance: ', m[i][t2]
			toVisit.remove(nextVisit) #???
			# after visiting all the nodes, select a next one to visit, it must be the losest one
			# for e in toVisit:
			# 	print e.toString()
			dis = INF
			for a in toVisit :
				if dis >= m[i][a]:
					dis = m[i][a]
					nextVisit = a
			# print 'among this, I choose ', nextVisit.toString()
		# next , update the inter level edges if it is not the last level
		# next visit ?
		dis = INF
		for a in states[i]:
			if dis >= m[i][a]:
				dis = m[i][a]
				nextVisit = a

		if i+1 != len(DIFlist):
			d_next = DIFlist[i+1]
			toVisit = copy.copy(states[i])
			while toVisit != []:
				#update the distance to the next level
				for (t1, t2) in connInter[i]:
					if (t1 == nextVisit):
						if m[i+1][t2] > m[i][t1] + 1:
							m[i+1][t2] = m[i][t1] + 1
							backtrace[t2] = t1
							print t1.toString() , ' --> ', t2.toString(), 'distance: ', m[i+1][t2]

				# print len(toVisit)
				toVisit.remove(nextVisit)
				# after visiting all the nodes, select a next one to visit, it must be the closest one
				dis = INF
				for a in toVisit:
					if dis >= m[i][a]:
						dis = m[i][a]
						nextVisit = a

	# return the backtrace
	lastLevelStates = states[len(DIFlist) -1]
	dis = INF
	for a in lastLevelStates:
		if dis >= m[i][a]:
			dis = m[i][a]
			nextVisit = a

	backlist = [nextVisit]
	# print nextVisit.toString()
	while nextVisit != s0:
		nextVisit = backtrace[nextVisit]
		backlist.append(nextVisit)
		# print nextVisit.toString()
	backlist.append(s0)
	path = copy.copy(backlist)
	path.reverse()
	# print 'is it empty? ', type(path)
	return path







def  main():
	buildAllStates()
	buildConnections ()
	# draw()
	# s = State(POS,NEG,POS,ZERO)
	# (visitedStates, conn) = trace(s, [NEG, ZERO,POS,ZERO])
	s = State(ZERO,POS,ZERO,ZERO)
	DIFlist = [POS, ZERO,NEG,ZERO]
	(states, conn, connInter) = trace(s, DIFlist)
	# drawTrace(states, conn, connInter)
	path =  shortestPath(s, states, conn, connInter, DIFlist)
	print 'print path: '
	for p in path:
		print p.toString()




if __name__ == "__main__":
		main()



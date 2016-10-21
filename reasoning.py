# Shuai Wang 11108339
# Aashish Venkatesh 11392363

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

index = {}

def toStr (num):
	if num == ZERO:
		return 'ZERO'
	elif num == POS:
		return 'POS'
	elif num == NEG:
		return 'NEG'
	elif num == MAX:
		return 'MAX'
	else: return 'ERROR'

class State ():
	def __init__(self, IF, DIF, V, DV):
		self.IF = IF
		self.DIF = DIF
		self.V = V
		self.DV = DV
	def toString(self):
		d = (self.IF + 1) * 1000 + (self.DIF + 1) * 100 + (self.V + 1) * 10 + (self.DV +1)
		return str(d)

	def status(self,id):
		# s = str(index) + ' '
		# s="IF,DIF V,DV H,DH P,DP OF,DOF"+"\n"
		global index
		s= 'ID='+ str(index[self.toString()]) +'  '+'IF('

		if self.IF == ZERO:
			s += '0,'
		else:
			s += '+,' 

		# s += ' dIF = '
		# self.string += ' DIF: '
		if self.DIF == ZERO:
			s += '0)'
		elif self.DIF == POS:
			s += '+)' 
		else:
			s += '-)'

		s += r"\n"

		# self.string += 'V: '
		s += 'V('
		if self.V == ZERO:
			s += '0,'
		elif self.V == POS:
			s += '+,' 
		else:
			s += 'M,' 

		# s += '\n'	
		# s += 'dV/dH/dPr/dOF =  '
		# self.string += ' DV: '
		if self.DV == ZERO:
			s += '0)'
		elif self.DV == POS:
			s += '+)' 
		else:
			s += '-)'

		s += ' H('

		# s += 'V: '
		if self.V == ZERO:
			s += '0,'
		elif self.V == POS:
			s += '+,' 
		else:
			s += 'M,' 

		# self.string += ' DV: '
		if self.DV == ZERO:
			s += '0)'
		elif self.DV == POS:
			s += '+)' 
		else:
			s += '-)'

		s += r"\n"

		s += 'Pr('
		if self.V == ZERO:
			s += '0,'
		elif self.V == POS:
			s += '+,' 
		else:
			s += 'M,' 

		# self.string += ' DV: '
		if self.DV == ZERO:
			s += '0)'
		elif self.DV == POS:
			s += '+)' 
		else:
			s += '-)'

		s += ' OF('

		# s += 'V: '
		if self.V == ZERO:
			s += '0,'
		elif self.V == POS:
			s += '+,' 
		else:
			s += 'M,' 

		# self.string += ' DV: '
		if self.DV == ZERO:
			s += '0)'
		elif self.DV == POS:
			s += '+)' 
		else:
			s += '-)'

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
	for i in range(len(AllStates)):
		index[AllStates[i].toString()] = i+1
def addConnection(i, j, Connection):
	global AllStates
	Connection.append((AllStates[i-1].toString(), AllStates[j-1].toString()))

def buildConnections ():
	global Connection
	addConnection(1,2, Connection)
	addConnection(2,11, Connection)
	addConnection(3,17, Connection)
	addConnection(4,5, Connection)
	addConnection(4,3, Connection)
	addConnection(5,14, Connection)
	addConnection(6,22, Connection)
	addConnection(7,6, Connection)
	addConnection(7,8, Connection)
	addConnection(9,12, Connection)
	addConnection(10,13, Connection)
	addConnection(10,12, Connection)
	addConnection(10,14, Connection)
	addConnection(11,14, Connection)
	addConnection(12,13, Connection)
	addConnection(12,4, Connection)
	addConnection(13,3, Connection)
	addConnection(13,6, Connection)
	addConnection(13,7, Connection)
	addConnection(13,14, Connection)
	addConnection(13,4, Connection)
	addConnection(14,4, Connection)
	addConnection(14,7, Connection)
	addConnection(15,1, Connection)
	addConnection(15,2, Connection)
	addConnection(15,16, Connection)
	addConnection(16,19, Connection)
	addConnection(17,1, Connection)
	addConnection(17,15, Connection)
	addConnection(17,4, Connection)
	addConnection(17,18, Connection)
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

def trace (state, DIFList):
	global Connection
	dot = Digraph (comment = 'trace')
	# now we expand and visit all the states 
	# Visited = [state]

	newConn = {}
	newConnInterLevel = {}
	rechableStates = {}
	CanAccess = {} 
	# CanAccess[state.DIF] = [state]
	for i in range(len(DIFList)):
		newConn[i] = []
		newConnInterLevel[i] = []
		CanAccess[i] = []

	CanAccess[0] = [state]
	for i in range(len(DIFList)):
		d = DIFList[i]
		# print 'I am currently dealing with ', i
		# denote a list of nodes to visit
		toVisit = copy.copy(CanAccess[i]) 
		# print 'there are ', len(toVisit), ' states to visit'
		while len(toVisit) != 0: 
			s = toVisit [0] #pick a state
			# print 'visiting ', s.toString()
			for t in AllStates:
				if (s.toString(), t.toString()) in Connection:
					if t.DIF == d:
						# this is the situation that we need to add to the accessible next states
						# print '\t it has access to', t.toString()
						if t not in CanAccess[i]: 
							CanAccess[i].append(t) 
						toVisit.append(t)
						newConn[i].append((s, t))
			toVisit.remove(s) 
		# prepare the next d
		if (CanAccess[i] != [] and i+1 != len(DIFList)):
			d_next = DIFList[i+1] 
			for s in CanAccess[i]:
				# print 'INTER-visiting ', s.toString()
				for t in AllStates:
					if (s.toString(), t.toString()) in Connection:
						if t.DIF == d_next:
							# print '\t INTER ', s.toString(), ' has access to', t.toString()
							if t not in CanAccess[i+1]: 
								CanAccess[i+1].append(t)
							# print '\t\tafter adding, it has ', len(CanAccess[i+1]) , ' to visit'
							newConnInterLevel[i].append((s, t))
			# print 'from prediction, there are at least', len(CanAccess[i+1]), ' nodes to visit at the next level'
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
	# dot = Digraph (comment = 'trace')
	dot = Digraph(name='pet-shop', node_attr={'shape': 'note','labeljust': 'r'})
	index = 1
	for s in sum(states.values(), []):
		dot.node(s.toString(), s.status(index))
		index += 1

	l = sum(conn.values(), [])
	k = sum(connInter.values(), [])
	for (s, t) in  list(set(l + k)):
		dot.edge(s.toString(), t.toString())

	dot.render('trace.gv', view=True) 


def drawShortestPath(states, conn, connInter, path):
	# dot = Digraph (comment = 'trace')
	dot = Digraph(name='pet-shop', node_attr={'shape': 'note','labeljust': 'r'})
	index = 1
	for s in sum(states.values(), []):
		dot.node(s.toString(), s.status(index))
		index += 1

	l = sum(conn.values(), [])
	k = sum(connInter.values(), [])
	for (s, t) in  list(set(l + k)):
		flag = False
		for i in range(len(path) -1):
			if path[i] == s and path[i+1] == t:
				flag = True
		if flag : 
			dot.edge(s.toString(), t.toString(), color = 'red')
		else: 
			dot.edge(s.toString(), t.toString())
	dot.render('shortest.gv', view=True)


				

def shortestPath (s0, states, conn, connInter, DIFList):
	print '------------------------ Step 1 --------------------------------'
	print 'start to generate the shortest path of every state from ', s0.toString()

	backtrace = {} 
	m = []
	for d in DIFList:
		distance = {}
		m.append(distance)

	for i in range(len(DIFList)):
		for t in states[i]:
			m[i][t] = INF
	
	m[0][s0] = 0
	# print 'start from ', s0.toString()
	for i in range(len(DIFList)):
		d = DIFList[i]
		# print 'This is level ', i
		# print '\tThere are ', len(states[i]), ' states'
		# print '\tThere are ', len(conn[i]), ' inner connections'
		# print '\tThere are ', len(connInter[i]), ' inter connections'
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
						backtrace[(i,t2)] = (i, t1)
						# print '\t\tINNER: update the distance from',  t1.toString() , ' to ', t2.toString(), 'as ', m[i][t2]
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

		if i+1 != len(DIFList):
			d_next = DIFList[i+1]
			toVisit = copy.copy(states[i])
			while toVisit != []:
				#update the distance to the next level
				for (t1, t2) in connInter[i]:
					if (t1 == nextVisit):
						if m[i+1][t2] > m[i][t1] + 1:
							m[i+1][t2] = m[i][t1] + 1
							backtrace[(i+1,t2)] = (i,t1)
							# print '\t\tOUTTER: update the distance from', t1.toString() , ' to ', t2.toString(), 'as ', m[i+1][t2] ,'(for the next level)'

				# print len(toVisit)
				toVisit.remove(nextVisit)
				# after visiting all the nodes, select a next one to visit, it must be the closest one
				dis = INF
				for a in toVisit:
					if dis >= m[i][a]:
						dis = m[i][a]
						nextVisit = a

	# return the backtrace
	lastLevelStates = states[len(DIFList) -1]
	lastLevelIndex = len(DIFList) -1


	terminatingStates = []
	for s in lastLevelStates:
		if s.DIF == ZERO and s.DV == ZERO:
			terminatingStates.append(s)
	
	distance = INF
	bestTerminating = terminatingStates[0]
	

 # if there is a terminating state then I use it, otehrwise, I use the shortest path one
 	print '-------------------------------------step 2---------------------------------------'
	print 'Now that we have computed the shortest distance of all the states, we need to obtain the path'
	print 'First, we compute the best terminating state:'

	if len(terminatingStates) != 0:
		for st in terminatingStates:
			if m[lastLevelIndex][st] <= distance:
				bestTerminating = st
				distance = m[lastLevelIndex][st]
		print 'we found a stable terminating state (DIF = 0, DV = 0) with the shortest distance: ', bestTerminating.toString()
	else: 
		dis = INF
		for a in lastLevelStates:
			if dis >= m[i][a]:
				dis = m[i][a]
				bestTerminating = a
		print 'we cannot find a terminating state but we can start from the state with the shortest distance'


	backlist = [bestTerminating] # start from the best terminating state
	# print 'best = ', bestTerminating.toString()
	# print nextVisit.toString()
	level = len(DIFList) - 1 
	# print backtrace
	# print level
	while bestTerminating != s0:
		(k, b) = backtrace[(level, bestTerminating)]
		# print '\t This is level' , level, ' from the state ', bestTerminating.toString(), ', we trace back and get',  b.toString(), 'at level ', k 
		bestTerminating = b
		backlist.append(bestTerminating) # prepare for the next iteration
		level = k
		# print nextVisit.toString()
	backlist.append(s0)
	path = copy.copy(backlist)
	path.reverse()

	for i in range(len(path) -1):
		print 'At step ', i+1
		if path[i].DIF != path[i+1].DIF :
			print 'Due to the effect of the change of DIF from', toStr(path[i].DIF) , ' to ', toStr(path[i+1].DIF)
			print '\tThe previous state IF(', toStr(path[i].IF) ,', ', toStr(path[i].DIF), ')\n\t\t\t V(', toStr(path[i].V), ', ',toStr(path[i].DV), ') H(', toStr(path[i].V), ', ',toStr(path[i].DV), ') \n\t\t\tPr(', toStr(path[i].V), ', ',toStr(path[i].DV), ') OF(', toStr(path[i].V), ', ',toStr(path[i].DV) ,')'
			print '\tThe consequent state IF(', toStr(path[i+1].IF) ,', ', toStr(path[i+1].DIF), ')\n\t\t\t V(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') H(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') \n\t\t\tPr(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') OF(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV) ,')' 
			
		elif path[i].DIF == path[i+1].DIF and path[i].IF != path[i+1].IF:
			print 'Due to the effect of the change of IF from', toStr(path[i].IF), ' to ', toStr(path[i].IF)  
			print '\tThe previous state IF(', toStr(path[i].IF) ,', ', toStr(path[i].DIF), ')\n\t\t\t V(', toStr(path[i].V), ', ',toStr(path[i].DV), ') H(', toStr(path[i].V), ', ',toStr(path[i].DV), ') \n\t\t\tPr(', toStr(path[i].V), ', ',toStr(path[i].DV), ') OF(', toStr(path[i].V), ', ',toStr(path[i].DV) ,')'
			print '\tThe consequent state IF(', toStr(path[i+1].IF) ,', ', toStr(path[i+1].DIF), ')\n\t\t\t V(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') H(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') \n\t\t\tPr(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') OF(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV) ,')' 
			
		elif path[i].V != MAX and path[i+1].V == MAX:
			print 'Due to the positive effect of IF on V, which increases the volumn'
			print '\tThe previous state IF(', toStr(path[i].IF) ,', ', toStr(path[i].DIF), ')\n\t\t\t V(', toStr(path[i].V), ', ',toStr(path[i].DV), ') H(', toStr(path[i].V), ', ',toStr(path[i].DV), ') \n\t\t\tPr(', toStr(path[i].V), ', ',toStr(path[i].DV), ') OF(', toStr(path[i].V), ', ',toStr(path[i].DV) ,')'
			print '\tThe consequent state IF(', toStr(path[i+1].IF) ,', ', toStr(path[i+1].DIF), ')\n\t\t\t V(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') H(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') \n\t\t\tPr(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') OF(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV) ,')' 
			
		elif path[i].V != MAX and path[i+1].V != MAX:
			print 'Due to the negative effect of OF on V, which reduced the volumn'
			print '\tThe previous state IF(', toStr(path[i].IF) ,', ', toStr(path[i].DIF), ')\n\t\t\t V(', toStr(path[i].V), ', ',toStr(path[i].DV), ') H(', toStr(path[i].V), ', ',toStr(path[i].DV), ') \n\t\t\tPr(', toStr(path[i].V), ', ',toStr(path[i].DV), ') OF(', toStr(path[i].V), ', ',toStr(path[i].DV) ,')'
			print '\tThe consequent state IF(', toStr(path[i+1].IF) ,', ', toStr(path[i+1].DIF), ')\n\t\t\t V(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') H(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') \n\t\t\tPr(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') OF(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV) ,')' 
			
		else:
			print 'Due to the uncertain impact of both IF and OF on V'
			print '\tThe previous state IF(', toStr(path[i].IF) ,', ', toStr(path[i].DIF), ')\n\t\t\t V(', toStr(path[i].V), ', ',toStr(path[i].DV), ') H(', toStr(path[i].V), ', ',toStr(path[i].DV), ') \n\t\t\tPr(', toStr(path[i].V), ', ',toStr(path[i].DV), ') OF(', toStr(path[i].V), ', ',toStr(path[i].DV) ,')'
			print '\tThe consequent state IF(', toStr(path[i+1].IF) ,', ', toStr(path[i+1].DIF), ')\n\t\t\t V(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') H(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') \n\t\t\tPr(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV), ') OF(', toStr(path[i+1].V), ', ',toStr(path[i+1].DV) ,')' 
			

	# print 'is it empty? ', type(path)
	return path




def  main():
	buildAllStates()
	buildConnections ()
	# draw()
	s = State(ZERO,POS,ZERO,ZERO)
	# ask for a state
	invalid = True
	V = INF
	IF = INF
	DIF = INF
	DV = INF
	while (invalid): 
		x = raw_input ('Input your state in the format V|IF. (notation: M = Max, 0 = Zero, + = Pos, - Neg)\n For example +|0\n')
		v = x[0]
		i = x[2] 
		# di  = x[4]

		# print v, i , di
		invalid = False
		if v == '+':
			V = POS
		elif v == '-':
			invalid = True
		elif v == 'M':
			V = MAX
		elif v == '0':
			V = ZERO
		else:
			invalid = True

		if i == '+':
			IF = POS
		elif i == '-':
			invalid = True
		elif i == 'M':
			invalid = True
		elif i == '0':
			IF = ZERO
		else:
			invalid = True

		# if di == '+':
		# 	DIF = POS
		# elif di == '-':
		# 	DIF = NEG
		# elif di == 'M':
		# 	invalid = True
		# elif di == '0':
		# 	DIF = ZERO
		# else:
		# 	invalid = True

		if invalid:
			print 'Your input is invalid, please input again'
	# print 'creating a state: ', V, ' ', IF, ' ', DIF

	DIFList = []
	DIFSteady = [ZERO]
	DIFIncreasing = [POS, ZERO]
	DIFDecreasing = [NEG, ZERO]
	DIFParabolaPos = [POS, ZERO, NEG]
	DIFParabolaNeg = [NEG, ZERO, POS]
	DIFSinusoidal = [POS, ZERO, NEG, ZERO, POS, ZERO]
	
	valid = False
	while not valid:
		valid = True
		print 'Input the exogenous quantity behaviour as one of the following (must be consistent with your state)'
		x = raw_input ('Steady, Increasing, Decreasing, ParabolaPos, ParabolaNeg, Sinusoidal :\nFor Example: ParabolaPos\n')

		if (x == 'Steady'):
			DIFList = DIFSteady
		elif x == 'Increasing':
			DIFList = DIFIncreasing
		elif x == 'Decreasing':
			DIFList = DIFDecreasing
		elif x == 'ParabolaPos':
			DIFList = DIFParabolaPos
		elif x == 'ParabolaNeg':
			DIFList = DIFParabolaNeg
		elif x == 'Sinusoidal':
			DIFList = DIFSinusoidal
		else: 
			valid = False
			print 'Your input is invalid or in contradictino with the initial state'

	print 'Input complete. Start the reasoning!\n\n'
	DIF = DIFList[0] 

	if IF == POS and V == ZERO:
		DV = POS
	elif IF == ZERO and (V == POS or V == MAX):
		DV = NEG 
	else:
		DV = ZERO

	s = State(IF, DIF, V, DV)


	# # ask for input of DIF:

	# DIFList = [POS,ZERO,NEG,ZERO,POS,ZERO,NEG]
	DIFList2 = []
	DIFList2 = copy.copy(DIFList) # towards a static terminating state

	# print 'DIF list: ', DIFList 
	if DIFList[-1] != ZERO:
		DIFList2.append(ZERO)
	(states, conn, connInter) = trace(s, DIFList2)


	# s = State(ZERO,POS,ZERO,ZERO)
	# # DIFList = [POS, ZERO,NEG,ZERO]
	(states, conn, connInter) = trace(s, DIFList2)
	# drawTrace(states, conn, connInter)
	path =  shortestPath(s, states, conn, connInter, DIFList2)
	# print '\nIn summary, the shortest path found is therefore as follows: '
	# for p in path:
		# print p.toString(), 
	drawShortestPath(states, conn, connInter, path)
	print '\n You will find a graphical representation of this path in your local folder as shortest.gv '
	print 'If you have a viewer of PDF, you may open the file shortest.gv.pdf to view the shortest path'




if __name__ == "__main__":
		main()



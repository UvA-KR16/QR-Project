# Shuai Wang 11108339
# Aashish Venkatesh 11392363

import sys
from graphviz import Digraph
import copy
import numpy
from  calculus import expand_states

ZERO  = 0
POS  = 1
NEG = -1
MAX = 2


INF = 100000000
Connection = []
AllStates = []
index = {}
from tmp import *

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

		global index
		s= 'ID='+ str(index[self.toString()]) +'  '+'IF('

		if self.IF == ZERO:
			s += '0,'
		else:
			s += '+,' 

		if self.DIF == ZERO:
			s += '0)'
		elif self.DIF == POS:
			s += '+)' 
		else:
			s += '-)'

		s += r"\n"

		s += 'V('
		if self.V == ZERO:
			s += '0,'
		elif self.V == POS:
			s += '+,' 
		else:
			s += 'M,' 

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

		if self.DV == ZERO:
			s += '0)'
		elif self.DV == POS:
			s += '+)' 
		else:
			s += '-)'

		s += ' OF('

		if self.V == ZERO:
			s += '0,'
		elif self.V == POS:
			s += '+,' 
		else:
			s += 'M,' 

		if self.DV == ZERO:
			s += '0)'
		elif self.DV == POS:
			s += '+)' 
		else:
			s += '-)'

		return s


def addConnection(i, j, Connection):
	global AllStates
	Connection.append((AllStates[i-1].toString(), AllStates[j-1].toString()))


# simple function to covert a constant to string for printing
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


# validity testing
def isValid(s):
	if s.IF == ZERO and s.DIF == NEG:
		return False
	if (s.V == 0  and s.DV == NEG) or (s.OF == 0 and s.DOF == NEG):
		return False
	return True


# generate the tracing
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

			# obtain the reachable states of s
			reachable_states = expand_states(s)

			for t in AllStates:
				if (s.toString(), t.toString()) in Connection:
					if t.DIF == d:
						# this is the situation that we need to add to the accessible next states
						if t not in CanAccess[i]: 
							CanAccess[i].append(t) 
						toVisit.append(t)
						newConn[i].append((s, t))
			toVisit.remove(s) 
		# prepare the next d
		if (CanAccess[i] != [] and i+1 != len(DIFList)):
			d_next = DIFList[i+1] 
			for s in CanAccess[i]:
				
				# obtain the reachable states of s
				reachable_states = expand_states(s)

				for t in AllStates:
					if (s.toString(), t.toString()) in Connection:
						if t.DIF == d_next:
							if t not in CanAccess[i+1]: 
								CanAccess[i+1].append(t)
							newConnInterLevel[i].append((s, t))
		
		rechableStates[i] = copy.copy(CanAccess[i]) 

	return (rechableStates, newConn, newConnInterLevel)

# this function is only used for our report
def drawTrace (states, conn, connInter):
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


# a simple drawing file
def drawShortestPath(states, conn, connInter, path):
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
	for i in range(len(DIFList)):
		d = DIFList[i]
		# print 'This is level ', i
		# print '\tThere are ', len(states[i]), ' states'
		# print '\tThere are ', len(conn[i]), ' inner connections'
		# print '\tThere are ', len(connInter[i]), ' inter connections'

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
			dis = INF
			for a in toVisit :
				if dis >= m[i][a]:
					dis = m[i][a]
					nextVisit = a
		# next , update the inter level edges if it is not the last level
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
	level = len(DIFList) - 1 
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
	# print out the tracing log
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
			
	return path




def  main():
	buildAllStates()
	buildConnections ()
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
		invalid = False
		# restrictions on input
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

		if invalid:
			print 'Your input is invalid, please input again'

	#some hardcoded values to save time for users
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

	DIFList2 = []
	DIFList2 = copy.copy(DIFList) # towards a static terminating state

	if DIFList[-1] != ZERO:
		DIFList2.append(ZERO)
	(states, conn, connInter) = trace(s, DIFList2)
	path =  shortestPath(s, states, conn, connInter, DIFList2)
	# uncomment this to print the path
	# print '\nIn summary, the shortest path found is therefore as follows: '
	# for p in path:
		# print p.toString(), 
	drawShortestPath(states, conn, connInter, path)
	print '\n You will find a graphical representation of this path in your local folder as shortest.gv '
	print 'If you have a viewer of PDF, you may open the file shortest.gv.pdf to view the shortest path'


if __name__ == "__main__":
		main()



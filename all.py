import sys
from graphviz import Digraph

ZERO  = 0
POS  = 1
NEG = -1
MAX = 2

Expanded = []
ToExpand = []
Connection = []

AllStates = []
ValidStates = []
StableStates = []
UnstableStates =[]

index = 0

class State ():
	# global index
	def __init__(self, IF, DIF, V, DV, OF, DOF):
		global index
		index = index + 1 
		self.index = index + 1
		self.IF = IF
		self.DIF = DIF
		self.V = V
		self.DV = DV
		self.OF = OF
		self.DOF = DOF
		self.string = '' 
		# 'index = ' + str(self.index) + '\n'
		# self.string += 'IF: '
		if IF == ZERO:
			self.string += '0'
		elif IF == POS:
			self.string += '+' 

		# self.string += ' DIF: '
		if DIF == ZERO:
			self.string += '0'
		elif DIF == POS:
			self.string += '+' 
		elif DIF == NEG:
			self.string += '-'

		self.string += '\n'


		# self.string += 'V: '
		if V == ZERO:
			self.string += '0'
		elif V == POS:
			self.string += '+' 
		elif V == MAX:
			self.string += 'M' 

		# self.string += ' DV: '
		if DV == ZERO:
			self.string += '0'
		elif DV == POS:
			self.string += '+' 
		elif DV == NEG:
			self.string += '-'

		self.string += '\n'


		# self.string += 'OF: '
		if OF == ZERO:
			self.string += '0'
		elif OF == POS:
			self.string += '+' 
		elif OF == MAX:
			self.string += 'M'

		# self.string += ' DOF: '
		if DOF == ZERO:
			self.string += '0'
		elif DOF == POS:
			self.string += '+' 
		elif DOF == NEG:
			self.string += '-'

		
# def isStable(s):
# 	if s.IF = ZERO and s.DIF == ZERO and s.V == ZERO and  s.DV == ZERO and s.OF == ZERO and s.DOF == ZERO:
# 		return True
# 	if s.IF == POS and s.DOF == ZERO and s.V = MAX and s.DV == ZERO and s.OF == MAX and s.DOF == ZERO:
# 		return True
# 	if s.IF == POS and s.DOF == NEG and s.V = POS and s.DV == NEG and s.OF == POS and s.DOF == NEG:
# 		return True
# 	if s.IF == POS and s.DOF == POS and s.V = POS and s.DV == POS and s.OF == POS and s.DOF == POS:
# 		return True
	
# 	return False



def isValid(s):
	if s.IF == ZERO and s.DIF == NEG:
		return False
	if (s.V == 0  and s.DV == NEG) or (s.OF == 0 and s.DOF == NEG):
		return False
	return True

	# if s.IF == ZERO  and s.DIF == NEG and s.V == ZERO and s.DV == ZERO  and s.OF = ZERO  and s.DOF == ZERO
	# 	return False

	# if s.IF == ZERO  and s.DIF == NEG and s.V == ZERO and s.DV == POS  and s.OF = ZERO  and s.DOF == POS
	# 	return False

	# if s.IF == ZERO  and s.DIF == NEG and s.V == POS and s.DV == POS  and s.OF = POS and s.DOF == POS
	# 	return False

	# if s.IF == ZERO  and s.DIF == NEG and s.V == MAX and s.DV == ZERO  and s.OF = MAX and s.DOF == ZERO
	# 	return False

	# if s.IF == ZERO  and s.DIF == NEG and s.V == MAX and s.DV == POS  and s.OF = MAX and s.DOF == POS
	# 	return False

	# if s.IF == ZERO  and s.DIF == ZERO and s.V == ZERO and s.DV == POS  and s.OF = ZERO and s.DOF == POS
	# 	return False

	# if s.IF == ZERO  and s.DIF == ZERO and s.V == MAX and s.DV == POS  and s.OF = MAX and s.DOF == POS
	# 	return False

	# if s.IF == ZERO  and s.DIF == POS and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
	# 	return False

	# if s.IF == ZERO  and s.DIF == POS and s.V == ZERO and s.DV == POS  and s.OF = ZERO and s.DOF == POS
	# 	return False

	# if s.IF == POS  and s.DIF == NEG and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
	# 	return False

	# if s.IF == POS  and s.DIF == ZERO and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
	# 	return False

	# if s.IF == POS  and s.DIF == POS and s.V == ZERO and s.DV == ZERO  and s.OF = ZERO and s.DOF == ZERO
	# 	return False


	# if s.IF == POS  and s.DIF = POS and s.V == MAX and s.DV == NEG  and s.OF = MAX and s.DOF == NEG
	# 	return False

	# if s.IF == POS  and s.DIF = POS and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
	# 	return False

# return True


# def addHumanConnections():
# 	for a in StableStates:
# 		if a.DIF == NEG :
# 			s.DIF = ZERO
# 			#add to the stack if valid
# 		if a.DIF == POS :
# 			s.DIF = ZERO
# 		if a.DIF == ZERO:
# 			s1.DIF = POS
# 			s2.DIF = NEG

# def addUnstableConnections():
# 	for a in UnstableStates:
# 		# unstable because of human
# 		if a.DIF == POS and a.IF == ZERO  and a.DV == ZERO :
# 			s.DIF = POS and s.IF = POS and s.DV = POS
# 		if a.DIF == ZERO and a.IF == POS  and a.DV == POS:
# 			s.DIF = ZERO and s.IF = POS and s.DV = NEG

# def addMaxConnnections():
# 	for a in ValidStates:
# 		if a.IF == POS and a.DIF == ZERO and a.V == POS and a.DV == POS and a.OF == POS and a.DOF == POS:
# 			s.V = MAX and s.OF = MAX


def expand (s):
	# TODO by Aashish
	# iplus = 1 * s.IF
	# iminus = -1 * s.OF
	ifValues = []
	dvValues = {}
	dvValues[ZERO] = []
	dvValues[POS] = []
	# vValues = []


	# IF values ---------------------------------------
	if s.IF == ZERO:
		if s.DIF == NEG:
			ifValues = [] #impoossible
		if s.DIF == ZERO:
			ifValues = [ZERO]
		if s.DIF == POS:
			ifValues = [POS]
	if s.IF == POS:
		if s.DIF == NEG:
			ifValues = [POS, ZERO]

		if s.DIF == ZERO:
			ifValues = [POS]
		if s.DIF == POS:
			ifValues = [POS]

 	def V_values(IF, dV, s):
 		if IF==0:
 			V = s.DV + dv 

	# based on our if values: 
	for i in ifValues:
		if (i == ZERO):
			if(s.OF == ZERO):
				dvValues[i].append(ZERO)
			if (s.OF != ZERO):
				dvValues[i].append(NEG)

		elif (i == POS):
			if (s.OF != ZERO):
				if (s.DV == POS):
					dvValues[i].append(POS)
					dvValues[i].append(ZERO)
				elif(s.DV == NEG): 
					dvValues[i].append(NEG)
					dvValues[i].append(ZERO)
				else: # zero
					dvValues[i].append(ZERO)
					dvValues[i].append(POS)
					dvValues[i].append(NEG)
					# dvValues = [ZERO, POS, NEG]
			if (s.OF == ZERO):
				dvValues[i].append(POS)



	
	return (dvValues, ifValues) # return a list of possible states


def possibleStates(IF, DIF, V):
	#TODO by Aashish
	return []

def main (IF, DIF, V):
	global Expanded, ToExpand, Connection
	
	print 'I start a first node now'
	# possStates = possibleStates(IF, DIF, V)
	# ToExpand.append(possStates)
	# while not len(ToExpand) == 0 :
	# 	currentState = ToExpand[0]
	# 	ToExpand.remove (state)
	# 	Expanded.append(state)

	# 	combinations = constraints(s)
	# 	for c in combinations:
	# 		#create a state for each combination
	# 		# s = State(c[0], c[1],c[2],c[3],c[4], c[5], c[6])
	# 		#build up link between currentState and s
	# 		Connection.append(currentState.index, c.index)
	# 		if not(c in ToExpand or c in Expanded):
	# 			ToExpand.append(c)

	# next, illustrate the state-graph
	states = []

	for i in [ZERO, POS]:
		for di in [NEG, ZERO, POS]:
			for v in [ZERO, POS, MAX]:
				for dv in [NEG, ZERO, POS]:
					s = State(i, di, v, dv, v, dv)
					if isValid(s):
						states.append(s)

	print 'You have ', len(states), ' states'


	# s1 = State(0,0,0,0,0,0)
	# s2 = State(0,0,0,0,0,0)
	# s3 = State(0,0,0,0,0,0)

	# Connection.append((s1.index, s2.index))
	# Connection.append((s2.index, s3.index))
	# Connection.append((s3.index, s1.index))
	
	dot = Digraph (comment = 'test')

	for s in states:
		if isValid(s):
			dot.node(str(s.index), s.string)
	s = State(1,0,1,0,1,0)

	# for s in states: 
	(dvValues, ifValues) = expand(s)
	print s.index, s.IF, s.DIF, s.V, s.DV
	for t in states:
		if t.IF in ifValues and t.DV in dvValues[t.IF]:
			s_next = State(t.IF, s.DIF, s.V, t.DV, s.V, t.DV)
			index = s.index
			for tmp in states:
				if s_next.IF == tmp.IF and s_next.DIF == tmp.DIF and s_next.V == tmp.V and s_next.DV == tmp.DV:
					index = tmp.index
			Connection.append((s.index, index))
			dot.edge(str(s.index) , str(index))
	# dot.node(str(s2.index), s2.string)
	# dot.node(str(s3.index), s3.string)

	# dot.edge(str(s2.index) , str(s1.index) , constraint = 'false')
	# dot.edge(str(s2.index) , str(s3.index) , constraint = 'false')
	#next, use graphviz and export the states as images

	dot.render('test.gv', view=True)


if __name__ == "__main__":

	if (len(sys.argv) >2) and sys.argv[1] == '-all':
		print 'this is a graph of all states and their transitions'
	else:
		print '**********************************************************************************'
		print 'please input in the following format: inflow(IF)|derivative of inflow (DIF)|volume'
		print '+ represents positive, - represents negative, 0 represents zero and M represents Max'
		print 'for example: +|-+|+, which means that there is inflow and then it stopped for '
		print '             a while and it continued for a sink with some water in it initially' 
		print '**********************************************************************************'
		description = raw_input('>')
		description = description.split('|')
		print description
		IF = 0
		DIF = []
		V = 0
		if description[0][0] == '+':
			IF = POS
		if description[0][0] == '0':
			IF = ZERO

		for b in description[1]:
			if b == '-':
				DIF.append(NEG)
			if b == '+':
				DIF.append(POS)
			if b =='0':
				DIF.append(ZERO)
		if description[2][0] == '0':
			V = ZERO
		if description[2][0] == 'M':
			V = MAX
		if description[2][0] == '+':
			V = MAX

		main(IF, DIF, V)
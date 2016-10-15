import sys
from graphviz import Digraph

ZERO  = 0
POS  = 1
NEG = 2
MAX = 3

Expanded = []
ToExpand = []
Connection = []

AllStates = []
ValidStates = []
StableStates = []
UnstableStates =[]

index = 0

class State ():
	global index
	def __init__(self, IF, DIF, V, DV, OF, DOF):
		index = index + 1 
		self.index = index + 1
		self.IF = IF
		self.DIF = DIF
		self.V = V
		self.DV = DV
		self.OF = OF
		self.DOF = DOF
		self.string = 'index = ' + str(self.index) + '\n'
		self.string += 'IF: '
		if IF == IFZero:
			self.string += '0'
		elif IF == IFPos:
			self.string += '+' 

		self.string += ' DIF: '
		if DIF == DIFZero:
			self.string += '0'
		elif DIF == DIFPos:
			self.string += '+' 
		elif DIF == DIFNeg:
			self.string += '-'

		self.string += '\n'


		self.string += 'V: '
		if V == VZero:
			self.string += '0'
		elif V == VPos:
			self.string += '+' 
		elif V == VMax:
			self.string += 'M' 

		self.string += ' DV: '
		if DV == DVZero:
			self.string += '0'
		elif DV == DVPos:
			self.string += '+' 
		elif DV == DVNeg:
			self.string += '-'

		self.string += '\n'


		self.string += 'OF: '
		if OF == OFZero:
			self.string += '0'
		elif OF == OFPos:
			self.string += '+' 
		elif OF == OFMax:
			self.string += 'M'

		self.string += ' DOF: '
		if DOF == DOFZero:
			self.string += '0'
		elif DOF == DOFPos:
			self.string += '+' 
		elif DOF == DOFNeg:
			self.string += '-'

		
def isStable(s):
	if s.IF = ZERO and s.DIF == ZERO and s.V == ZERO and  s.DV == ZERO and s.OF == ZERO and s.DOF == ZERO:
		return True
	if s.IF == POS and s.DOF == ZERO and s.V = MAX and s.DV == ZERO and s.OF == MAX and s.DOF == ZERO:
		return True
	if s.IF == POS and s.DOF == NEG and s.V = POS and s.DV == NEG and s.OF == POS and s.DOF == NEG:
		return True
	if s.IF == POS and s.DOF == POS and s.V = POS and s.DV == POS and s.OF == POS and s.DOF == POS:
		return True
	
	return False



def isValid(s):
	if s.IF == ZERO  and s.DIF = NEG and s.V == ZERO and s.DV == ZERO  and s.OF = ZERO  and s.DOF == ZERO
		return False

	if s.IF == ZERO  and s.DIF = NEG and s.V == ZERO and s.DV == POS  and s.OF = ZERO  and s.DOF == POS
		return False

	if s.IF == ZERO  and s.DIF = NEG and s.V == POS and s.DV == POS  and s.OF = POS and s.DOF == POS
		return False

	if s.IF == ZERO  and s.DIF = NEG and s.V == MAX and s.DV == ZERO  and s.OF = MAX and s.DOF == ZERO
		return False

	if s.IF == ZERO  and s.DIF = NEG and s.V == MAX and s.DV == POS  and s.OF = MAX and s.DOF == POS
		return False

	if s.IF == ZERO  and s.DIF = ZERO and s.V == ZERO and s.DV == POS  and s.OF = ZERO and s.DOF == POS
		return False

	if s.IF == ZERO  and s.DIF = ZERO and s.V == MAX and s.DV == POS  and s.OF = MAX and s.DOF == POS
		return False

	if s.IF == ZERO  and s.DIF = POS and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
		return False

	if s.IF == ZERO  and s.DIF = POS and s.V == ZERO and s.DV == POS  and s.OF = ZERO and s.DOF == POS
		return False

	if s.IF == POS  and s.DIF = NEG and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
		return False

	if s.IF == POS  and s.DIF = ZERO and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
		return False

	if s.IF == POS  and s.DIF = POS and s.V == ZERO and s.DV == ZERO  and s.OF = ZERO and s.DOF == ZERO
		return False


	if s.IF == POS  and s.DIF = POS and s.V == MAX and s.DV == NEG  and s.OF = MAX and s.DOF == NEG
		return False

	if s.IF == POS  and s.DIF = POS and s.V == ZERO and s.DV == NEG  and s.OF = ZERO and s.DOF == NEG
		return False

return True


def addHumanConnections():
	for a in StableStates:
		if a.DIF == NEG :
			s.DIF = ZERO
			#add to the stack if valid
		if a.DIF == POS :
			s.DIF = ZERO
		if a.DIF == ZERO:
			s1.DIF = POS
			s2.DIF = NEG

def addUnstableConnections():
	for a in UnstableStates:
		# unstable because of human
		if a.DIF == POS and a.IF == ZERO  and a.DV == ZERO :
			s.DIF = POS and s.IF = POS and s.DV = POS:
		if a.DIF == ZERO and a.IF = POS  and a.DV == POS:
			s.DIF = ZERO and s.IF = POS and s.DV = NEG

def addMaxConnnections():
	for a in ValidStates:
		if a.IF == POS and a.DIF == ZERO and a.V == POS and a.DV == POS and a.OF == POS and a.DOF == POS:
			s.V = MAX and s.OF = MAX


def expand (state):
	# TODO by Aashish
	return [] # return a list of possible states


def possibleStates(IF, DIF, V):
	#TODO by Aashish
	return []

def main (IF, DIF, V):
	global Expanded, ToExpand, Connection
	
	print 'I start a first node now'
	possStates = possibleStates(IF, DIF, V)
	ToExpand.append(possStates)
	while not len(ToExpand) == 0 :
		currentState = ToExpand[0]
		ToExpand.remove (state)
		Expanded.append(state)

		combinations = constraints(s)
		for c in combinations:
			#create a state for each combination
			# s = State(c[0], c[1],c[2],c[3],c[4], c[5], c[6])
			#build up link between currentState and s
			Connection.append(currentState.index, c.index)
			if not(c in ToExpand or c in Expanded):
				ToExpand.append(c)

	# next, illustrate the state-graph

	s1 = State(0,0,0,0,0,0)
	s2 = State(0,0,0,0,0,0)
	s3 = State(0,0,0,0,0,0)

	Connection.append((s1.index, s2.index))
	Connection.append((s2.index, s3.index))
	Connection.append((s3.index, s1.index))
	
	dot = Digraph (comment = 'test')

	dot.node(str(s1.index), s1.string)
	dot.node(str(s2.index), s2.string)
	dot.node(str(s3.index), s3.string)

	dot.edge(str(s2.index) , str(s1.index) , constraint = 'false')
	dot.edge(str(s2.index) , str(s3.index) , constraint = 'false')
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
			IF = IFPos
		if description[0][0] == '0':
			IF = IFZero

		for b in description[1]:
			if b == '-':
				DIF.append(DIFNeg)
			if b == '+':
				DIF.append(DIFPos)
			if b =='0':
				DIF.append(DIFZero)
		if description[2][0] == '0':
			V = VZero
		if description[2][0] == 'M':
			V = VMax
		if description[2][0] == '+':
			V = VMax

		main(IF, DIF, V)
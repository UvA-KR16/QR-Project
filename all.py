import sys
from graphviz import Digraph

IFZero = 0
IFPos = 1

DIFZero = 2
DIFPos = 3
DIFNeg = 4

VZero = 5
VPos = 6
VMax = 7

DVZero = 8
DVPos = 9
DVNeg = 10

OFZero = 11
OFPos = 12
OFMax = 13

DOFNeg = 14
DOFPos = 15
DOFZero = 16

Expanded = []
ToExpand = []
Connection = []



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

		


def isValid(state):
	# TODO
	return False

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
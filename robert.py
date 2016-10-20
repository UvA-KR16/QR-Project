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
		s = str(index) + '\n'

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

		s += '\n'

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

		s += '\n'

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

		s += '\n'
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
	AllStates.append(State(POS, POS, ZERO, ZERO)) # 5
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
def addConnection(i, j):
	global Connection
	global AllStates
	Connection.append((AllStates[i-1].toString(), AllStates[j-1].toString()))

def buildConnections ():
	addConnection(1,2)
	addConnection(2,11)
	addConnection(3,17)
	addConnection(4,5)
	addConnection(5,14)
	addConnection(6,22)
	addConnection(7,6)
	addConnection(7,8)
	addConnection(9,12)
	addConnection(10,13)
	addConnection(12,13)
	addConnection(13,3)
	addConnection(13,7)
	addConnection(13,6)
	addConnection(13,7)
	addConnection(13,14)
	addConnection(13,4)
	addConnection(13,3)
	addConnection(14,7)
	addConnection(15,1)
	addConnection(15,2)
	addConnection(15,16)
	addConnection(16,19)
	addConnection(17,1)
	addConnection(17,15)
	addConnection(17,18)
	# addConnection(17,15)
	addConnection(18,17)
	addConnection(18,19)
	addConnection(18,5)
	addConnection(18,4)
	addConnection(19,18)
	addConnection(20,16)
	addConnection(20,15)
	addConnection(21,19)
	addConnection(22,17)
	addConnection(23,19)
	addConnection(23,18)
	addConnection(23,17)
	addConnection(24,19)

def draw():
	dot = Digraph (comment = 'test2')
	for i in range(len(AllStates)):
		s = AllStates[i]
		dot.node(s.toString(), s.status(i+1))
	for (s, t) in Connection:
		dot.edge(s, t)

	dot.render('test2.gv', view=True)

def  main():
	buildAllStates()
	buildConnections ()
	draw()


if __name__ == "__main__":
		main()



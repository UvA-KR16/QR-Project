import sys

IFZero = 0
IFPos = 1

DIFZero = 2
DIFPos = 3
DIFNeg = 4

VZero = 5
VPos = 6
VMax = 7

OFZero = 8
OFPos = 9
OFMax = 10

OFNeg = 11
OFPos = 6
OFZero = 7

Expanded = []
ToExpand = []
Connection = []



index = 0

class State ():
	global index
	def __init__(self, IF, DIF, V, DV, OF, DOF):
		index = index + 1 
		self.__index = index + 1
		self.__IF = IF
		self.__DIF = DIF
		self.__V = V
		self.__DV = DV
		self.__OF = OF
		self.__DOF = DOF

def isValid(state):
	# TODO
	return False

def constraints (state):
	# TODO by Aashish
	return []


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
			s = State(c[0], c[1],c[2],c[3],c[4], c[5], c[6])
			#build up link between currentState and s
			Connection.append(currentState.index, s.index)
			if not(s in ToExpand or s in Expanded):
				ToExpand.append(s)

	# next, illustrate the state-graph



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
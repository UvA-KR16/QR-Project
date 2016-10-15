
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
	def __init__(self, IF, V, OF):
		index = index + 1 
		self.__index = index + 1
		self.__IF = IF
		self.__V = V
		self.__OF = OF



def constraints (state):
	# TODO by Aashish
	return []



def main ([IF, DIF, V]):
	print 'I start a first node now'
	s = State(IF, DIF, V)
	combinations = constraints(s)
	global Expanded ToExpand Connection
	Expanded = Expanded.append(s)
	for cb in combinations:
		s = State (cb[0], cb[1], cb [2])
	if s in Expanded:
		Connection.append(current.index, s.index)
	if 


if __name__ == "__main__":

	if (sys.argv[1] == '-all')
		print 'this is a graph of all states and their transitions'
	else:
		print '**********************************************************************************'
		print 'please input in the following format: inflow(IF)|derivative of inflow (DIF)|volume'
		print '+ represents positive, - represents negative, 0 represents zero and M represents Max'
		print 'for example: +0+|--+|+, which means that there is inflow and then it stopped for ',
		print '             a while and it continued for a sink with some water in it initially' 
		print '**********************************************************************************'
		description = raw_input('>')
		description = description.split('|')
		print description
		IF = []
		DIF = []
		V = []
		for a in description[0]:
			if a =='+':
				IF.append(IFPos)
			if a == '0':
				DIF.append(IFZero)
		for b in description[1]:
			if b == '-':
				DIF.append(DIFNeg)
			if b == '+':
				DIF.append(DIFPos)
			if b =='0':
				DIF.append(DIFZero)
		if description[2][0] == '0':
			V.append(VZero)
		if description[2][0] == 'M':
			V.append(VMax)
		if description[2][0] == '+':
			V.append(VMax)

	# print IF, ' - ' , DIF, ' - ', V

	main([IF, DIF, V])
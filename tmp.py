from reasoning import *
# some example testing states

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
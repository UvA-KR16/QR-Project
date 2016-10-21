# to generates all the states

# first we define global constants
ZERO  = 0
POS  = 1
NEG = -1
MAX = 2

# define the state class
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

# define the expand function based on a given state, this function returns a list of states
def expand(s):
	ifValues = []
	dvValues = {}
	dvValues[ZERO] = []
	dvValues[POS] = []
	vValues = []
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

	def V_values( dV, s):
 		if s.V == ZERO:
 			if dV == NEG:
 				vValues = []
 			elif dV == ZERO:
 				vValues = [ZERO]
 			else:
 				vValues = [ZERO, POS]

 		if s.V == POS:
 			if dV == NEG:
 				vValues = [POS,ZERO]
 			elif dV == ZERO:
 				vValues = [POS]
 			else:
 				vValues = [MAX, POS]
 			
 		if s.V == MAX:
 			if dV == NEG:
 				vValues = [MAX,POS]
 			elif dV == ZERO:
 				vValues = [MAX]
 			else:
 				vValues = [] 

 		return vValues

	# based on our if values: 
	for i in ifValues:
		if (i == ZERO):
			if(s.V == ZERO):
				dvValues[i].append((ZERO,V_values(ZERO,s)))
			if (s.V != ZERO):
				dvValues[i].append((NEG,V_values(NEG,s)))

		elif (i == POS):
			if (s.V != ZERO):
				if (s.DV == POS):
					dvValues[i].append((POS,V_values(POS,s)))
					dvValues[i].append((ZERO,V_values(ZERO,s)))
				elif(s.DV == NEG): 
					dvValues[i].append((NEG,V_values(NEG,s)))
					dvValues[i].append((ZERO,V_values(ZERO,s)))
				else: # zero
					dvValues[i].append((ZERO,V_values(ZERO,s)))
					dvValues[i].append((POS,V_values(POS,s)))
					dvValues[i].append((NEG,V_values(NEG,s)))
					# dvValues = [ZERO, POS, NEG]
			if (s.V == ZERO):
				dvValues[i].append((POS,V_values(POS,s)))

	return (dvValues, ifValues)

def isValid(s):
	if s.IF == ZERO and s.DIF == NEG:
		return False
	if (s.V == 0  and s.DV == NEG) or (s.V == 0 and s.DV == NEG):
		return False
	return True

def expand_states(s):
	states = []
	(dvValues, ifValues) = expand(s)
	for i in ifValues:
			for dv in dvValues[i]:
				for v in dv[1]:
					if v == 0:
						continue
					else:
						s1 = State(i, s.DIF, v, dv)	
						if isValid(s1):
							states.append(s1)

	return states
from itertools import *
import copy

def unq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

class Symbol:
	nume=None
	def __init__(self,nume):
		self.nume=nume
	def __str__(self):
		return self.nume
	def __eq__(self,other):
		return self.nume==other
	def __repr__(self):
		return self.__str__()

class Rule:
	pleacaDin=None
	pleacaIn=[]
	def __init__(self,start,end):
		self.pleacaDin=start
		self.pleacaIn=end
	def __str__(self):
		s=self.pleacaDin
		s=s+"->"
		for x in self.pleacaIn:
			s=s+x.nume
		return s
	def __repr__(self):
		return self.__str__() 
	def nrOf(self,symbol):
		c=0
		for s in self.pleacaIn:
			if symbol==s:
				c=c+1
		return c

f=open("gramatica.txt",'r')
gramatica=[]
for line in f:
	st=line.rstrip().split('->')
	start=st[0]
	
	for g in st[1].split('|'):
		end=[]
		for l in g:
			end.append(Symbol(l))
		gramatica.append(Rule(start,end))

for x in gramatica:
	print x

delGram=[]
newGram=[]
done=False
print "Gramatica just started:",gramatica
while not done:
	print "------------------------START----------------------------"
	done=True
	for x in gramatica:
		if '*' in x.pleacaIn:
			done=False
			for z in gramatica:
				if x.pleacaDin in z.pleacaIn:
					a=z.nrOf(x.pleacaDin)
					comb=list(product([0,1],repeat=a))
					for co in comb:
						i=0
						d=0
						temp=copy.deepcopy(z.pleacaIn)
						print "Temp:",temp,"Comb:",co
						for s in z.pleacaIn:
							if s==x.pleacaDin:
								if co[i]==0:
									print "Deleted:",temp[d]
									del temp[d]
									d=d-1
								i=i+1
							d=d+1
						print "Temp final:",temp
						if not temp:
							temp=[Symbol('*'),]
						newGram.append(Rule(z.pleacaDin,temp))
						delGram.append(z)
						delGram.append(x)
						delGram=unq(delGram)
					print x.pleacaDin,">>>>>",z,a,comb
	gramatica=gramatica+newGram
	gramatica=[i for i in gramatica if i not in delGram]
	gramatica=unq(gramatica)
	print "-------------------------END--------------------------------"

print "Gramatica partea 1:",gramatica
print "DelGram:",delGram
delGram=[]
for x in gramatica:
	if len(x.pleacaIn)==1 and not x.pleacaIn[0]=='*' and x.pleacaIn[0].nume.isupper() and not x.pleacaIn[0]=="S":
		delGram.append(x)
		for k in gramatica:
			if k.pleacaDin==x.pleacaIn[0]:
				gramatica.append(Rule(x.pleacaDin,k.pleacaIn))
		

	gramatica=[i for i in gramatica if i not in delGram]
	gramatica=unq(gramatica)

print "Gramatica partea 2:",gramatica
surplus=1
for x in gramatica:
	if len(x.pleacaIn)==3:
		newStr="V"+str(surplus)
		newSymb=Symbol(newStr)
		newRule=Rule(newStr,[x.pleacaIn[0],x.pleacaIn[1]])
		surplus=surplus+1
		x.pleacaIn=[newSymb,x.pleacaIn[2]]
		gramatica.append(newRule)

print "Gramatica partea 3:",gramatica
newGram=[]
newRules=[]
for x in gramatica:
	if len(x.pleacaIn)>1:
		for s in x.pleacaIn:
			if s.nume.islower():
				if not "U"+s.nume.lower() in newRules:
					newRules.append("U"+s.nume.lower())
					newGram.append(Rule("U"+s.nume.lower(),[Symbol(s.nume.lower()),]))
				print "Changed:",s.nume,"to","U"+s.nume.lower()
				s.nume="U"+s.nume.lower()


gramatica=gramatica+newGram
gramatica=unq(gramatica)


print "Gramatica finala:",gramatica


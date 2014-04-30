from itertools import *
class Symbol:
	nume=None
	def __init__(self,nume):
		self.nume=nume
	def __str__(self):
		return self.nume
	def __eq__(self,other):
		return self.nume==other

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

for x in gramatica:
	if '*' in x.pleacaIn:
		for z in gramatica:
			if x.pleacaDin in z.pleacaIn:
				print ">>>>>",z


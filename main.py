def stari(word):
	BAD_LETTERS = "1234567890"
	return len([letter for letter in word if letter not in BAD_LETTERS])

f=open("gramatica.txt",'r')
gramatica=dict()
tempg=dict()
i=0
for line in f:
	print line.rstrip()
	st=line.rstrip().split('->')
	gramatica.update({st[0]:st[1]})
print gramatica

# din X->aY in X->AY si A->a
for key in gramatica:
	for s in gramatica[key].split('|'):
		for c in s:
			if c.islower():
				tempg.update({c.upper():c})
				gramatica.update({key:gramatica[key].upper()})
gramatica=dict(gramatica.items() + tempg.items())
print gramatica
tempg=dict()
# 
for key in gramatica:
	for s in gramatica[key].split('|'):
		c=1
		while stari(s)>=3:
			i=str(c)
			print key+i+s[:2]
			gramatica.update({key:key+i+s[-2:]})
			tempg.update({key+i:s[-2:]})
			s = key+i+s[:2]
			c=c+1
			print stari(s),s, gramatica, tempg

print tempg
gramatica=dict(gramatica.items() + tempg.items())
print gramatica

print "DONE"

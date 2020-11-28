import numpy as np
#1-Stone
#2-Paper
#3-Scissor
x=int(input('How many games you want? '))
print('Type 1 for Stone, Type 2 for Paper, Type 3 for Scissor')
i=0
Player=['Stone', 'Paper', "Scissor"]
Computer=['Stone', 'Paper', "Scissor"]
while (i<x):
	P=int(input('Give your Choice: '))
	if (P!=1 and P!=2 and P!=3):
		print('invalid')
	else:
		C=int(np.random.randint(1,4))
		print('Player choose {0}, Computer choose {1}'.format (Player[P-1],Computer[C-1]))
		if(P==1 and C==2) or (P==2 and C==3) or (P==3 and C==1):
			print('Computer gets the point')
		elif(C==1 and P==2) or (C==2 and P==3) or(C==3 and P==1):
			print('Player gets the point')
		else:
			print('Match tied')
	i=i+1


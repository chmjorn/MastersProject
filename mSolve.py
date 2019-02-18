#Matthew Chorney
import random
import sys
import numpy
import copy

popSize=10
maxChromSize=8
maze=[]
pop=[]
scores=[]

def fitnessTrim(maze,unit,startPos): #returns fitness and pos of invalid move if one
	score=0
	trim=0 #position where invalid move is made
	lastM=unit[0] #used to check if changed direction
	end=False #true if go to previous location
	visited=[] #keep track of previous locations and not travel to them again
	pos=copy.deepcopy(startPos)
	visited.append(copy.deepcopy(pos))
	for y in range(len(unit)): #each member solving maze
		if not end: #if didn't go to previous loaction continue
			#if for each direction
			if unit[y]==1: #north
				if canMove(maze,pos,unit[y]):
					pos[0]=pos[0]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y	
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
			elif unit[y]==2: #north east
				if canMove(maze,pos,unit[y]):
					pos[0]=pos[0]-2
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
			elif unit[y]==3: #east
				if canMove(maze,pos,unit[y]):
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
			elif unit[y]==4: #south east
				if canMove(maze,pos,unit[y]):
					pos[0]=pos[0]+2
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
			elif unit[y]==5: #south
				if canMove(maze,pos,unit[y]):
					pos[0]=pos[0]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
			elif unit[y]==6: #south west
				if canMove(maze,pos,unit[y]):
					pos[0]=pos[0]+2
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
			elif unit[y]==7: #west
				if canMove(maze,pos,unit[y]):
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
			elif unit[y]==8: #north west
				if canMove(maze,pos,unit[y]):
					pos[0]=pos[0]-2
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						if y==0:
							trim=1
						else:
							trim=y
						end=True
				else:
					if y==0:
						trim=1
					else:
						trim=y
					break
	return score,trim

def fitnessIgnore(maze,unit,startPos): #returns fitness and ignores bad moves
	#bad defined as trying to move out of maze or somewhere there isn't a path
	score=0
	lastM=unit[0] #used to check if changed direction
	visited=[] #keep track of previous locations and not travel to them again
	pos=copy.deepcopy(startPos)
	lastPos=copy.deepcopy(startPos)
	visited.append(copy.deepcopy(pos))
	for y in range(len(unit)): #each member solving maze
			#if for each direction
			if unit[y]==1: #north
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
			elif unit[y]==2: #north east
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]-2
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
			elif unit[y]==3: #east
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
			elif unit[y]==4: #south east
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]+2
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
			elif unit[y]==5: #south
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]+2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
			elif unit[y]==6: #south west
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]+2
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
			elif unit[y]==7: #west
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)

			elif unit[y]==8: #north west
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]-2
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						score=score+1
						if lastM!=unit[y]:
							score=score-1
						lastM=unit[y]
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
	return score

def crossover(unitOne,unitTwo): #crossover two units
	parOne=copy.deepcopy(unitOne)
	parTwo=copy.deepcopy(unitTwo)
	temp=[]
	if len(parOne)<len(parTwo):
		for x in range(len(parOne)/2):
			temp=parOne[len(parOne)-1-x]
			parOne[len(parOne)-1-x]=parTwo[len(parTwo)-1-x]
			parTwo[len(parTwo)-1-x]=temp
	else:
		for x in range(len(parTwo)/2):
			temp=parTwo[len(parTwo)-1-x]
			parTwo[len(parTwo)-1-x]=parOne[len(parOne)-1-x]
			parOne[len(parOne)-1-x]=temp
	return(parOne,parTwo)

def crossoverOne(unitOne,unitTwo): #crossover returning result of first unit
	parOne=copy.deepcopy(unitOne)
	parTwo=copy.deepcopy(unitTwo)
	temp=[]
	if len(parOne)<len(parTwo):
		for x in range(len(parOne)/2):
			temp=parOne[len(parOne)-1-x]
			parOne[len(parOne)-1-x]=parTwo[len(parTwo)-1-x]
			parTwo[len(parTwo)-1-x]=temp
	else:
		for x in range(len(parTwo)/2):
			temp=parTwo[len(parTwo)-1-x]
			parTwo[len(parTwo)-1-x]=parOne[len(parOne)-1-x]
			parOne[len(parOne)-1-x]=temp
	return(parOne)

def mutation(unit): #takes a chomosome and changes it
	mutate=random.randint(1,4)
	if mutate==1: #add a new move to a random location with higher chance to be same as neighbor
		place=random.randint(0,len(unit)-1) 
		if place==0:
			if len(unit)==1: #check if longer than one
				unit.append(unit[place])
			else:
				unit.insert(place,unit[place+1])
			num=random.randint(1,4)
			if num==1 or num==2:
				unit[place]=random.randint(1,8)
		else:
			unit.insert(place,unit[place-1])
			num=random.randint(1,4)
			if num==1 or num==2:
				unit[place]=random.randint(1,8)
	elif mutate==2 and len(unit)>1: #remove a random move
		del unit[random.randint(0,len(unit)-1)]
	elif mutate==3: #swap two moves
		posF=random.randint(0,len(unit)-1)
		posS=random.randint(0,len(unit)-1)
		temp=unit[posF]
		unit[posF]=unit[posS]
		unit[posS]=temp
	elif mutate==4: #move a section of same moves to another position
		moveSection(unit)
	return unit

def mutationGreedy(unit,score,maze,startPos): #takes a chomosome and changes it only if it isn't worse
	tempUnit=copy.deepcopy(unit)
	mutate=random.randint(1,4)
	if mutate==1: #add a new move to a random location with higher chance to be same as neighbor
		place=random.randint(0,len(tempUnit)-1) 
		if place==0:
			if len(tempUnit)==1: #check if longer than one
				tempUnit.append(tempUnit[place])
			else:
				tempUnit.insert(place,tempUnit[place+1])
			num=random.randint(1,4)
			if num==1 or num==2:
				tempUnit[place]=random.randint(1,8)
		else:
			tempUnit.insert(place,tempUnit[place-1])
			num=random.randint(1,4)
			if num==1 or num==2:
				tempUnit[place]=random.randint(1,8)
	elif mutate==2 and len(tempUnit)>1: #remove a random move
		del tempUnit[random.randint(0,len(tempUnit)-1)]
	elif mutate==3: #swap two moves
		posF=random.randint(0,len(tempUnit)-1)
		posS=random.randint(0,len(tempUnit)-1)
		temp=tempUnit[posF]
		tempUnit[posF]=tempUnit[posS]
		tempUnit[posS]=temp
	elif mutate==4: #move a section of same moves to another position
		moveSection(tempUnit)
	tempScore,garb=fitnessTrim(maze,tempUnit,startPos)
	if tempScore>=score:
		unit=copy.deepcopy(tempUnit)
	return unit

def canMove(maze,pos,direction): #check if can move in desired direction
	if direction==1 and pos[0]>1: #north
		if maze[pos[0]-1][pos[1]]=='|' and maze[pos[0]-2][pos[1]]=='*':
			return True
		else:
			return False
	elif direction==2 and pos[0]>1 and pos[1]<len(maze[pos[0]])-2: #north east
		if maze[pos[0]-1][pos[1]+1]=='/' or maze[pos[0]-1][pos[1]+1]=='X' and maze[pos[0]-2][pos[1]+2]=='*':
			return True
		else:
			return False
	elif direction==3 and pos[1]<len(maze[pos[0]])-2: #east
		if maze[pos[0]][pos[1]+1]=='-' and maze[pos[0]][pos[1]+2]=='*':
			return True
		else:
			return False
	elif direction==4 and pos[0]<len(maze)-2 and pos[1]<len(maze[0])-2: #south east
		if maze[pos[0]+1][pos[1]+1]=='\\' or maze[pos[0]+1][pos[1]+1]=='X' and maze[pos[0]+2][pos[1]+2]=='*':
			return True
		else:
			return False
	elif direction==5 and pos[0]<len(maze)-2: #south
		
		if maze[pos[0]+1][pos[1]]=='|' and maze[pos[0]+2][pos[1]]=='*':
			return True
		else:
			return False
	elif direction==6 and pos[0]<len(maze)-2 and pos[1]>1: #south west
		if 	maze[pos[0]+1][pos[1]-1]=='/' or maze[pos[0]+1][pos[1]-1]=='X' and maze[pos[0]+2][pos[1]-2]=='*':
			return True
		else:
			return False
	elif direction==7 and pos[1]>1: #west
		if maze[pos[0]][pos[1]-1]=='-' and maze[pos[0]][pos[1]-2]=='*':	
			return True
		else:
			return False
	elif direction==8 and pos[0]>1 and pos[1]>1: #north west
		if maze[pos[0]-1][pos[1]-1]=='\\' or maze[pos[0]-1][pos[1]-1]=='X' and maze[pos[0]-2][pos[1]-2]=='*':
			return True
		else:
			return False
	elif direction<1 or direction>8:
		print("canMove ERROR")
		exit()
	else:
		return False

def alterPop(unit): #change some chromeosomes to be like neighbors
	ran=len(unit)/3
	if ran!=0:
		for y in range(ran):
			place=random.randint(1,len(unit)-1)
			unit[place]=unit[place-1]
	return unit

def deleteInvalid(unit,pos): #delete invalid move position on
	end=len(unit)
	for x in range(pos,end):
		unit.pop()
	return unit

def clean(maze,unit,startPos): #a very inefficient function to make fitnessIgnore output more readable
	visited=[] #keep track of previous locations and not travel to them again
	pos=copy.deepcopy(startPos)
	lastPos=copy.deepcopy(startPos)
	visited.append(copy.deepcopy(pos))
	delPos=[] #array of poistions in chomosome to erase
	for y in range(len(unit)): #each member solving maze
			#if for each direction
			if unit[y]==1: #north
				if canMove(maze,pos,unit[y]):
					pos[0]=pos[0]-2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)	
				else:
					delPos.append(y)	
			elif unit[y]==2: #north east
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]-2
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)
				else:
					delPos.append(y)
			elif unit[y]==3: #east
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)
				else:
					delPos.append(y)
			elif unit[y]==4: #south east
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]+2
					pos[1]=pos[1]+2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)
				else:
					delPos.append(y)
			elif unit[y]==5: #south
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]+2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)
				else:
					delPos.append(y)
			elif unit[y]==6: #south west
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]+2
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)
				else:
					delPos.append(y)
			elif unit[y]==7: #west
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)
				else:
					delPos.append(y)
			elif unit[y]==8: #north west
				if canMove(maze,pos,unit[y]):
					lastPos=copy.deepcopy(pos)
					pos[0]=pos[0]-2
					pos[1]=pos[1]-2
					if pos not in visited: #check if previously been to location 
						visited.append(copy.deepcopy(pos))
					else:
						pos=copy.deepcopy(lastPos)
						delPos.append(y)
				else:
					delPos.append(y)
	for x in range(len(delPos),0,-1):
		#print "X ",x," LENGTH ",len(delPos)," DELPOS ",delPos," UNIT ",unit
		del unit[delPos[x-1]]
	return unit

def makePop(pop,popSize,maxChromSize,scores): #create the population
	pop=[] #clear pop
	scores=[] #clear scores
	for x in range(popSize):
		pop.append([])
		for y in range(random.randint(2,maxChromSize)): #make size 2 to maxChromSize
			pop[x].append(random.randint(1,8))
	for x in range(popSize): #add a score for each member of the population
 		scores.append(0)
	return pop,scores

def moveSection(unit): #move a section of the same move to a new location
	pos=random.randint(0,len(unit)-1) #position of section to move
	moves=[] #store locations of same number
	adding=[] #hold section to move
	delStart=pos #start pos for removing from unit
	num=unit[pos] #number of section
	moves.append(pos)
	for x in range(pos+1,len(unit)): #find same move in later positions
		if num==unit[x]:
			moves.append(x)
	for x in range(pos-1,0,-1): #find same move in lower positions
		if num==unit[x]:
			delStart=x
			moves.insert(0,x)
	for x in range(len(moves)): #remove section from unit
		adding.append(num)
		del unit[delStart]
	pos=random.randint(0,len(unit)) #new position to re-add section
	for x in range(len(adding)):
		unit.insert(pos,num)
	return unit

if(len(sys.argv))!=2:
    print("Please input a file name")
    exit()

file_name=sys.argv[1]
		
print "Reading from: ", file_name

file=open(file_name)
height=file.readline()
height=int(height)
width=file.readline()
width=int(width)

for line in file:
        maze.append(line.split())

		
for x in range(height): #adds spaces to fill in gaps
	if len(maze[x])<width:
		y=0
		while y < len(maze[x]):
			if x%2==0:
				if y%2==0 and maze[x][y]=='-':
					maze[x].insert(y,' ')
					y=y+1
				if y%2!=0 and maze[x][y]=='*':
					maze[x].insert(y,' ')
					y=y+1
			else:
				if y%2==0 and (maze[x][y]=='X' or maze[x][y]=='\\' or maze[x][y]=='/'):
					maze[x].insert(y,' ')
					y=y+1
				elif y%2!=0 and maze[x][y]=='|':
					maze[x].insert(y,' ')
					y=y+1
			y=y+1
		if len(maze[x])<width:
			for i in range(len(maze[x]),width):
				maze[x].append(' ')

for x in range(height):	
	print maze[x]
print

limit=1
bestUnit=[1] #keep track of best set of moves
bestScore=0 #bestUnit score
bestStartPos=[0,0] #bestUnit starting position
startPos=[]
startPosLen=0
for x in range(0,height,2): #add every node as a possible starting position
	for y in range(0,width,2):
		startPos.append([x,y])
		startPosLen=startPosLen+1
TRIM=True #do the main loop that trims moves
IGNORE=True #do the main loop that ignores bad moves
if TRIM:
	for starting in range(startPosLen): #for each possible starting position
		pop,scores=makePop(pop,popSize,maxChromSize,scores) #make new random pop between each starting point
		for x in range(popSize):
			alterPop(pop[x])
		print "starting ",startPos[starting]	
		for num in range(limit): #traverse maze
			for x in range(len(pop)): #for everyone in the population
				pop[x]=mutationGreedy(pop[x],scores[x],maze,startPos[starting])
				scores[x],trim=fitnessTrim(maze,pop[x],startPos[starting])
				if trim>0:
					deleteInvalid(pop[x],trim)
				if scores[x]>bestScore or (scores[x]==bestScore and len(pop[x])<len(bestUnit)): #record best ever found or shorter path with same score
					bestUnit=copy.deepcopy(pop[x])
					bestScore=scores[x]
					bestStartPos=startPos[starting]
			scores, pop = (list(h) for h in zip(*sorted(zip(scores, pop)))) #sort lists
			killNum=len(pop)/3
			if num!=limit-1:
				for y in range(killNum): #kill worst part of population
					del pop[0]
					del scores[0]
					if random.randint(0,1)==0: #chance to be random new sequences instead of crossover
						pop.append([])
						for i in range(random.randint(1,maxChromSize)):
							pop[len(pop)-1].append(random.randint(1,8))
						alterPop(pop[len(pop)-1])
					else:
						pop.append(crossoverOne(pop[random.randint(0,killNum)],pop[random.randint(0,killNum)])) #append new made from two existing
					scores.append(0)
					

if TRIM==True and IGNORE==True:
	print ""
	print "Best Moves ",bestUnit
	print "Score ",bestScore
	print "Starting at ",bestStartPos
	print ""
	bestUnit=[]
	bestScore=0
	bestStartPos=[0,0]

if IGNORE:
	for starting in range(startPosLen): #for each possible starting position
		pop,scores=makePop(pop,popSize,maxChromSize,scores) #make new random pop between each starting point
		for x in range(popSize):
			alterPop(pop[x])
		print "starting ",startPos[starting]
		for num in range(limit): #traverse maze
			for x in range(len(pop)): #for everyone in the population
				pop[x]=mutationGreedy(pop[x],scores[x],maze,startPos[starting])
				scores[x]=fitnessIgnore(maze,pop[x],startPos[starting])
				if scores[x]>bestScore or (scores[x]==bestScore and len(pop[x])<len(bestUnit)): #record best ever found or shorter path with same score
					bestUnit=copy.deepcopy(pop[x])
					bestScore=scores[x]
					bestStartPos=startPos[starting]
			scores, pop = (list(h) for h in zip(*sorted(zip(scores, pop)))) #sort lists
			killNum=len(pop)/3
			if num!=limit-1:
				for y in range(killNum): #kill worst part of population
					del pop[0]
					del scores[0]
					if random.randint(0,1)==0: #chance to be random new sequences instead of crossover
						pop.append([])
						for i in range(random.randint(1,maxChromSize)):
							pop[len(pop)-1].append(random.randint(1,8))
						alterPop(pop[len(pop)-1])
					else:
						pop.append(crossoverOne(pop[random.randint(0,killNum)],pop[random.randint(0,killNum)])) #append new made from two existing
					scores.append(0)
	for x in range(len(pop)):
		clean(maze,pop[x],startPos[starting])
	clean(maze,bestUnit,bestStartPos)
print ""
print "Best Moves ",bestUnit
print "Score ",bestScore
print "Starting at ",bestStartPos


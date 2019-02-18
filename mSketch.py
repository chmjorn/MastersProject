
import random 
import numpy 

#must be odd numbers
width=7
height=7



maze = numpy.chararray((width, height)) 

for x in range(height):		#create map
	for y in range(width):
		if (x%2==0):
			if(y%2==0):
				maze[x][y]='*'
			else:
				maze[x][y]='-'
		else:
			if(y%2==0):
				maze[x][y]='|'
			else:
				maze[x][y]='X'
print(maze)
print

for x in range(height):		#remove paths
	for y in range(width):
		if (x%2==0 and y%2!=0 and random.randint(0,3)==0): 
			maze[x][y]=' ' #1/4 chance to replace '-' with ' '

		elif(x%2!=0 and random.randint(0,3)==0):
			if(y%2==0):
				maze[x][y]=' ' #replace '|' with ' '
			else:
				if (random.randint(0,1)):
					maze[x][y]='/'
				else:
					maze[x][y]='\\'

print(maze)


f=open("maze.txt","w")
f.write("%s\n" % height)
f.write("%s\n" % width)
for x in range(height):
	for y in range(width):
		f.write("%s" % maze[x][y])
		f.write(" ")
	f.write("\n")


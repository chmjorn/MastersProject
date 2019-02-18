Both files are written in Python 2

mSketch.py creates the maze/graph that is to be solved and creates a file 
containing it. When run it outputs to the command line first a fully connected 
maze followed the maze with edges missing which is then written to the file.

mSolve.py takes in the file made my mSketch.py as a command line parameter. When 
run it first outputs the maze it is solving. It will then output the position it is
starting from to try and find the best path and cycle through every node. After it 
tries every node it will output the best path and where is started from.

""""
task1 -> convert document into GridObject
             -step 1 -> convert doc into array
             -step 2 -> put values into array
             -step 3 -> probably add functions to Grid class
task2 -> make a main/run() function
task3 -> make check() functions
task4 -> make DO() and UNDO() functions


recursive logic -> getpossible moves () -> this returns an array ['e','w','s','n'] -> this function contains isWall() checks
- does it need to save it's position as an intersection? 
for example, would Grid class have an array that gets modified called branches that says, 
[possible outcomes['e','w','s','n'],and then moves tried[[e], pathwayBack['e,'e','w'] each of these sub list represents a previous intersection
(this would get added to every time a move happens)] -> that way, if it for sure fails, it will go back to the intersection and then try
the next posible outcome. branches will contains all the intersections, 
and the maze solver will only go back to the most recent intersection (the end of the list)

this branches list will not be recursive in and of itself, but it will allow for storing the needed data


             """

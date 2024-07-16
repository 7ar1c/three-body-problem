A super basic euler's method DE solver for a three body problem. </br>
Note that my code sets G (gravitational constant) to 1, and all masses are 1 as well. All plots are done in the center of mass frame (center of mass at origin)
There's three different functions: </br>
  1. 'threebody1' which solves and plots the DE numerically </br>
  2. 'solvethebody' which asks for user inputs of the initial conditions, and then calls the 'threebody1' function based on the inputted conditions </br>
  3. 'animatethebody' which uses Matplotlib FuncAnimation to animate the motion of the bodies (note that this takes a really long time to run, if anyone has any suggestions for efficiency let me know) </br>

I have attached an animation that was done using this code!

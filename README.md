A super basic euler's method DE solver for a three body problem. </br>
Note that my code sets G (gravitational constant) to 1, and all masses are 1 as well. All plots are done in the center of mass frame (center of mass at origin)
There's three different functions: </br>
  1. 'threebody1' which solves and plots the DE numerically </br>
  2. 'solvethebody' which asks for user inputs of the initial conditions, and then calls the 'threebody1' function based on the inputted conditions </br>
  3. 'animatethebody' which uses Matplotlib FuncAnimation to animate the motion of the bodies (note that this takes a really long time to run, if anyone has any suggestions for efficiency let me know) </br>

I have attached an animation that was done using this code! </br>

Update as of 20/10/2024: </br>
</br>
Archived all old code under three-body-archive </br>
Improved numerical integration performance using scipy.integrate </br>
Used manim (which is the coolest library ever) to animate the code (sample mp4 is found under media) </br>

</br>

As of 21/10/2024:  </br>
</br>
Added functionality to render in both OpenGL and Cairo </br>
Used 3D rendering to show a 3D simulation of the problem along with camera frame movement</br>

</br>
Notes: </br>
OpenGL rendering uses GPU and is (much) faster than CPU rendering using Cairo, however a bit of functionality is lost using OpenGL as there are less methods available to some classes currently. </br>
To change between Cairo and OpenGL, use the flag on line 110 of threebody2.py </br>


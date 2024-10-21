import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from manim import *
from manim.opengl import *


def equations(state, t, masses):
    x1, y1, z1, x2, y2, z2, x3, y3, z3, vx1, vy1, vz1, vx2, vy2, vz2, vx3, vy3, vz3 = state ##define state
    m1, m2, m3 = masses ##define masses


    ## Calculate distances between bodies

    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2)
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2)

       # Calculate forces

    fx1 = G * m1 * m2 * (x2 - x1) / r12**3 + G * m1 * m3 * (x3 - x1) / r13**3
    fy1 = G * m1 * m2 * (y2 - y1) / r12**3 + G * m1 * m3 * (y3 - y1) / r13**3
    fz1 = G * m1 * m2 * (z2 - z1) / r12**3 + G * m1 * m3 * (z3 - z1) / r13**3

    fx2 = -G * m1 * m2 * (x2 - x1) / r12**3 + G * m2 * m3 * (x3 - x2) / r23**3
    fy2 = -G * m1 * m2 * (y2 - y1) / r12**3 + G * m2 * m3 * (y3 - y2) / r23**3
    fz2 = -G * m1 * m2 * (z2 - z1) / r12**3 + G * m2 * m3 * (z3 - z2) / r23**3

    fx3 = -G * m1 * m3 * (x3 - x1) / r13**3 - G * m2 * m3 * (x3 - x2) / r23**3
    fy3 = -G * m1 * m3 * (y3 - y1) / r13**3 - G * m2 * m3 * (y3 - y2) / r23**3
    fz3 = -G * m1 * m3 * (z3 - z1) / r13**3 - G * m2 * m3 * (z3 - z2) / r23**3

    # Return velocities and accelerations

    return [vx1, vy1, vz1, vx2, vy2, vz2, vx3, vy3, vz3,
            fx1/m1, fy1/m1, fz1/m1,
            fx2/m2, fy2/m2, fz2/m2,
            fx3/m3, fy3/m3, fz3/m3]


##set ICs

G = 1 ##G = 1 for convenience

## ICs can be edited at will

m1, m2, m3 = 1, 1, 1
x1, y1, z1 = 0, 0.05, 0
x2, y2, z2 = 0, -0.05, 0
x3, y3, z3 = 1, 0, 0
vx1, vy1, vz1 = -np.sqrt(1/(0.2)), 0, 0
vx2, vy2, vz2 = np.sqrt(1/(0.2)), 0, 0
vx3, vy3, vz3 = 0, np.sqrt(3), 0

initial_state = [x1, y1, z1, x2, y2, z2, x3, y3, z3, vx1, vy1, vz1, vx2, vy2, vz2, vx3, vy3, vz3] ## put ICs into a list
masses = [m1, m2, m3] ## put masses into a list
t = np.linspace(0, 20, 1000) ##define time span
solutions = odeint(equations, initial_state, t, args=(masses,)) ##return solutions using odeint

##find center of mass in x, y, and z directions

total_mass = m1 + m2 + m3
com_x = (m1 * solutions[:, 0] + m2 * solutions[:, 3] + m3 * solutions[:, 6]) / total_mass
com_y = (m1 * solutions[:, 1] + m2 * solutions[:, 4] + m3 * solutions[:, 7]) / total_mass
com_z = (m1 * solutions[:, 2] + m2 * solutions[:, 5] + m3 * solutions[:, 8]) / total_mass

# Adjust coordinates to the center of mass frame and create a list[list] for coordinates of each planet

planet1 = [solutions[:, 0] - com_x, solutions[:, 1] - com_y, solutions[:, 2] - com_z]
planet2 = [solutions[:, 3] - com_x, solutions[:, 4] - com_y, solutions[:, 5] - com_z]
planet3 = [solutions[:, 6] - com_x, solutions[:, 7] - com_y, solutions[:, 8] - com_z]


##below is code to use to make a static plot in matplotlib

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(x1, y1, z1, label='Body 1', color='r')
#ax.plot(x2, y2, z2, label='Body 2', color='g')
#ax.plot(x3, y3, z3, label='Body 3', color='b')
#x.set_xlabel('X (m)')
#ax.set_ylabel('Y (m)')
#x.set_zlabel('Z (m)')
#ax.set_title('Three-Body Problem Simulation in 3D')
#ax.legend()
#ax.grid()
#plt.show()

# The following code is a Manim implementation of the above code
# ***All the code below is for the Manim implementation rendered using OpenGL***


class ThreeBody(Scene): ## define a scene called ThreeBody

    def construct(self): ## define the construct method

        ## Create 3D axes

        axes = ThreeDAxes( 
            x_range=[-30, 30],
            y_range=[-30, 30],
            z_range=[-30, 30],
            x_length=10,
            y_length=10,
            z_length=10,
        )


        ## convert coordinates to numpy arrays and transpose for compatibility with OpenGLVMobject

        planet1_points = np.array(planet1).T
        planet2_points = np.array(planet2).T
        planet3_points = np.array(planet3).T

        ## create an OpenGLVGroup and OpenGLVMobjects for each planet
        
        planets = OpenGLVGroup()
        planet1_vmobject = OpenGLVMobject(make_smooth_after_applying_functions=True).set_points_as_corners(axes.point_to_coords(planet1_points))
        planet2_vmobject = OpenGLVMobject().set_points_as_corners(axes.point_to_coords(planet2_points))
        planet3_vmobject = OpenGLVMobject().set_points_as_corners(axes.point_to_coords(planet3_points))
        
        ## set colors for each planet

        planet1_vmobject.set_color(RED)
        planet2_vmobject.set_color(GREEN)
        planet3_vmobject.set_color(BLUE)

        ## add planets to the OpenGLVGroup


        planets.add(planet1_vmobject)
        planets.add(planet2_vmobject)
        planets.add(planet3_vmobject)

        ## create dots to trace the planets

        dot1 = Dot(color=RED)
        dot2 = Dot(color=GREEN)
        dot3 = Dot(color=BLUE)


        dots = Group(dot1, dot2, dot3) #add dots to a group

        def update(dots): ## define an updater function for the dots which moves the dots to the end of the current frame
            dot1.move_to(planet1_vmobject.get_end())
            dot2.move_to(planet2_vmobject.get_end())
            dot3.move_to(planet3_vmobject.get_end())

        dots.add_updater(update) ## add the updater to the dots

        ## create tails for the dots

        tail1 = TracedPath(dot1.get_center, stroke_color=RED, stroke_width=2, dissipating_time=0.5)
        tail2 = TracedPath(dot2.get_center, stroke_color=GREEN, stroke_width=2, dissipating_time=0.5)
        tail3 = TracedPath(dot3.get_center, stroke_color=BLUE, stroke_width=2, dissipating_time=0.5)


        planets.set_opacity(0) ## set the opacity of the line to 0 so tails can dissapear, 
            #this is purely aesthetic and can be removed if desired

        self.add(dots) ## add dots to the scene
        self.add(tail1, tail2, tail3) ## add tails to the scene
        self.add(axes) ## add axes to the scene
        self.play(*(Create(curve, run_time=15) ## play the scene with a runtime of 15 seconds
        for curve in planets), rate_functions=linear)
        self.interactive_embed() ## for rendering in openGL, so we can interact with the scene

        ## to render the scene, run the following command in the terminal:
        ## enable_gui is used to allow for interaction with the scene, and opens an interactive IPython shell
        ## manim threebody2.py -p --renderer=opengl --enable_gui


        ## setting a VSCode task in tasks.json allows for the following command to be run in the terminal using Ctrl+Shift+B
        ## this allows for easy (and effienct) rendering of the scene
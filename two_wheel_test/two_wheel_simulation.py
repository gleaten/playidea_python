import numpy as np
import matplotlib.pyplot as plt

import TwoWheelRobot
import Plotter


args={"SAMPLING_FREQ":10,
      "ROBOT_RADIUS":1,
      "SIMULATION_TIME":100,
      "PLOT_TRAJ":True,
      }


# ImageSequenceClip(images, fps=5).ipython_display()
                
        
if __name__ == "__main__":
    robot = TwoWheelRobot(pos=[0,1],vel=[10,5],head=10)
    plotter = Plotter(robot=robot)
    
    for iter_ in range(args["SIMULATION_TIME"]):
        robot.move()
        robot.sense()
        
        plotter.draw()
        plt.pause(0.01)

        

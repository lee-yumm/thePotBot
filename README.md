# ThePotBot
Final Robotics Source Folder

<img src="https://64.media.tumblr.com/1ccd390771493d256f2ff3fe31ede650/0d8bdb5cb4f54ff5-f9/s400x600/5a046269db0b4b410106ffcefcad29988f19f5e1.png">

The folders shown here are the packages used in the source folder of thepotbot's workspace.

DiffDrive and Serial folders were copied from <a href="https://github.com/joshnewans" target="blank">josh newans</a> repo for driving robot and setting up communications between Arduino Uno and Raspberry Pi.

LdLidar folder refers to the driver for lidar module that can be found <a href="https://github.com/ldrobotSensorTeam/ldlidar_sl_ros2">here</a>.

The pot driver folder contains the driver for the pothole identifying and filling system.  It's an executable python file called "ultrasonic.py", the other ultrasonic python file was an attempt to stop the cmd_vel messages to pause navigation, but to no avail.

The folder entitled "thepotbot" is the main package of thepotbot workspace.  It contains launch files for running nodes, xacro files for translating physical dimensions, and yaml configuration files for processing those xacro descriptions.

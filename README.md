# Maze Navigator 
In this project we calculate the escape path of a given 3D maze for a robot.

### 📷 Detection of 3D-Maze (/detector)
Pictures of a 3D maze from the bottom down perspective are used to then generate maze object, which saves information about shape and structure of the maze. 


### 🧠 Solving maze using reinforcement learning (/solver)
Calculate escape path for current maze for the agents current position using a deterministic reinforcement learning alorithm.


### 📈 Visualisation of maze and learning progress (/visualizer)
Uses PySimpleGUI to graphically represent the detected maze and the position of the agent. Also shows the attractiveness of the cells using coloring and the direct path to take.


### 🤖 Controlling MindStorm EV3 (/controller)
Establishes a Bluetooth connection between a host PC and the EV3 to then send moving instructions.

Used libraries:
(host): mobaXterm (ssh connection to ev3), etcher (ev3 img flasher), ev3dev-stretch, evdev2
(ev3): rpyc (3.3.0), python (3.5.3)

### :computer: Setup
For convenience, we advise to use Conda Virtual Environments.
After installing anaconda, create a new environment using:
`conda create -n <env-name> python=3.5` and activate it using `conda activate <env-name>`.
Now navigate into the project "/MazeSolver" (`cd */MazeSolver`) and  run the command `pip install -r requirements.txt` to automatically install all required libaries.

To run the program, make sure a birds-eye-view picture of a maze is in the `/input` folder. Next boot the ev3 brick and pair it via Bluetooth with the HOst PC, then start mobaxterm to run `bash rpyc_server.sh`. After the server started, run the main python script using `python main.py`

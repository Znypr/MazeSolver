# Modular Maze Navigator


### 📷 Detection of 3D-Maze
using live webcam feed of maze to analyze maze layout
: opencv, numpy, pythonbuildgui

### 🧠 Solving maze using reinforcement learning#
Calculate path of current maze for the agent to take


### 📈 Visualisation of learning progress
using -lib- to show agents actions and progress over time

: opencv, numpy, pythonbuildgui


### 🤖 Controlling MindStorm EV3 to navigate through maze
give moving instructions to agent 

(host): mobaXterm (ssh connection to ev3), etcher (ev3 img flasher), ev3dev-stretch, evdev2
(ev3): rpyc (3.3.0), python (3.5.3)

it is possible to automatically start the server when booting up the ev3 brick. However this is not done here, to be able to see the communication on mobaXterm

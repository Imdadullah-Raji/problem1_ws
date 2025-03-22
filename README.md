# problem1_ws
Controlling a turtlebot3 in gazebo simulation with verbal commands, using ROS Noetic.


Running program. 
1. Requires Ubuntu 20, you can run it on a virtual machine like oracle virtualbox
2. Install ROS Noetic. You find the installation instructions here [https://wiki.ros.org/noetic/Installation/Ubuntu](url)
3. Install gazebo. Open the terminal and run:
     $ sudo apt update
     $ sudo apt install gazebo9
4. INSTALL NECESSARY ADDITIONAL PYTHON MODULES
    RUN
     $ sudo apt update
     $ sudo apt install python3-pip python3-dev portaudio19-dev
     $ pip3 install SpeechRecognition
5. Install turtlebot3 into your Machine. Run the following:

    $ sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
      ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
      ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
      ros-noetic-rosserial-python ros-noetic-rosserial-client \
      ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
      ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
      ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
      ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers

    $ sudo apt install ros-noetic-dynamixel-sdk
    $ sudo apt install ros-noetic-turtlebot3-msgs
    $ sudo apt install ros-noetic-turtlebot3

   See here in more details [https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup](url)

6. Clone the repository into your machine:
    $ git clone https://github.com/Imdadullah-Raji/problem1_ws.git
   
   

# Use a smaller ROS Noetic image
FROM osrf/ros:noetic-desktop

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_WS=/root/catkin_ws

# Install system dependencies and ROS packages
RUN apt-get update && apt-get install -y \
    ros-noetic-gazebo-ros-pkgs \
    ros-noetic-gazebo-ros-control \
    ros-noetic-turtlebot3-simulations \
    python3-pip \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install --no-cache-dir SpeechRecognition pyaudio

# Create workspace and copy your code
WORKDIR $ROS_WS
COPY . $ROS_WS/src/
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && catkin_make"

# Source ROS environment
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN echo "source $ROS_WS/devel/setup.bash" >> ~/.bashrc

# Start with a bash shell
CMD ["bash"]

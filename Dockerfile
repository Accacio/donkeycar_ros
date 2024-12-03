FROM osrf/ros:noetic-desktop-full
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git ros-noetic-moveit ros-noetic-ros-controllers ros-noetic-gazebo-ros-control ros-noetic-rosserial ros-noetic-rosserial-arduino ros-noetic-roboticsgroup-upatras-gazebo-plugins ros-noetic-actionlib-tools python3-pip

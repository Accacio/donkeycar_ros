#!/usr/bin/env bash

tmux new-session -d -s donkeycar

tmux set-option -g mouse on
tmux rename-window roscore
tmux set-option -g -window roscore
tmux send-keys "roscore" Enter

tmux new-window
tmux rename-window IO
tmux send-keys "cd ~/ros_ws/; . devel/setup.bash" Enter
tmux send-keys "sleep 1;roslaunch donkeycar architect_publisher.launch" Enter
tmux split
tmux send-keys "cd ~/ros_ws/; . devel/setup.bash" Enter
tmux send-keys "sleep 1;roslaunch donkeycar ontologenius.launch" Enter
tmux split -h
tmux send-keys "cd ~/ros_ws/; . devel/setup.bash" Enter
tmux send-keys "sleep 1;roslaunch donkeycar overworld.launch" Enter

tmux a

#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws1 || exit 1
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash

timeout 5 ros2 topic echo /keyboard_input std_msgs/msg/String > /tmp/topic.log &
ECHO_PID=$!

sleep 3

printf "hello\nq\n" | ros2 run mypkg talker

wait $ECHO_PID

grep 'hello' /tmp/topic.log && echo OK

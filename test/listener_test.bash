#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws1 || exit 1
colcon build
source $dir/.bashrc

timeout 5 ros2 run mypkg listener 2>&1 | tee /tmp/listener.log &
LISTENER_PID=$!

sleep 1

ros2 topic pub /keyboard_input std_msgs/msg/String "{data: hello}" -1

wait $LISTENER_PID

if grep 'hello' /tmp/listener.log > /dev/null; then
  echo OK
else
  echo NG
  exit 1
fi

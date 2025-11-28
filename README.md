# Robotair Demo Example

Sample application to demonstrate basic Robotair capabilities.
This example is an adaptation of [this](https://github.com/niksacdev/ros2_demo_pubsub) custom pub-sub example.

## Assumptions

- Tested on ROS2 foxy or Galactic build.
- Both Publisher and Subscriber nodes are communicating over `demo_topic`, this can be changed or parameterized in the packages.

## Build Instructions

Use `colcon` to build and then source using the `setup.bash` in Install folder created in your ROS2 workspace.

```bash
# install external ROS repositories
vcs import src < src/robotair_galactic_example/public.rosinstall
# ensure any dependencies are managed before you build
rosdep install -i --from-path src --rosdistro galactic -y 
# build the packages 
colon build
# source install the packages into ROS2
. install/setup.bash
```

## Running the Subscriber node in a ROS2 environment

In a terminal start the Subscriber:

```bash
[ROS2 Workspace Root]>> ros2 run demo_pub demo_pub_node
```

## Running the Publisher node in a ROS2 environment

In another terminal start the Publisher:

```bash
[ROS2 Workspace Root]>> ros2 run robotair_pub robotair_pub_node
```

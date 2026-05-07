#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler

hedefler = [
    (-0.484, -0.481, 0.00247),
    (0.599, -1.66, 0.00247),
    (1.73, 0.547, 0.00247),
    (-0.518, 1.79, -0.0014),
    (-0.361, 0.51, 0.00845)
]

def hedefe_git(x, y, yaw):
    istemci = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    istemci.wait_for_server()

    hedef = MoveBaseGoal()

    hedef.target_pose.header.frame_id = "map"
    hedef.target_pose.header.stamp = rospy.Time.now()

    hedef.target_pose.pose.position.x = x
    hedef.target_pose.pose.position.y = y

    quaternion = quaternion_from_euler(0, 0, yaw)

    hedef.target_pose.pose.orientation.x = quaternion[0]
    hedef.target_pose.pose.orientation.y = quaternion[1]
    hedef.target_pose.pose.orientation.z = quaternion[2]
    hedef.target_pose.pose.orientation.w = quaternion[3]

    rospy.loginfo(f"Hedefe gidiliyor: x={x}, y={y}, yaw={yaw}")

    istemci.send_goal(hedef)

    istemci.wait_for_result()

    rospy.loginfo("Hedefe ulaşıldı")


if __name__ == '__main__':

    rospy.init_node('hedef_gonderici')

    for x, y, yaw in hedefler:
        hedefe_git(x, y, yaw)

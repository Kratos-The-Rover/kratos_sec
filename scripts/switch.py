#! /usr/bin/env python

import rospy
from std_msgs.msg import Bool

rospy.init_node("switch" , anonymous=True)

class Switch():
	def __init__(self, *args, **kwargs):
		self.autonomous = False
		self.manual = True
		self.kill_switch = False
		self.auto_sub = rospy.Subscriber("/auto_mode" , Bool , self.set_auto)
		self.kill_sub = rospy.Subscriber("/kill", Bool , self.set_kill)

	def set_auto(self , msg):
		"""Setting Rover to autonomous mode"""
		self.autonomous = msg.data
		rospy.loginfo("Rover in auto: %r"%self.autonomous)

	def set_kill(self , msg):
		"""Kill rover"""
		self.kill_switch = msg.data
		rospy.logwarn("Killing Rover: %r"%self.kill_switch)

if __name__ == "__main__":
	o=Switch()
	rospy.spin()
	
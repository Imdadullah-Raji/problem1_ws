#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

import math

class Turtle_mover:
    def __init__(self):
        self.command= ''
        #self.pub= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #run on turtlesim_node if gazebo isnt available
        self.pub= rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate= rospy.Rate(10)
        self.battery= 100

    
    def execute_command(self, msg:String):
        self.command = msg.data.strip()
    
        if self.command=='f':
            rospy.loginfo('Moving forward for 2 sec')
            self.forward(2)
        elif self.command== 'f5':
            rospy.loginfo('Moving forward for 5 sec')
            self.forward(5)
        
        elif self.command== 'l':
            rospy.loginfo('Turning left')
            self.turn('l')
        elif self.command== 'r':
            rospy.loginfo('Turning right')
            self.turn('r')
        elif self.command== 'H':
            self.heal()
            
        def forward(self, time:float):
        #moves the turtle forward for 2 s
        start_time = rospy.Time.now().to_sec()
        msg=Twist()
        if self.battery<0:
            rospy.loginfo("Battery Low!")
            return
        while rospy.Time.now().to_sec() - start_time < time:
            msg.linear.x= 1.0
            msg.angular.z=0.0
            self.pub.publish(msg)
            self.rate.sleep()
            
        msg.linear.x = 0.0  # Stop moving
        self.pub.publish(msg)
        self.battery-=time*5
        rospy.loginfo("Current Battery Level:"+str(self.battery))
        
    def turn(self, direction:str):
        
        start_time = rospy.Time.now().to_sec()
        msg=Twist()
        duration= math.pi/2
        if self.battery<0:
            rospy.loginfo("Battery Low!")
            return
        while rospy.Time.now().to_sec() - start_time < duration:
            msg.linear.x= 0
            if direction=='l':
                msg.angular.z=1.0
            else:
                msg.angular.z= -1.0
            
            self.pub.publish(msg)
            
            self.rate.sleep()
        msg.angular.z=0
        self.pub.publish(msg)
        self.battery-=5
        rospy.loginfo("Current Battery Level:"+str(self.battery))


    def heal(self):
        if self.battery+20<=100:
            self.battery+=20
        else :
            self.battery= 100
        rospy.loginfo("Healed +20: current battery-"+str(self.battery))



if __name__=='__main__':
    
    rospy.init_node('control_node')
    turtle_mover= Turtle_mover()
    sub = rospy.Subscriber('/src_to_control', String, callback= turtle_mover.execute_command)

    rospy.spin()
    


    


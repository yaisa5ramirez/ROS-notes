#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def stringListenerCallback(data):
    rospy.loginfo('I heard: %s', data.data)

def subscriber():
    rospy.init_node('node_2', anonymous=False)
    rospy.Subscriber('/topic_1', String, stringListenerCallback)   #el nombre de los topicos siempre inicia con /

    rospy.spin()     #Quedese ahi hasta que reciba un mensaje

if __name__ == '__main__':
    subscriber()

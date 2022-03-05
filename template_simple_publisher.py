#!/usr/bin/env python3

import rospy
from std_msgs.msg import String     

def publisher():
    simple_publisher = rospy.Publisher('/topic_1', String, queue_size=10)     #En este caso el topico solo recibe String
    rospy.init_node('node_1', anonymous=False)   #Anonymus para no repetir nombres
    rate = rospy.Rate(1)      #Rate esta en Hz, en este caso manda 1 mensaje por segundo

    topic1_content = "First ros topic"

    while not rospy.is_shutdown():
        simple_publisher.publish(topic1_content)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

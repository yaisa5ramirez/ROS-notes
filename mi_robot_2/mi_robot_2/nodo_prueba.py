import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial
import time
ser = serial.Serial("/dev/ttyUSB0", baudrate=9600) #Modificar el puerto serie de ser necesario
#dar permiso al puerto sudo chmod 666 /dev/ttyUSB0
global lista_a
lista_a = [0,0]

class RobotCmdVelSubscriber(Node):

    def __init__(self):
        super().__init__('robot_cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            '/robot_cmdVel',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        #mensaje = repr(self.get_logger().info(f"Received cmdVel: linear_x={msg.linear.x}, angular_z={msg.angular.z}"))
        global lista_a
        lineal = int(msg.linear.x)
        angular = int(msg.angular.z)
        lista_n = [lineal, angular]
        if(lista_n != lista_a):
            print(f"{lineal},{angular}\n")
            ser.write(f"{lineal},{angular}\n".encode())
            time.sleep(0.1)
        lista_a = lista_n



def main(args=None):
    rclpy.init(args=args)
    robot_cmd_vel_subscriber = RobotCmdVelSubscriber()
    rclpy.spin(robot_cmd_vel_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

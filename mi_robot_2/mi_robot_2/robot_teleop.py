import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard
from pynput.keyboard import Key, Listener

lin = input("Introduzca la velocidad lineal: ")
ang = input("Introduzca la velocidad angular: ")

class RobotTeleop(Node):

    def __init__(self):

        super().__init__('robot_teleop')
        self.publisher_ = self.create_publisher(Twist, 'robot_cmdVel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.last_key = None

    def on_press(self, key):

        msg = Twist()    

        try:      

            if key.char == "w": #adelante
                msg.linear.x = float(lin)
                msg.angular.z = 0.0
                self.publisher_.publish(msg)
                self.get_logger().info('Adelante')
                self.i += 1        

            elif key.char == "s": #atras

                msg.linear.x = -float(lin)
                msg.angular.z = 0.0
                self.publisher_.publish(msg)
                self.get_logger().info('Atras')
                self.i += 1

            elif key.char == "d": #giro derecha

                msg.linear.x = 0.0
                msg.angular.z = -float(ang)
                self.publisher_.publish(msg)
                self.get_logger().info('Giro derecha')
                self.i += 1

            elif key.char == "a": #giro izquierda

                msg.linear.x = 0.0
                msg.angular.z = float(ang)
                self.publisher_.publish(msg)
                self.get_logger().info('Giro izquierda')
                self.i += 1

        except: 

            print("Tecla deshabilitada")


    def on_release(self, key):

        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info('Stop')
        self.i += 1

    def timer_callback(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()               


def main(args=None):

    rclpy.init(args=args)
    robot_teleop = RobotTeleop()
    rclpy.spin(robot_teleop)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot_teleop.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
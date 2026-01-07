import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class KeyboardListener(Node):
    def __init__(self):
        super().__init__('keyboard_listener')
        self.subscription = self.create_subscription(
            String,
            'keyboard_input',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

        if msg.data == 'q':
            self.get_logger().info('qを受信したので終了')
            rclpy.shutdown()


def main():
    rclpy.init()
    node = KeyboardListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except rclpy.executors.ExternalShutdownException:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

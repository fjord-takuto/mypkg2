import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class KeyboardTalker(Node):
    def __init__(self):
        super().__init__('keyboard_talker')
        self.publisher_ = self.create_publisher(String, 'keyboard_input', 10)
        self.get_logger().info('入力してください（qで終了）')

    def run(self):
        while rclpy.ok():
            try:
                text = input('>> ')
                if text == 'q':
                    self.get_logger().info('終了します')
                    break

                msg = String()
                msg.data = text
                self.publisher_.publish(msg)
                self.get_logger().info(f'Sent: "{text}"')

            except KeyboardInterrupt:
                break


def main():
    rclpy.init()
    node = KeyboardTalker()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

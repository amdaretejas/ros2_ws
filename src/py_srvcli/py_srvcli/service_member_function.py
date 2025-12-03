from example_interfaces.srv import AddTwoInts
from tutorial_interfaces.srv import AddThreeInts # Change

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddThreeInts, 'add_two_ints', self.add_two_ints_callback) # Change

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c  # Change 
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c))  # Change 

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

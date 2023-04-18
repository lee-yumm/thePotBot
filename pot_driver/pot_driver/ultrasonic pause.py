#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import time
import RPi.GPIO as GPIO
from std_msgs.msg import Float32

class UltrasonicNode(Node):
    def __init__(self):
        super().__init__('ultrasonic_node')
        self.publisher_ = self.create_publisher(Float32, 'ultrasonic', 10)
        self.trigger_pin = 18
        self.echo_pin = 24
        self.valve_pin = 16
        self.min_distance = 7  # in cm
        self.timeout = 0.1  # in seconds

        # Initialize GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setup(self.valve_pin, GPIO.OUT)
        GPIO.output(self.valve_pin, GPIO.LOW)

        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        # Send trigger pulse
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)

        # Wait for echo pulse
        pulse_start = time.time()
        pulse_end = time.time()
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            pulse_start = time.time()
            if pulse_start - pulse_end > self.timeout:
                break
        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            pulse_end = time.time()
            if pulse_end - pulse_start > self.timeout:
                break

        # Calculate distance in cm
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        # Close valve by default
        GPIO.output(self.valve_pin, GPIO.LOW)
        self.get_logger().info('Vavle is closed')

        # Open valve if distance is less than minimum
        if distance < self.min_distance:
            GPIO.output(self.valve_pin, GPIO.HIGH)
            self.get_logger().info('Vavle is open')

        # Create message with distance variable
        msg = Float32()
        msg.data = distance
        self.publisher_.publish(msg)

        # Print distance to console
        # self.get_logger().info('Distance: {} cm'.format(distance))
        self.get_logger().info('Publishing: %.2fcm' % msg.data)

    def __del__(self):
        # Cleanup GPIO pins
        GPIO.cleanup()

def main(args=None):
    rclpy.init(args=args)
    ultrasonic_node = UltrasonicNode()
    rclpy.spin(ultrasonic_node)
    ultrasonic_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(2)
print("Diện tích hình tròn:", circle.area())

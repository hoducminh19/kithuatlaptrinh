print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')
import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Hình hoa với các vòng tròn")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

colors = ["red", "green", "blue"]

def draw_flower():
    for i in range(12):
        pen.color(colors[i % 3])
        pen.circle(100)
        pen.right(30)

draw_flower()

pen.hideturtle()
screen.mainloop()

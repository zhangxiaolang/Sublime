import turtle
import time
"""
turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
"""

# 画布Canvas使用
#1.多角形
"""
turtle.color("red","yellow")
turtle.speed(5)
turtle.hideturtle()
turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
time.sleep(1)
turtle.mainloop()
"""

#2.蛇

def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2)  # 直线前进
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)

if __name__ == "__main__":
   turtle.setup(1500, 1400, 0, 0)
   turtle.pensize(30)  # 画笔尺寸
   turtle.pencolor("green")
   turtle.seth(-40)    # 前进的方向
   drawSnake(70, 80, 2, 15)
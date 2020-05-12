"""
    功能：五角星的绘制
"""
import turtle

def main():
    #计数器
    count = 1
    while count <= 5:
        count = count +1
        turtle.forward(100)
        turtle.right(144)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
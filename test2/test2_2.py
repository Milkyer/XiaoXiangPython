"""
    功能：五角星的绘制，循环绘制
"""
import turtle

def draw_pentagram(size):
    # 计数器
    count = 1
    while count <= 5:
        count = count + 1
        turtle.forward(size)
        turtle.right(144)

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50
    while size <= 100:
        draw_pentagram(size)
        size += 10
    turtle.exitonclick()

if __name__ == '__main__':
    main()
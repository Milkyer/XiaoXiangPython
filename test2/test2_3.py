"""
    功能：五角星的绘制，使用迭代功能绘制
"""
import turtle

def draw_recursive_pentagram(size):
    # 迭代绘制五角星
    count = 1
    while count <= 5:
        count = count + 1
        turtle.forward(size)
        turtle.right(144)
    #五角星绘制完，更新参数size
    size += 10
    if size <= 100:
        draw_recursive_pentagram(size)

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50
    draw_recursive_pentagram(size)

    turtle.exitonclick()

if __name__ == '__main__':
    main()
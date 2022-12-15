import turtle
pen = turtle.Turtle()
def drawhuruf (b,n):
    pen.up()
    pen.goto(b,n)
    pen.down()
    pen.pensize(10)
    pen.color('red')
    for x in range (1): 
        pen.speed(1)
        pen.forward(50)
        pen.circle(50,90)
        pen.forward(50)
        pen.circle(50,90)
        pen.forward(50)
        pen.left(90)
        pen.forward(150)
drawhuruf(-10,200)

def drawangka(v,y,z):
    pen.up()
    pen.goto(v,y)
    pen.down()
    pen.color('black')
    for i in range (4):
        pen.forward(z)
        pen.right(90)
        pen.forward(z)

drawangka(-200,0,50)
drawangka(-200,100,50)


     
pen = turtle.Screen().exitonclick()





# def drawangka (j,k):
#     pen.up()
#     pen.goto(j,k)
#     pen.down()
#     for x in range (2):
#         pen.speed(2)
#         pen.circle(40)

# drawangka(-300,-40)

import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.forward(180)
tao.left(120)
tao.forward(130)
tao.left(60)
tao.forward(50)
tao.left(60)
tao.forward(130)
tao.left(30)
tao.forward(150)
tao.left(90)
tao.forward(180)
tao.left(90)
tao.forward(150)

tao.up()
tao.goto(70,-150)
tao.down()
tao.forward(70)
tao.right(90)
tao.forward(40)
tao.right(90)
tao.forward(70)
tao.left(90)

tao.up()
tao.goto(20,-60)
tao.down()
for i in range(4):
    tao.forward(40)
    tao.left(90)

tao.up()
tao.goto(120,-60)
tao.down()
for i in range(4):
    tao.forward(40)
    tao.left(90)

tao.up()
tao.goto(-20,0)
tao.down()

turtle.done

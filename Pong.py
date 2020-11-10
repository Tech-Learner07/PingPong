import turtle
import winsound

win = turtle.Screen()
win.bgcolor("black")
win.title("Pong by @HARI")
win.setup(width=800, height=600)
win.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.penup()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)
paddle_a.color("white")
paddle_a.speed(0)

paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)
paddle_b.color("white")
paddle_b.speed(0)

ball = turtle.Turtle()
ball.shape("square")
ball.goto(0, 0)
ball.color("white")
ball.speed(0)
ball.penup()
ball.dx = 0.2
ball.dy = 0.2

pen = turtle.Turtle()
score_a = 0
score_b = 0
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1 : {} | Player 2 : {}".format(score_a, score_b), align="center", font=("Arial", 18, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while True:
    win.update()
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("boing.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("boing.wav", winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1 : {} | Player 2 : {}".format(score_a, score_b), align="center", font=("Arial", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1 : {} | Player 2 : {}".format(score_a, score_b), align="center", font=("Arial", 18, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)

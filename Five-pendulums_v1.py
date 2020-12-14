import turtle
import time
wn=turtle.Screen()
wn.setup(1200,900)
wn.bgpic('five_pend.gif')
turtle.tracer(2)
t=turtle.Turtle('turtle')
t.hideturtle()
t.color('blue')
t.penup()
t.begin_poly()
t.fd(400)
t.left(90)
t.circle(30.358)
t.fd(4)
t.left(90)
t.fd(400)
t.end_poly()
wn.addshape('pend',t.get_poly())

t1=turtle.Turtle(shape='pend')
t1.up()
t1.color('blue')
t1.showturtle()

t2=t1.clone()
t2.goto(-120,0)
t2.showturtle()

t3=t1.clone()
t3.goto(120,0)
t3.showturtle()

t4=t1.clone()
t4.goto(-60,0)
t4.showturtle()

t5=t1.clone()
t5.goto(60,0)
t5.showturtle()

FONT=('Times New Roman',20,'bold')
angle=float(wn.textinput('Oscillations of a pendulum',\
                         'Enter the deflection angle'))
angle=-angle
if angle>0:
    t2.right(angle)
    
if angle<0:
    t3.right(angle)
q=0
N=110
def motion(turtle1,turtle2):
    q=0
    for i in range(N):
            q=0.01*i*angle/60
            turtle1.lt(q)
            time.sleep(0.01)

    q1=q
    for i in range(N):
        q2=q1-0.01*i*angle/60
        turtle2.lt(q2)
        time.sleep(0.01)
    q3=0    
    for i in range(N):
        q3=0.01*i*angle/60
        turtle2.lt(-q3)
        time.sleep(0.01)
        
    q4=q3
    for i in range(N):
        q5=q4-0.01*i*angle/60
        turtle1.lt(-q5)
        time.sleep(0.01)
    q=0
    
while True:
    if angle<0:
        motion(t3,t2)
    if angle>0:
        motion(t2,t3)


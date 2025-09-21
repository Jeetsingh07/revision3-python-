#print("hello world")
import turtle
import colorsys
t= turtle. Turtle ()
s= turtle. Screen(). bgcolor('green')
t.speed(0)
n=10
h=0
for i in range (720):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left
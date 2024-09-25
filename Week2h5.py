import turtle

t = turtle.Turtle()
turtle.speed(10)

hoek = 20 
stappen = 100 

for i in range(stappen):
    t.fd(i * 2)  
    t.lt(hoek)   

turtle.done() 
 
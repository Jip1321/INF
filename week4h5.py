import turtle

def uitvoeren(regel):
    commando = regel[0]  
    argument = regel[1:].strip('\n') 
    
    match commando:
        case 'f':  
            t.forward(float(argument))
        case 'b': 
            t.backward(float(argument))
        case 'l':  
            t.left(float(argument))
        case 'r':  
            t.right(float(argument))
        case 'o':  
            
            if ',' in argument:
                radius, color = argument.split(',')
                t.dot(float(radius), color)
        case 's':  
            t.begin_fill()
        case 'e':  
            t.end_fill()
        case 'p': 
            t.pencolor(argument)
        case 'i':  
            t.fillcolor(argument)
        case 'c':  
            if ',' in argument:
                rad, deg = argument.split(',')
                t.circle(float(rad), float(deg))
        case 'u':  
            t.up()
        case 'd':  
            t.down()
        case 'g':  
            if ',' in argument:
                x, y = argument.split(',')
                t.goto(float(x), float(y))
        case _:
            print(f"Onbekend commando: {commando}")


turtle.speed(10)
s = turtle.getscreen()
t = turtle.Turtle()


with open("tekening2.txt", "r") as file:
    while regel := file.readline():
        uitvoeren(regel)

turtle.mainloop()

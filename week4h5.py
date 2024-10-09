import turtle as t

def uitvoeren(regel):
    commando = regel[0]
    argument = regel[1:].strip()

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
            radius, color = argument.split(',')
            t.color(color)
            t.circle(float(radius))
        case 'c':
            t.color(argument)
        case 's':
            t.penup()
        case 'd':
            t.pendown()
        case 'g':
            x, y = map(float, argument.split(','))
            t.goto(x, y)
        case 'p':
            t.begin_fill()
        case 'e':
            t.end_fill()
        case _:
            print(f"Onbekend commando: {commando}")

def main():
    t.speed(10)
    with open('tekeningen2.txt', 'r') as file:
        for regel in file:
            if regel.strip():  # Check if the line is not empty
                uitvoeren(regel)
    t.done()

if __name__ == "__main__":
    main()

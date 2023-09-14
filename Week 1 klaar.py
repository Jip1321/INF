import turtle

# volledig onnodig om dit in een functie met variable te zetten
# ziet er wel geordend uit
def turtle_zetten():
    t = turtle.Turtle()
    t.pensize(3)
    t.pencolor("blue")
    t.fillcolor("blue")
    return t
# functie voor turtle cursor waar het heen moet/ waar het heen gaat
def hartje(turtle_instance):
    turtle_instance.penup()
    turtle_instance.goto(0, -200)
    turtle_instance.pendown()

    turtle_instance.begin_fill()
    turtle_instance.left(50)
    turtle_instance.forward(133)
    turtle_instance.circle(50, 200)
    turtle_instance.right(140)
    turtle_instance.circle(50, 200)
    turtle_instance.forward(133)
    turtle_instance.end_fill()

    turtle_instance.hideturtle()

# functie status machine ofwel main waar alle waardes bijelkaar komen
def main():
    t = turtle_zetten()
    hartje(t)
    turtle.done()

# hieronder is in principe hetzelfde als print() maar inplaats van alles binnen () refereer ik naar de main functie erboven
if __name__ == "__main__":
    main()


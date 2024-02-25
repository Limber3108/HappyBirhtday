import turtle

wn = turtle.Screen()
wn.title("PT projects")
wn.bgcolor("lightgreen")  # Cambiamos el color de fondo a verde agua

t = turtle.Turtle()
t.shape("circle")

# Plato para la tarta
t.penup()
t.setpos(-300, -50)

t.speed(1)
t.begin_fill()
t.fillcolor("#79b6c9")  # Cambiamos el color del plato a un tono de rosa
t.forward(600)
t.left(90)
t.forward(10)
t.left(90)
t.forward(600)
t.left(90)
t.forward(10)
t.end_fill()

t.left(180)
t.forward(20)
t.right(90)
t.forward(100)
t.left(90)

# Piso de la tarta
t.begin_fill()
t.fillcolor("#522719")  # Cambiamos el color del piso a un tono de rosa
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.end_fill()

t.left(180)
t.forward(100)
t.left(90)
t.forward(50)
t.right(90)

# Capa media de la tarta
t.begin_fill()
t.fillcolor("#ff4000")  # Cambiamos el color de la capa media a un tono de melocotón
t.forward(100)
t.left(90)
t.forward(300)
t.left(90)
t.forward(100)
t.end_fill()

t.left(180)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)

# Capa superior de la tarta
t.begin_fill()
t.fillcolor("#ADD8E6")  # Cambiamos el color de la capa superior a un tono de azul claro
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.end_fill()
t.pendown()

# Dibujar las velas pequeñas
t.penup()
t.setpos(140, 120)
t.color("#9400d3")  # Cambiamos el color del texto a negro
style = ("Arial", 13, "italic")
t.write("FELIZ CUMPLEAÑOS JIMENA :D", font=style, align="Right")

# Nombre del cumpleañero
t.penup()
t.setpos(100, 100)
t.color("black")  # Cambiamos el color del texto a negro
style = ("Times New Roman", 15, "italic")
t.write("IG:limberv17", font=style, align="Right")

t.hideturtle()
turtle.done()
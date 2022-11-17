import turtle


def draw_square(tu, toa_do, w):
    tu.penup()
    tu.goto(toa_do)
    tu.pendown()
    
    for i in range(4):
        t.forward(w)
        t.right(90)
        
        
def draw_triangle(tu, toa_do, canh):
    tu.penup()
    tu.goto(toa_do)
    tu.pendown()
    tu.circle(-canh, steps = 3)
    

    
def draw_polygon(tu, toa_do, n , canh = 100):
    angle = (n-2)*180/n
    for i in range(n):
        tu.forward(canh)
        tu.left(180-angle)
    
def draw_rectangle(tu, toa_do, canh_ngang, canh_doc, mau):
    tu.penup()
    tu.goto(toa_do)
    tu.pendown()
    tu.fillcolor(mau)
    tu.begin_fill()
    
    for i in range(2):
        tu.forward(canh_ngang)
        tu.right(90)
        tu.forward(canh_doc)
        tu.right(90)
        
        tu.end_fill()
        
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor("red")

#square_draw(t, (-100,200), 200)

#square_draw(t, (-30, 60), 60)

#triangle_draw(t, (-150, -187), 100)

#polygon_draw(t, (-100, -200), 3, 150)

draw_rectangle(t, (-90, 150), 90, 150, "pink")
draw_rectangle(t, (-60, 100), 30, 50, "white")

draw_rectangle(t, (0, 150), 90, 150, "pink")
draw_rectangle(t, (30, 100), 30, 50, "white")

draw_rectangle(t, (-90, 0), 90, 150, "pink")
draw_rectangle(t, (-60, -50), 30, 50, "white")

draw_rectangle(t, (0, 0), 90, 150, "pink")
draw_rectangle(t, (30, -50), 30, 50, "white")

draw_rectangle(t, (90, 0), 100, 150, "grey")

draw_rectangle(t, (150, -75), 30, 75, "green")
draw_rectangle(t, (100, -75), 30, 75, "green")


turtle.done()

               

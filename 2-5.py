import turtle,time
t1 = turtle.Turtle()

win = turtle.Screen()
win.title("my window")
win.bgcolor("white")
t1.color("violet")
t1.shape("turtle")
t1.forward(100)
time.sleep(1)
t1.left(90)

polygom=turtle.Turtle()

num_sides = int(input("要畫幾邊形(3-10)?"))
side_length = 70

angle = 360.0 / num_sides

for i in range(num_sides):
    polygom.forward(side_length)
    polygom.right(angle)
    time.sleep(1)
    
turtle.done()
    
    


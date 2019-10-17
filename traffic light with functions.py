from graphics import *

win= GraphWin("Traffic light" , 200, 200)

def draw_light_body(x, y, length, width):
    light_body = Rectangle(Point(x,y), Point(width, length))
    light_body.setOutline("black")
    light_body.setFill("white")
    light_body.draw(win)

def draw_lamp(color, x, y, radius):
    lamp = Circle(Point(x, y), radius)
    lamp.setOutline("black")
    lamp.setFill(color)
    lamp.draw(win)

def draw_traffic_light(x, y):
    draw_light_body(70, 10, 100, 30)
    draw_lamp("red", 50,30.5, 7)
    draw_lamp("yellow", 50,49.5, 7)
    draw_lamp("green", 50,68.5, 7)
draw_traffic_light(70,10)
                     
    
    


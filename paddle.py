from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.create_paddle(coordinates)
        
        
    def create_paddle(self, coordinates):
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.penup()
        self.setposition(coordinates)
            
    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(y= new_y, x = self.xcor())
    
    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(y= new_y, x = self.xcor())
            

import turtle
import random

screen=turtle.Screen()
screen.bgcolor("black")

pen= turtle.Turtle()
pen.speed(0)
pen.tracer(100,100)

size = 10

while(True):
  red = random.randint(0,255)
  green =random.randint(0,255)
  blue = random.randint(0,255)
  pen.color(red,green,blue)
  
  pen.forward(size)
  pen.right(45)
  pen.forward(size)
  pen.right(45)
  pen.forward(size)
  pen.right(91)
  pen.forward(size)
  size += 1





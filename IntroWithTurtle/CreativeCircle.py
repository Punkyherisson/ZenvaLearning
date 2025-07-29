'''Create a pattern or image using at least three different shapes and three different colors.
 You can use circles, squares, triangles, or any combination of shapes you’ve learned so far.
  Arrange them in any way you like to create a unique and colorful piece of art.'''
from turtle import *
color('blue')
begin_fill
circle(50)  # Draw a circle with radius 50 
end_fill() 
forward(100)  # Move forward 100 pixels
color('green')  
begin_fill()
forward(100)  
left(90)
forward(100)  # Draw a square with side length 100  
end_fill()
done()

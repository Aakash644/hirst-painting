from secrets import choice
import turtle 
import random
import colorgram  
from turtle import Turtle as t, Screen  
#tom=t.Screen()
tim=t()  
turtle.colormode(255)
# rgb_colors=[]
# colors=colorgram.extract('dot.jpg',30)                   
# for color in colors: 
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b 
#     new_color=(r,g,b)
#     rgb_colors.append(new_color) 

    
color_list=[(233, 233, 232), (231, 233, 237), (235, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 
203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (195, 79, 72), (161, 201, 219), (45, 74, 77), (79, 74, 44), (57, 126, 122), (218, 175, 187), (168, 206, 169), (220, 182, 168)]       
tim.speed("fastest") 
tim.penup()
tim.setheading(225)
tim.forward(300) 
for j in range(5):
    tim.setheading(0) #1
    for i in range(10):
       tim.dot(20,random.choice(color_list))
       tim.forward(50) 
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)#2
    for i in range(10):
       tim.dot(20,random.choice(color_list))
       tim.forward(50)  
    tim.setheading(90)
    tim.forward(50)

turtle.exitonclick()

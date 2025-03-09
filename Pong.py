"""
Name: Ping Pong Game In Python
Author: Saeed Soukiah
Date: March 10, 2025
"""

import turtle
import winsound
import pygame

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Saeed Soukiah\Documents\VS Code\Python\Pong\background_music.mp3")  
pygame.mixer.music.set_volume(0.2)  # Set the volume to 20%
pygame.mixer.music.play(-1)  # Loop indefinitely

# Initialize Screen
wind = turtle.Screen() 
wind.title("Ping Pong") 
wind.bgcolor("black") 
wind.setup(width=800, height=600) 
wind.tracer(0)

# Ping 1
madrab1 = turtle.Turtle() 
madrab1.speed(0) 
madrab1.shape("square") 
madrab1.color("blue") 
madrab1.shapesize(stretch_wid=5, stretch_len=1) 
madrab1.penup() 
madrab1.goto(-350, 0)

# Ping 2 (AI Opponent)
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5
speed_increment = 0.01

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("White")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))
winning_score = 5

# Functions for Player 1 movement
# Functions for Player 1 movement (improved)
def madrab1_up():
    y = madrab1.ycor()
    if y < 250:  # Prevent the paddle from going off the top edge
        y += 20
    madrab1.sety(y)
    
def madrab1_down():
    y = madrab1.ycor()
    if y > -250:  # Prevent the paddle from going off the bottom edge
        y -= 20
    madrab1.sety(y)

# Keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "Up")
wind.onkeypress(madrab1_down, "Down")

# Main game loop
while True:
    wind.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Border Collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1} Player 2: {score2}", align="center", font=("Courier", 24, "normal"))
        pygame.mixer.music.pause()
        winsound.PlaySound(r'C:\Users\Saeed Soukiah\Documents\VS Code\Python\Pong\score.wav', winsound.SND_ASYNC)
        pygame.mixer.music.unpause()
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1: {score1} Player 2: {score2}", align="center", font=("Courier", 24, "normal"))
        pygame.mixer.music.pause()
        winsound.PlaySound(r'C:\Users\Saeed Soukiah\Documents\VS Code\Python\Pong\score.wav', winsound.SND_ASYNC)
        pygame.mixer.music.unpause()

    # Game Over Condition
    if score1 == winning_score:
        score.clear()
        score.write("Player 1 WINS!", align="center", font=("Courier", 30, "bold"))
        break
    elif score2 == winning_score:
        score.clear()
        score.write("Player 2 WINS!", align="center", font=("Courier", 30, "bold"))
        break
    
    # Paddle and Ball Collision
    if (340 < ball.xcor() < 350) and (madrab2.ycor() - 40 < ball.ycor() < madrab2.ycor() + 40):
        ball.setx(340)
        ball.dx *= -1
        pygame.mixer.music.pause()
        winsound.PlaySound(r'C:\Users\Saeed Soukiah\Documents\VS Code\Python\Pong\paddle_hit.wav', winsound.SND_ASYNC)
        pygame.mixer.music.unpause()
        ball.dx *= (1 + speed_increment)
        ball.dy *= (1 + speed_increment)
        
    if (-350 < ball.xcor() < -340) and (madrab1.ycor() - 40 < ball.ycor() < madrab1.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1
        pygame.mixer.music.pause()
        winsound.PlaySound(r'C:\Users\Saeed Soukiah\Documents\VS Code\Python\Pong\paddle_hit.wav', winsound.SND_ASYNC)
        pygame.mixer.music.unpause()
        ball.dx *= (1 + speed_increment)
        ball.dy *= (1 + speed_increment)

    # AI Opponent Logic (madrab2)
    if madrab2.ycor() < ball.ycor() and abs(madrab2.ycor() - ball.ycor()) > 10:
        madrab2.sety(madrab2.ycor() + 10)
    elif madrab2.ycor() > ball.ycor() and abs(madrab2.ycor() - ball.ycor()) > 10:
        madrab2.sety(madrab2.ycor() - 10)

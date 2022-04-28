#importo librerias 
from shutil import move
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#screen crea el escenario

#crear escenario; instanciar es tomar todas las variables de un objeto
screen=Screen() #instancia el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("programate snake")

#desactiva el efecto de la animacion 
screen.tracer(0)

#se crea o instnancia el objeto snake, food y scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#se realiza los movimientos del snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


#creo una variable con el estado para el juego 
game_is_on = True

while game_is_on:

    #refresca la pantalla
    screen.update()
    #tiempo o velocidad en el que programo la animacion 
    time.sleep(0.2)

    #Se llama del archivo snake la funcion move
    snake.move()
    
    #Se detecta la colision con la comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Detectar las paredes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detectar la colision de la cola 
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


#parte final del codigo 
screen.exitonclick()



from turtle import Turtle

ALING = "center"
FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 #atributo caracteristiccas 
        self.goto(0, 270) 
        #color del tipo de la letra
        self.color("white")
        self.update_score()
        self.hideturtle()

    #esta funcion le da el estilo a la letra tipo, tamaño y estilo (cursiva, negrita, etc)
    def update_score(self):
        self.write(f"El puntaje es: {self.score}",font= FONT, align=ALING)

    #se crea un metodo de incrementacion 
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Juego terminado",font= FONT, align=ALING)




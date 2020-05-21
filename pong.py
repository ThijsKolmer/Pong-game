import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"

class MenuScreen():
    #hier in staat alle informatie van het menuscherm.
    #in de INIT staan alle acties en belangrijke dingen
    def __init__(self):
        self.position_x = None
        self.position_y = None
        self.width = None
        self.height = None
        self.color = None

        self.start_position_x = None
        self.start_position_y = None
        self.start_color = None
        self.font_size = None

        self.start_2_position_x = None
        self.start_2_position_y = None
        self.start_2_color = None
        self.font_size_2 = None

        self.disappear = False
        
    #in de setup krijgt alles een naam
    def setup(self, position_x, position_y, width, height, color, start_position_x, start_position_y, start_color, font_size, start_2_position_x, start_2_position_y, start_2_color, font_size_2):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color

        self.start_position_x = start_position_x
        self.start_position_y = start_position_y
        self.start_color = start_color
        self.font_size = font_size

        self.start_2_position_x = start_2_position_x
        self.start_2_position_y = start_2_position_y
        self.start_2_color = start_2_color
        self.font_size_2 = font_size_2
    
    #hier wordt alles getekend
    #ook staat hier wat er op het start scherm moet staan
    def on_draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)
        arcade.draw_text(f"Welkom bij mijn Pong Game, je speelt met de W en de S toets. W is omhoog en S is omlaag.", self.start_position_x, self.start_position_y, self.start_color, self.font_size)
        arcade.draw_text(f"Het is heel leuk. Veel speelplezier. Druk op ENTER om te starten. Gemaakt door Thijs", self.start_2_position_x, self.start_2_position_y, self.start_2_color, self.font_size_2)

    #on_update zegt eigenlijk dat hier de bewegingen en dingen die veranderen plaats vinden
    def on_update(self):
        if self.disappear == True:
            self.position_x = 2000
            self.position_y = 2000
            self.start_position_x = 2000
            self.start_position_y = 2000
            self.start_2_position_x = 2000
            self.start_2_position_y = 2000


#hier staat alles over het rechter scorebord
class RightScoreBoard():
    def __init__(self):
        self.position_x = None
        self.position_y = None
        self.font_size = None
        self.color = None

        self.score = None


    def setup(self, position_x, position_y, font_size, color, score):
        self.position_x = position_x
        self.position_y = position_y
        self.font_size = font_size
        self.color = color

        self.score = score


    def on_draw(self):
        arcade.draw_text(f"Score: {self.score}", self.position_x, self.position_y, self.color, self.font_size)

#hier staat alles over het linker scorebord
class LeftScoreBoard():
    def __init__(self):
        self.position_x = None
        self.position_y = None
        self.font_size = None
        self.color = None

        self.score = None


    def setup(self, position_x, position_y, font_size, color, score):
        self.position_x = position_x
        self.position_y = position_y
        self.font_size = font_size
        self.color = color

        self.score = score

    #hier staat wat er op het scorebord moet staan
    def on_draw(self):
        arcade.draw_text(f"Score: {self.score}", self.position_x, self.position_y, self.color, self.font_size)

#hier staat alles over de bal   
class Ball():

    def __init__(self):
        self.position_x = None
        self.position_y = None
        self.radius = None
        self.color = None

        self.delta_x = None
        self.delta_y = None

    def setup(self, position_x, position_y, radius, color, delta_x, delta_y):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

        self.delta_x = delta_x
        self.delta_y = delta_y

    def on_draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


    def on_update(self, delta_time, leftscore_board, rightscore_board, leftpaddle, rightpaddle):
        self.position_x = self.position_x + self.delta_x * delta_time
        self.position_y = self.position_y + self.delta_y * delta_time

        #als we de bovenkant raken, zet de beweegrichting naar beneden
        if self.position_y + self.radius >= SCREEN_HEIGHT:
            self.delta_y = self.delta_y * -1
        
        if self.position_y <= 12.5:
            self.delta_y = self.delta_y * -1
        
        if self.position_x + self.radius >= SCREEN_WIDTH:
            self.delta_x = self.delta_x * -1
            leftscore_board.score += 1
            self.reset()

        if self.position_x <= 12.5:
            self.delta_x = self.delta_x * -1
            rightscore_board.score += 1
            self.reset()

        # als inkerkant bal kleiner of gelijk aan rechterkant paddle EN rechterkant bal groter of gelijk aan linkerkant paddle

        if self.position_x - self.radius <= leftpaddle.position_x + leftpaddle.width / 2 and self.position_x + self.radius >= leftpaddle.position_x - leftpaddle.width / 2 and self.position_y + self.radius > leftpaddle.position_y - (leftpaddle.height /2) and self.position_y - self.radius < leftpaddle.position_y + (leftpaddle.height /2):
            self.delta_x = self.delta_x * -1



        if self.position_x - self.radius <= rightpaddle.position_x + rightpaddle.width / 2 and self.position_x + self.radius >= rightpaddle.position_x - rightpaddle.width / 2 and self.position_y + self.radius > rightpaddle.position_y - (rightpaddle.height /2) and self.position_y - self.radius < rightpaddle.position_y + (rightpaddle.height /2):
            self.delta_x = self.delta_x * -1
            


    #als de bal de zijkant raakt, ga terug naar het midden
    def reset(self):
        self.position_x = SCREEN_WIDTH / 2
        self.position_y = SCREEN_HEIGHT / 2

# hier staat alles over de linker paddle
class LeftPaddle():

    def __init__(self):
        self.position_x: None
        self.position_y: None
        self.height: None
        self.width: None
        self.color: None

        self.move_up = False
        self.move_down = False

    def setup(self, position_x, position_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.width = width
        self.color = color

    def on_draw(self):
         arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def on_update(self):
        if self.move_up == True:
            self.position_y += 4 
        
        if self.move_down == True:
            self.position_y -= 4 
        
        if self.position_y <= 50:
            self.move_down = False
        
        if self.position_y >= 550:
            self.move_up = False



#bewegen met toetsen
#hier staat alles over de rechter paddle
class RightPaddle():

    def __init__(self):
        self.position_x = None
        self.position_y = None
        self.height = None
        self.width = None
        self.color = None

    def setup(self, position_x, position_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.width = width
        self.color = color

    def on_draw(self):
         arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def on_update(self, ball):
        if ball.position_y > self.position_y:
            self.position_y += 4
        if ball.position_y < self.position_y:
            self.position_y -= 4




#bal volgen
#dit is de mygame class, en dit is de allerbelangrijkste class. Zonder deze class werkt je game niet. Ook staat hier alle info van de paddles en de bal in.
class MyGame(arcade.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.ball = None
        self.rightscore_board = None
        self.leftscore_board = None

    #Hier staat alle info zoals de x en y waarde van de objecten in de game
    def setup(self):
        self.ball = Ball()
        self.ball.setup(400, 300, 15, arcade.color.WHITE, -120, -120)

        self.leftpaddle = LeftPaddle()
        self.leftpaddle.setup(30, 300, 10, 100, arcade.color.WHITE)

        self.rightpaddle = RightPaddle()
        self.rightpaddle.setup(770, 300, 10, 100, arcade.color.WHITE)

        self.leftscore_board = LeftScoreBoard()
        self.leftscore_board.setup(200, 570, 15, arcade.color.WHITE, 0)

        self.rightscore_board = RightScoreBoard()
        self.rightscore_board.setup(600, 570, 15, arcade.color.WHITE, 0)

        self.menuscreen = MenuScreen()
        self.menuscreen.setup(400, 300, 800, 600, arcade.color.BLACK, 50, 330, arcade.color.WHITE, 15, 70, 270, arcade.color.WHITE, 15)

        

    def on_draw(self):
        arcade.start_render()

        self.ball.on_draw()
        self.leftpaddle.on_draw()
        self.rightpaddle.on_draw()
        self.leftscore_board.on_draw()
        self.rightscore_board.on_draw()
        self.menuscreen.on_draw()

    def on_update(self, delta_time,):
        self.ball.on_update(delta_time, self.leftscore_board, self.rightscore_board, self.rightpaddle, self.leftpaddle)

        self.leftpaddle.on_update()

        self.rightpaddle.on_update(self.ball)

        self.menuscreen.on_update()


    
#hier staat dat er iets moet gebeuren als je op een knop drukt
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.leftpaddle.move_up = True
        
        if key == arcade.key.S:
            self.leftpaddle.move_down = True

        if key == arcade.key.ENTER:
            self.menuscreen.disappear = True

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W:
            self.leftpaddle.move_up = False        

        if key == arcade.key.S:
            self.leftpaddle.move_down = False



#hierin staat dat de game moet opstarten
def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
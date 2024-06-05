#(lab) slide and catch
#Zechariah Prieshoff
#June 4th, 2024
#A simple, space themed slide and catch game.

import pygame
import simpleGE
import random

class Fuel(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("fuel.png")
        self.setSize(30, 30)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screen.get_height():
            self.reset()
class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("spaceship.png")
        self.setSize(50, 40)
        self.position = (320, 400)
        self.movespeed = 7

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.movespeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.movespeed

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("arcadespace.jpg")

        self.soundFuel = simpleGE.Sound("powerup.wav")

        self.numFuels = 4

        self.score = 0
        self.lblScore = LblScore()
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 5
        self.lblTime = LblTime()

        self.ship = Ship(self)
        self.fuels = []
        for i in range(self.numFuels):
            self.fuels.append(Fuel(self))
        self.sprites = [self.ship, self.fuels, self.lblScore, self.lblTime]

    def process(self):
        for fuel in self.fuels:
            if fuel.collidesWith(self.ship):
                fuel.reset()
                self.soundFuel.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"

        self.lblTime.text = f"Fuel left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()

        self.prevScore = prevScore

        self.setImage("arcadespace.jpg")
        self.response = "Quit"

        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = ["Welcome to Retro Rocket Refuel! You are the rocket", "Move with your left and right arrow keys", "Catch fuel to continue your journey.", "", "Good luck Space Ranger!"]
        self.directions.center = (320, 190)
        self.directions.size = (550, 250)

        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        self.btnPlay.size = (150, 30)

        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
        self.btnQuit.size = (150, 30)

        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last Score: 0"
        self.lblScore.center = (300, 400)

        self.lblScore.text = f"Last Score: {self.prevScore}"

        self.sprites = [self.directions, self.btnPlay, self.btnQuit, self.lblScore]

    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()

        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()

def main():

    keepGoing = True
    lastScore = 0

    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()

        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
        else:
            keepGoing = False

if __name__ == "__main__":
    main()
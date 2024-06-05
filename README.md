# (lab) Slide and Catch Part 2

This is a simple slide and catch game with an arcade/pixel space theme. Users constrol the space ship using the left and right arrow keys to catch the following fuel canisters. fuel canisters fall at random speeds and from random locations.

# Sprite Details

## Fuel Sprite
* **Class name:** "Fuel"
* **Image:** "fuel.png"
* **Size:** 30x30
* **Sprite Type:** Can be a BasicSprite because of its simple motion but it is a SuperSprite.
* **Being Born:** Spawned at the top of the screen at random locations.
* **Dying:** Doesn't necessary die or get destroyed, when it makes contact with the user its location is simply reset.
* **Movement:** Starting from the top of the screen, the sprite(s) fall to the bottom of the screen.
* **Control:** Controlled by the computer.
* **Motion:** Almost like gravity, constantly moving to the bottom of the screen at random speeds.
* **Off-Stage** Sprites are never really off the screen/stage.
* **Collision:** When they makes contact with the user, its location is reset to a random location at the top of the screen.

## Ship Sprite
* **Class name:** "Ship"
* **Image:** "spaceship.png"
* **Size:** 50x40
* **Sprite Type:** Can be a BasicSprite because of its simple motion but it is a SuperSprite. Would need to be a SuperSprite if more complex motions or maybe abilities are added.
* **Being Born:** Spawned in the middle at the bottom of the screen. Same spot everytime.
* **Dying:** Doesn't die or get destroyed, this mechanic can be added later if lives and enemey sprites or things you need to avoid are added.
* **Movement:** Starting from the bottom middle of the screen, the user moves the sprite left and right at a set speed.
* **Control:** Controlled by the user pressing left and right arrow keys.
* **Motion:** Horizontal movement with screen boundaries so that the sprite doesn't go off screen
* **Off-Stage** Sprite is never off the screen/stage.
* **Collision:** When it makes contact with the fuel sprite only the fuel sprite is affected. Added a points system. Current score is at the top left of the screen and updates in the instructions/description screen after each play.

## UI Components
* **Pre-game Explanation:** When game is started, instruction/description screen is opened. Two clickable buttons, play and quit. Later I would like to give the user a choice between pressing space to play or q to quit while also allowing them to use the mouse to click the buttons.
* **Gameplay Feedback:** Added a points system.  Later I will link it to the timer. If the user doesn't get X amount of points in X amount of time they lose.
* **UI Components:** Text for the users score, timer with text that says "fuel left: " would like to had a second everytime the user collects one fuel, may need to be adjusted to .8 or .5 of a second.
* **Mechanics Update:** These components arwe updated in real time during gameplay, the fuel timer is set at 4 and starts dropping when game starts. Should be 10 seconds if the mechanic to add time is not added. Later will add updates to the fuel left timer to have time added.
* **UI Placement:** Score is at the top left of the screen, and the fuel left timer is at the top right. These don't block gameplay.

## Game States
* **States:** There is a instructions (Start Menu) state and playing state.
* **Transfer Between States:** When the game is started the player is shown the instructions screen, when they press the play button they are sent to the playing state. The transitions look like *Start Menu* > *Playing Game* by pressing the play button. In game it looks like *Playing Game* > *Start Menu*.
* **Communication Between States:** The users last score is passed through the states to have a "last score" mechanic.
* **Game Ending:** The playing state is ended whenever the fuel left timer reaches zero. The entire game can be quit by the user either manually closing out of the pygame window or pressing the "Quit" button.

## Sound Effects
* **Needed Sound Effects:** Game Start, collecting fuel "powerup.wav", Game Over. Already have collecting fuel sound, its annoying but good so turn your volume down. 
* **Sound Playback:** Game Start sound would be played when the user the play button while in the Start Menu State. Collecting fuel sound is already played when the user collects fuel. Game Over sound would be played when the users fuel left timer goes down, then if the user chooses to play again the Game Start sound can be played again.
* **Sound Code Placement:** Should be in event handling sections for their causes.

## Background Image
* **Image:** There is a background image that represents a pixel space theme.
* **Where?:** I created the image myself.
* **Visability:** The gameplay can still be clearly seen because the sprites are brightly color and the background image is dark.

## Intellectual Property
* **Fuel:** Image taken from pixelart https://www.pixilart.com/draw/gas-can-0d8faf0067e0f64
* **Background Image:** Image created by me using pixilart
* **Ship:** Image made by me using pixilart
* **Collecting Fuel:** Sound taken from Freesound https://freesound.org/people/Romeo_Kaleikau/sounds/588251/

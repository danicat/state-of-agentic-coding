Create a Pac Man clone written in Go. The game should only have one stage and one life. There are 4 ghosts that move in random directions. The player controls Pac Man and dies if touches the ghosts. The game is over if the player is killed or they eat all the dots in the maze.

TODO:
- use github.com/hajimehoshi/ebiten/v2/ as the game engine
- use github.com/hajimehoshi/ebiten/v2/vector to build the sprites
- arrow keys move pacman
- pac man should keep moving in the same direction until a new input changes it
- Q should quit the game
- R should restart
- F toggles the fullscreen mode
- Pac man should have a mouth animation when moving
- Ghosts should have eye animations when moving, looking towards direction of movement

Acceptance Criteria:
- Code builds successfully
- Pac Man dies if touches Ghost
- Game over if lives == 0
- Score increases if Pac Man eats dots (+1)
- Game win if total number of dots in the maze == 0
# 2048 Game
This is an adapted version of original game of 2048.

In the original game the user has to slide the tiles to combine similar tiles and finally has to reach number 2048 usually on a board of size 5*5.

However in this adaptation of game the the user can specify the board size and the winning value.

Windows was the OS used to write the program.
Atom was used as a text editor.


![Initial Setup](/Images/InitialSetup.png)

## Table of contents
1. [Requirements](#requirements)
2. [How to play](#how-to-play)
3. [Working of game](#working-of-game)
4. [Validation of Inputs](#validation-of-inputs)
5. [Modules used](#modules-used)
## Requirements
* The user needs to have python 3 installed in his system.
Here's the [link](https://www.python.org/downloads/) to download python3.Download according to system's OS.

* The user needs to install pip3.(In case the program is unable to import a module it will install through pip3).

To install pip3 in UNIX based OSs enter 
`sudo apt-get install pip3`or `sudo apt-get install python3-pip` on terminal.

In case of Fendora linux enter `sudo yum install python3-pip`.

## How to play
This game is made to be played from command line.

#### 1.To Start:
* Go to directory where the program is stored.
* enter ` python 2048.py ` for windows and `python3 2048.py` for UNIX based OSs.
  > To change the value of board size `python 2048.py --n N --w W`
  > here N is the value of board size and W is winning value.
  >
  > In case these values are not specified the default values i.e. N=5 and W=2048 are taken.
  ![Custom Inputs](/Images/Customspecifying.png)


#### 2. Movements
* The movement of board in four directions can be controlled by  w,a,s,d keys
  * w for upward movement
  * s for downward movement
  * a for leftward movement
  * d for rightward movement
    > there is no need to press enter after each key
* q is used to __**Forfeit**__ the game in middle of game play.
![Forfeit](/Images/Forfeit.png)
  >**Any other key entered during the game is considered to be Invalid Input**
  
  
  ![Invalid Input](/Images/Invalid.png)

## Working of game
* The game is won by reaching a desired score set by user W ( or default 2048)


  ![Win](/Images/Win.png)
* In case all places are filled by non-zero numbers the user looses the game.


  ![Lost](/Images/lost.png)
  
* Each time a valid input of movement is made a random 2 is generated on a place with zero value.


## Validation of inputs
* Specifying the board size and winning value using `--n N and --w W` is
only valid if N is an integer with value (<= 40 set as default can be increased in code)
and W is an interger and multiple of 2 (<= 2<sup>50</sup> set as default can be increased in code)
* During the gameplay any key other than w/a/s/d/q is considered to be **Invalid Input** and 
program continues to ask for input until it gets a valid input.
* In case the move does not make any changes to the board 
  * A message " Try another move" is flashed .
  
  
    ![Try another move](/Images/tryanothermove.png)
  * No new random 2 is generated.
  
## Modules used
* os 
  > for getting the os name and passing commands to command line
* random
* argparse
* msvcrt
  >to use getche in windows
* getch
  >to use getche in UNIX based OSs
## Contributors
**[Atharva Kathale](https://github.com/Atharva-K12)**




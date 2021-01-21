# PDP-8

A fork of the Python PDP-8 emulator with Blinkenlights. Needs PyGame.

The top row of lights shows the program counter and the bottom row the accumulator.

To quit the program, press Ctrl+C to return to the monitor, then q.

## Running the Chekmo chess program

 python3 pdp8.py
 load
 r

Enter a White move in uppercase (time for Caps Lock!), e.g. "E2-E4" and then "PB" for the computer to play Black.

 $ python3 pdp8.py
 pygame 2.0.1 (SDL 2.0.14, Python 3.9.1)
 Hello from the pygame community. https://www.pygame.org/contribute.html
 PDP-8 simulator v0.000001, (c) 2020 j. dersch
 PC 0000 AC 0000 L 0 SW 0000 IE 0
 > load
 PC 0200 AC 0000 L 0 SW 0000 IE 0
 > r

 CHEKMO-II
 W. YOUR MOVE? E2-E4
 B. YOUR MOVE? PB
 B. D7-D5  
 W. YOUR MOVE? 

![screenshot](https://github.com/mdoege/PDP-8/raw/master/chekmo.png "screenshot")
![blinkenlights](https://github.com/mdoege/PDP-8/raw/master/Das_Blinkenlights.gif "very important blinkenlights sign")

## Running RIM tape files

### Shifter

 rim
 pt shifter.rim
 r
 <Ctrl-C> when loading has finished
 pc 100

Now repeatedly enter "s" to single-step through the program and watch the accumulator increase every few steps.

### FOCAL

 rim
 pt focal-2.rim
 r
 <Ctrl-C> when loading has finished
 pc 200
 r

Now enter some FOCAL code at the "*" prompt, e.g. this **F**OR loop which **T**YPEs numbers:

 *1.1 F X=1,1,5; T X,!
 *G
 =    1.0000
 =    2.0000
 =    3.0000
 =    4.0000
 =    5.0000

Or compute the square root of 2:

 *T FSQT(2)
 =    1.4142*

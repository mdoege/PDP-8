# PDP-8

A fork of the Python PDP-8 emulator with Blinkenlights. Needs PyGame.

The top row of lights shows the program counter and the bottom row the accumulator.

To quit the program, press Ctrl+C to return to the monitor, then q.

## Running the Chekmo chess program
```
 python3 pdp8.py
 load
 r
```
Enter a White move in uppercase (time for Caps Lock!), e.g. "E2-E4" and then "PB" for the computer to play Black.
```
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
```

Here is a game between Stockfish and Chekmo, with analysis provided by SCID:

![screenshot](https://github.com/mdoege/PDP-8/raw/master/chekmo.png "screenshot")

And always remember to only *watch* those pretty blinkenlights... :)

![blinkenlights](https://github.com/mdoege/PDP-8/raw/master/Das_Blinkenlights.gif "very important blinkenlights sign")

## Running RIM tape files

### Shifter
```
 rim
 pt shifter.rim
 r
 <Ctrl-C> when loading has finished
 pc 100
```
Now repeatedly enter "s" to single-step through the program and watch the accumulator increase every few steps.

### FOCAL
```
 rim
 pt focal-2.rim
 r
 <Ctrl-C> when loading has finished
 pc 200
 r
```
Now enter some FOCAL code at the "*" prompt, e.g. this **F**OR loop which **T**YPEs numbers:
```
 *1.1 F X=1,1,5; T X,!
 *G
 =    1.0000
 =    2.0000
 =    3.0000
 =    4.0000
 =    5.0000
```
Or compute the square root of 2:
```
 *T FSQT(2)
 =    1.4142*
```

### Loading external text files into the PDP-8

The "auto" monitor command auto-types a text file into the terminal. You can e.g. load external code into FOCAL this way:
```
*CTRL-C halt
PC 2667 AC 0000 L 1 SW 0000 IE 1
> auto fib.fc
PC 2667 AC 0000 L 1 SW 0000 IE 1
> r
01.10 TYPE "FIBONACCI NUMBERS" !
*01.20 ASK "MAX N =", N
*01.30 SET A=0
*01.40 SET B=1
*01.50 FOR I=2,N; DO 2.0
*01.60 QUIT
* 
*02.10 SET T=B
*02.20 SET B=A+B
*02.30 SET A=T
*02.40 TYPE "F(",I,") ", %8, B, !
*
*G
FIBONACCI NUMBERS
MAX N =:20
F(=        2) =        1
F(=        3) =        2
F(=        4) =        3
F(=        5) =        5
F(=        6) =        8
F(=        7) =       13
F(=        8) =       21
F(=        9) =       34
F(=       10) =       55
F(=       11) =       89
F(=       12) =      144
F(=       13) =      233
F(=       14) =      377
F(=       15) =      610
F(=       16) =      987
F(=       17) =     1597
F(=       18) =     2584
F(=       19) =     4181
F(=       20) =     6765
*
```


# PDP-8

![screenshot](https://github.com/mdoege/PDP-8/raw/master/screenshot.png "screenshot")

A fork of the Python [PDP-8](https://en.wikipedia.org/wiki/PDP-8) emulator with added [Blinkenlights](https://en.wikipedia.org/wiki/Blinkenlights). Needs [PyGame](https://www.pygame.org/).

The top row of lights shows the program counter and the bottom row the accumulator.

To quit the program, press Ctrl+C to return to the monitor, then enter q.

PDP-8 front panel photo by [David Gesswein](https://www.pdp8online.com/straight8/front_panel_restore.shtml).

## Running the [Chekmo](https://www.chessprogramming.org/CHEKMO-II) chess program
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

Here is a game between Stockfish and Chekmo, with analysis provided by [SCID](http://scidvspc.sourceforge.net/):

![chekmo](https://github.com/mdoege/PDP-8/raw/master/chekmo.png "chekmo")

But always remember to only *watch* those pretty blinkenlights... :)

![blinkenlights](https://github.com/mdoege/PDP-8/raw/master/Das_Blinkenlights.gif "very important blinkenlights sign")

## Running RIM tape files

### Shifter
```
 rim
 pt shifter.rim
 r
     Press <Ctrl-C> when loading has finished
 pc 100
```
Now repeatedly enter "s" to single-step through the program and watch the accumulator increase every few steps.

## The [FOCAL](https://en.wikipedia.org/wiki/FOCAL_(programming_language)) programming language
```
$ python3 pdp8.py 
pygame 2.0.1 (SDL 2.0.14, Python 3.9.1)
Hello from the pygame community. https://www.pygame.org/contribute.html
PDP-8 simulator v0.000001, (c) 2020 j. dersch
PC 0000 AC 0000 L 0 SW 0000 IE 0
> load focal
PC 0200 AC 0000 L 0 SW 0000 IE 0
> r

CONGRATULATIONS!!
YOU HAVE SUCCESSFULLY LOADED 'FOCAL,1969' ON A PDP-8 COMPUTER.


SHALL I RETAIN LOG, EXP, ATN ?:NO

SHALL I RETAIN SINE, COSINE ?:NO

PROCEED.

*W
C-FOCAL,1969
```
Now enter some FOCAL code at the "*" prompt, e.g. this **F**OR loop which **T**YPEs numbers, and then use **G**OTO to run the program. (In FOCAL, commands can be abbreviated by just using their first character.)
```
 *1.1 F X=1,1,5; T X,!
 *G
 =    1.0000
 =    2.0000
 =    3.0000
 =    4.0000
 =    5.0000
```

Use "W" to list the program and "E ALL" to delete it.

### Loading external code into FOCAL

The "auto" monitor command auto-types a text file into the terminal. Three FOCAL source code files are included:

* lunar.fc ([Lunar Lander](https://en.wikipedia.org/wiki/Lunar_Lander_(video_game_genre)))
* ham.fc ([Hamurabi](https://en.wikipedia.org/wiki/Hamurabi_(video_game)))
* mand.fc ([Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set))
* fib.fc ([Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number))
* eras.fs ([Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes))

Note that lunar.fc and ham.fc need a lot of free RAM, so you need to answer "NO" to the FOCAL startup questions!

#### Hamurabi
```
$ python3 pdp8.py 
pygame 2.0.1 (SDL 2.0.14, Python 3.9.1)
Hello from the pygame community. https://www.pygame.org/contribute.html
PDP-8 simulator v0.000001, (c) 2020 j. dersch
PC 0000 AC 0000 L 0 SW 0000 IE 0
> load focal
PC 0200 AC 0000 L 0 SW 0000 IE 0
> r

CONGRATULATIONS!!
YOU HAVE SUCCESSFULLY LOADED 'FOCAL,1969' ON A PDP-8 COMPUTER.


SHALL I RETAIN LOG, EXP, ATN ?:NO

SHALL I RETAIN SINE, COSINE ?:NO

PROCEED.

*CTRL-C halt
PC 2670 AC 0000 L 0 SW 0000 IE 1
> auto ham.fcl
PC 2670 AC 0000 L 0 SW 0000 IE 1
> r
   .... <computer reads program text>
*G


HAMURABI:  


LAST YEAR
=     0 STARVED,
=     5 ARRIVED,
POPULATION IS=   100

THE CITY OWNS=  1000 ACRES.

WE HARVESTED=     3 BUSHELS PER ACRE;
 RATS ATE =   200 BUSHELS, YOU NOW HAVE
=  2800 BUSHELS IN STORE.


HAMURABI:  LAND IS TRADING AT=    18 BUSHELS PER ACRE;
HOW MANY ACRES OF LAND DO YOU WISH TO BUY?
```

#### Mandelbrot set
```
$ python3 pdp8.py 
pygame 2.0.1 (SDL 2.0.14, Python 3.9.1)
Hello from the pygame community. https://www.pygame.org/contribute.html
PDP-8 simulator v0.000001, (c) 2020 j. dersch
PC 0000 AC 0000 L 0 SW 0000 IE 0
> load focal
PC 0200 AC 0000 L 0 SW 0000 IE 0
> r

CONGRATULATIONS!!
YOU HAVE SUCCESSFULLY LOADED 'FOCAL,1969' ON A PDP-8 COMPUTER.


SHALL I RETAIN LOG, EXP, ATN ?:NO

SHALL I RETAIN SINE, COSINE ?:NO

PROCEED.

*CTRL-C halt
PC 2671 AC 0000 L 0 SW 0000 IE 1
> auto mand.fc
PC 2671 AC 0000 L 0 SW 0000 IE 1
> r
   .... <computer reads program text>

*G

**********************************************************************
**********************************************************************
**************************************************** *****************
*************************************************      ***************
*************************************************      ***************
****************************************    *               **********
*************************************** *                       ******
*************************************                            *****
********************** **** *******                               ****
***********************          **                                 **
*********************                                             ****
*** *                                                          *******
*********************                                             ****
***********************          **                                 **
********************** **** *******                               ****
*************************************                            *****
*************************************** *                       ******
****************************************    *               **********
*************************************************      ***************
*************************************************      ***************
**************************************************** *****************
**********************************************************************
**********************************************************************
**********************************************************************
```


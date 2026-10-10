# CS4346 Morris Game AI 

## Overview

**Files**
- MiniMaxOpening.py: Computes whites best move during the oppening phase of the game
- MiniMaxGame.py: Computes whites best move during the mid/end-game phase
- ABOpening.py & ABGame.py: Reimplements the previous 2 files, this time making use of ALPHA-BETA prunging to shorten runtimes.
- MiniMaxOpeningBlack.py & MiniMaxGameBlack.py: Reimplementations of first 2 files, this time computing blacks best move during opening/mid/end-game phases of play
- MiniMaxOpeningImpoved.py & MiniMaxGameImproved.py: Upgrades on the supplied static estimation function located in `morris.py`.

## Usage
**Playing A Game**


**Evaluating Static Estimation Functions**
For this project we were given a set of static estimation functions (SEFs) which can be seen below.
```
def staticEstimationOpening(board):
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    return numWhitePieces - numBlackPieces
def staticEstimationMidgameEndgame(board):
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    L = GenerateMovesMidgameEndgameBlack(board)
    numBlackMoves = len(L)
    if numBlackPieces <= 2:
        return 10000
    elif numWhitePieces <= 2:
        return -10000
    elif numBlackMoves == 0:
        return 10000
    else:
        return 1000 * (numWhitePieces - numBlackPieces) - numBlackMoves

```

As the implementations above are quite basic we have gone ahead and implemented a series of improved SEFs. These SEFs have been tested thorhough a 2 step process, first we ran them on the test boards located within the `./boards` directory. These test boards have been designed to display an implementations ability (or lack thereof) to take advantage of things like potential mills, block enemy mills, populate important locations on the board, etc. Boards found in `./boards` have been specifically designed to test each implementations ability to perform during both the opening game (boards 0-4) and mid/endgame (boards 5-9). 

The second step was to how they performed in real matches aganinst each other. If you would like to see how this went go ahead and read the `MyStaticEstimation.txt` file for more detail or run the `match_stats.py` file in the `/tests` directory.

*Note: All SEF implementation can be found at `MiniMaxOpeningImporved.py` & `MiniMaxGameImproved.py`, those which are being used by the `MinimaxOpeingImproved` and `MiniMaxgameImproved` are the ones we have found to perform the best.*

**Testing**
Test scripts have also been implemented to help correct potential issues in development. These include things like unittesting, benchmarking, and xxx. These all can be found within the `./tests` directory.

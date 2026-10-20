"""Improved implementation of MiniMaxGame.py, computes white's maxima move in the fixed midgame/endgame phase."""

import sys
from morris import (
    read_board,
    write_board,
    GenerateMovesMidgameEndgame,
    GenerateMovesMidgameEndgameBlack,
    MILLS,
    neighbors
)

def ImprovedSEFGame(board):
    numWhitePieces = board.count('W')
    numBlackPieces = board.count('B')
    
    if numBlackPieces <= 2:
        return 10000
    elif numWhitePieces <= 2:
        return -10000
    
    whiteMoves = GenerateMovesMidgameEndgame(board)
    blackMoves = GenerateMovesMidgameEndgameBlack(board)
    
    if len(blackMoves) == 0:
        return 10000
    if len(whiteMoves) == 0:
        return -10000

    white2Pieces = 0
    black2Pieces = 0
    for mill in MILLS:
        pieces = [board[i] for i in mill]
        if pieces.count('W') == 2 and pieces.count('x') == 1:
            white2Pieces += 1
        elif pieces.count('B') == 2 and pieces.count('x') == 1:
            black2Pieces += 1

    pieceScore = 1000 * (numWhitePieces - numBlackPieces)
    mobilityScore = 10 * (len(whiteMoves) - len(blackMoves))
    millSetupScore = 20 * (white2Pieces - black2Pieces)

    # 100 * (numWhitePieces - numBlackPieces) + 10 * (len(whiteMoves) - len(blackMoves)) + 20 * (white2Pieces - black2Pieces)
    return pieceScore + mobilityScore + millSetupScore 

def MiniMaxGameImproved(board, depth):
    if not isinstance(board, str) or len(board) != 23 or any(c not in "WBx" for c in board):
        raise ValueError("board must contain exactly 23 characters from W, B, x")
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a nonnegative integer")

    positions_evaluated = 0

    def evaluate(position):
        nonlocal positions_evaluated
        positions_evaluated += 1
        return ImprovedSEFGame(position), position

    def visit(position, remaining, maximizing, alpha, beta):
        if remaining == 0:
            return evaluate(position)
        children = GenerateMovesMidgameEndgame(position) if maximizing else GenerateMovesMidgameEndgameBlack(position)
        if not children:
            return evaluate(position)

        best_score = float("-inf") if maximizing else float("inf")
        best_board = None
        for child in children:
            score, _ = visit(child, remaining - 1, not maximizing, alpha, beta)
            better = score > best_score if maximizing else score < best_score
            if best_board is None or better:
                best_score = score
                best_board = child
        return best_score, best_board

    estimate, best_board = visit(board, depth, True, float("-inf"), float("inf"))
    return estimate, best_board, positions_evaluated

def main():
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} input.txt output.txt depth", file=sys.stderr)
        return 1

    try:
        depth = int(sys.argv[3])
        if depth < 0:
            raise ValueError("depth must be a nonnegative integer")
        board = read_board(sys.argv[1])
        estimate, best_board, count = MiniMaxGameImproved(board, depth)
        write_board(sys.argv[2], best_board)
    except (OSError, ValueError, RecursionError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Board Position: {best_board}")
    print(f"Positions evaluated by static estimation: {count}")
    print(f"MINIMAX estimate: {estimate}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

import sys
from morris import (
    read_board,
    write_board,
    GenerateMovesOpening,
    GenerateMovesOpeningBlack,
    staticEstimationOpening
)

def swap_colors(board):
    """Swap 'W' and 'B' characters in the board string."""
    return "".join(
        'B' if c == 'W' else ('W' if c == 'B' else c) for c in board
    )

def minimax_opening_black(board, depth):
    """Minimax search for Black opening phase using color swapping. Return (score, board, count)."""
    if not isinstance(board, str) or len(board) != 23 or any(c not in "WBx" for c in board):
        raise ValueError("board must contain exactly 23 characters from W, B, x")
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a nonnegative integer")

    # Swap colors so Black is treated as White (maximizing player)
    swapped_board = swap_colors(board)

    positions_evaluated = 0

    def evaluate(position):
        nonlocal positions_evaluated
        positions_evaluated += 1
        return staticEstimationOpening(position), position

    def visit(position, remaining, maximizing, alpha, beta):
        if remaining == 0:
            return evaluate(position)
        children = (
            GenerateMovesOpening(position)
            if maximizing
            else GenerateMovesOpeningBlack(position)
        )
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

    estimate, best_swapped_board = visit(swapped_board, depth, True, float("-inf"), float("inf"))
    best_board = swap_colors(best_swapped_board)
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
        estimate, best_board, count = minimax_opening_black(board, depth)
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

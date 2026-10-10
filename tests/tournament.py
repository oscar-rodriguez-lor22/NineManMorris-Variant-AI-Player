import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))


from morris import(
        swap_colors
)
from cli_helper import(
        _search
)
from MiniMaxOpeningImproved import(
        ImprovedSEFOpening_1,
        ImprovedSEFOpening_2,
        ImprovedSEFOpening_3,
        MiniMaxOpeningImproved
)
from MiniMaxGameImproved import(
        ImprovedSEFGame_1,
        ImprovedSEFGame_2
        ImprovedSEFGame_3,
        MiniMaxGameImproved
)

class Player()

    def __init__(self, player_color, op, mid):
        self.turn = 0
        self.player_color = player
        self.opening_sef = op
        self.midgame_sef = mid

    def PlayTurn(self, board, depth):
        evaluation = None

        if (self.turn <= 9):
            evaluation = opening_sef
        else:
            evaluation = midgame_sef
        
        if (self.player_color == "B"):
            board = swap_colors(board)

        _search(
                board,
                depth,
                GenerateMovesOpening,
                GenerateMovesOpeningBlack,
                evaluation
                )
        # Check if _search() can determine whether a game has ended or not
        # Check if _search() can determine if a draw has occured
        self.turn += 1

        

def PlayMatch(w_player, b_player):
    board = 
    turns = 0
    final_board = None
    winner = None
    game_ongoing = True

    while(game_ongoing):
        w_player.Playturn(board, 3)
        b_player.Playturn(board, 3)
        turns += 1


    # given 2 Player() objects, complete one game from start to finish
    # return [starting_board, final_board, number_of_turns, winner]

def TestModels():
    match_results = []

    w_op1_mid1 = Player(ImprovedSEFOpening_1, ImprovedSEFGame_1, "W")
    w_op1_mid2 = Player(ImprovedSEFOpening_1, ImprovedSEFGame_2, "W")
    w_op1_mid3 = Player(ImprovedSEFOpening_1, ImprovedSEFGame_3, "W")
    w_op2_mid1 = Player(ImprovedSEFOpening_2, ImprovedSEFGame_1, "W")
    w_op2_mid2 = Player(ImprovedSEFOpening_2, ImprovedSEFGame_2, "W")
    w_op2_mid3 = Player(ImprovedSEFOpening_2, ImprovedSEFGame_3, "W")
    w_op3_mid1 = Player(ImprovedSEFOpening_3, ImprovedSEFGame_1, "W")
    w_op3_mid2 = Player(ImprovedSEFOpening_3, ImprovedSEFGame_2, "W")
    w_op3_mid3 = Player(ImprovedSEFOpening_3, ImprovedSEFGame_3, "W")
    
    w_players = [ w_op1_mid1, w_op1_mid2, w_op1_mid3, w_op2_mid1, w_op2_mid2, w_op2_mid3, w_op3_mid1, w_op3_mid2, w_op3_mid3]

    b_op1_mid1 = Player(ImprovedSEFOpening_1, ImprovedSEFGame_1, "B")
    b_op1_mid2 = Player(ImprovedSEFOpening_1, ImprovedSEFGame_2, "B")
    b_op1_mid3 = Player(ImprovedSEFOpening_1, ImprovedSEFGame_3, "B")
    b_op2_mid1 = Player(ImprovedSEFOpening_2, ImprovedSEFGame_1, "B")
    b_op2_mid2 = Player(ImprovedSEFOpening_2, ImprovedSEFGame_2, "B")
    b_op2_mid3 = Player(ImprovedSEFOpening_2, ImprovedSEFGame_3, "B")
    b_op3_mid1 = Player(ImprovedSEFOpening_3, ImprovedSEFGame_1, "B")
    b_op3_mid2 = Player(ImprovedSEFOpening_3, ImprovedSEFGame_2, "B")
    b_op3_mid3 = Player(ImprovedSEFOpening_3, ImprovedSEFGame_3, "B")
    
    b_players = [ b_op1_mid1, b_op1_mid2, b_op1_mid3, b_op2_mid1, b_op2_mid2, b_op2_mid3, b_op3_mid1, b_op3_mid2, b_op3_mid3]

    for w_player in w_players:
        for b_player in b_players:
            match_result = PlayMatch()
            match_results.append(match_result)
    
    print()

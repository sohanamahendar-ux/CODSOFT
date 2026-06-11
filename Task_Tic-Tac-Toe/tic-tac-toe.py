# ================================================
# TIC-TAC-TOE WITH AI (Minimax Algorithm)
# Built step by step for beginners
# ================================================
# HOW THE GAME WORKS:
#   - You play as X, the computer plays as O
#   - The board has 9 spots, numbered 1 to 9
#   - You pick a number to place your X
#   - The AI thinks and places its O
#   - First to get 3 in a row wins!
# ================================================


# ------------------------------------------------
# STEP 1: CREATE THE BOARD
# ------------------------------------------------
# The board is just a list with 9 spots.
# We use numbers 1-9 so the player knows which
# spot to pick. Later, numbers get replaced by
# "X" or "O" as the game is played.

def create_board():
    # A list of strings "1" to "9"
    # Think of it like 9 empty boxes in a row
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    return board


# ------------------------------------------------
# STEP 2: DISPLAY THE BOARD
# ------------------------------------------------
# This prints the board in a nice grid so it
# looks like a real Tic-Tac-Toe board.
#
# Example output:
#   1 | 2 | 3
#  -----------
#   4 | 5 | 6
#  -----------
#   7 | 8 | 9

def show_board(board):
    print()  # blank line for spacing

    # board[0], board[1], board[2] are the top row
    print(f"  {board[0]} | {board[1]} | {board[2]}  ")
    print(" -----------")

    # board[3], board[4], board[5] are the middle row
    print(f"  {board[3]} | {board[4]} | {board[5]}  ")
    print(" -----------")

    # board[6], board[7], board[8] are the bottom row
    print(f"  {board[6]} | {board[7]} | {board[8]}  ")

    print()  # blank line for spacing


# ------------------------------------------------
# STEP 3: TAKE USER INPUT AND PLACE X
# ------------------------------------------------
# We ask the player to enter a number (1-9).
# Then we check if that spot is already taken.
# If it's free, we place "X" there.
# If it's taken or invalid, we ask again.

def player_move(board):
    while True:   # keep asking until we get a valid answer
        move = input("Your turn! Pick a spot (1-9): ")

        # Check 1: Did the player actually type a number?
        if not move.isdigit():
            print("  Oops! Please type a number between 1 and 9.")
            continue   # go back to the top of the loop

        # Convert the text "5" into the actual number 5
        move = int(move)

        # Check 2: Is the number in the valid range 1-9?
        if move < 1 or move > 9:
            print("  Oops! That number is out of range. Try 1-9.")
            continue

        # The board list uses index 0-8, but the player uses 1-9
        # So we subtract 1: player picks 5 → index 4
        index = move - 1

        # Check 3: Is that spot already taken by X or O?
        if board[index] == "X" or board[index] == "O":
            print("  That spot is already taken! Choose another.")
            continue

        # All checks passed! Place X on the board.
        board[index] = "X"
        break   # exit the loop, move is done


# ------------------------------------------------
# STEP 4: CHECK IF SOMEONE WON
# ------------------------------------------------
# A player wins if they have 3 in a row:
#   - across any row (horizontal)
#   - down any column (vertical)
#   - diagonally (corner to corner)
#
# We pass in "X" or "O" to check for that player.

def check_winner(board, player):

    # --- Check all 3 rows ---
    # Row 1: indexes 0, 1, 2
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    # Row 2: indexes 3, 4, 5
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    # Row 3: indexes 6, 7, 8
    if board[6] == player and board[7] == player and board[8] == player:
        return True

    # --- Check all 3 columns ---
    # Column 1: indexes 0, 3, 6
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    # Column 2: indexes 1, 4, 7
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    # Column 3: indexes 2, 5, 8
    if board[2] == player and board[5] == player and board[8] == player:
        return True

    # --- Check both diagonals ---
    # Diagonal top-left to bottom-right: indexes 0, 4, 8
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    # Diagonal top-right to bottom-left: indexes 2, 4, 6
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    # If none of the above matched, this player hasn't won yet
    return False


# ------------------------------------------------
# STEP 5: CHECK IF THE BOARD IS FULL (DRAW)
# ------------------------------------------------
# If all 9 spots are filled and nobody won,
# the game is a draw.
# We check if any spot still has a number (not X or O).
# If ALL spots have X or O, the board is full.

def check_draw(board):
    for spot in board:
        # If we find any spot that is still a number,
        # the board is NOT full yet
        if spot != "X" and spot != "O":
            return False   # board still has empty spots

    # If we got through the whole loop without finding
    # an empty spot, the board is full → it's a draw
    return True


# ------------------------------------------------
# STEP 6: THE MINIMAX ALGORITHM
# ------------------------------------------------
# This is the brain of the AI.
#
# Minimax works by imagining all possible future moves.
# It thinks: "If I play here, what's the best the opponent
# can do? And then what's the best I can do after that?"
#
# It gives scores to outcomes:
#   +1  → AI (O) wins
#   -1  → Human (X) wins
#    0  → Draw
#
# "is_ai_turn" tells us whose turn it is in the simulation.

def minimax(board, is_ai_turn):

    # --- BASE CASES (when the game is already over) ---

    # If AI (O) already won in this scenario, return +1
    if check_winner(board, "O"):
        return 1

    # If human (X) already won in this scenario, return -1
    if check_winner(board, "X"):
        return -1

    # If the board is full and nobody won, it's a draw → return 0
    if check_draw(board):
        return 0

    # --- RECURSIVE CASE: simulate future moves ---

    if is_ai_turn:
        # AI wants to MAXIMIZE the score (find the best move for O)
        best_score = -100   # start with a very low "worst case" score

        for i in range(9):   # look at all 9 spots
            if board[i] != "X" and board[i] != "O":   # only try empty spots
                saved = board[i]       # remember what was in this spot
                board[i] = "O"         # pretend AI plays here

                # Now it's the human's turn → call minimax again
                score = minimax(board, False)

                board[i] = saved       # undo the pretend move (backtrack)

                # Keep track of the highest score seen so far
                if score > best_score:
                    best_score = score

        return best_score   # return the best score AI can achieve

    else:
        # Human's turn → human wants to MINIMIZE the score (best for X)
        best_score = 100    # start with a very high "worst case" score

        for i in range(9):   # look at all 9 spots
            if board[i] != "X" and board[i] != "O":   # only try empty spots
                saved = board[i]       # remember what was in this spot
                board[i] = "X"         # pretend human plays here

                # Now it's the AI's turn → call minimax again
                score = minimax(board, True)

                board[i] = saved       # undo the pretend move (backtrack)

                # Keep track of the lowest score seen so far
                if score < best_score:
                    best_score = score

        return best_score   # return the best score human can force


# ------------------------------------------------
# STEP 7: FIND THE BEST MOVE FOR THE AI
# ------------------------------------------------
# This function looks at all available (empty) spots,
# runs Minimax for each one, and picks the move
# that gives the AI the highest score.

def best_ai_move(board):
    best_score = -100      # start with a very low score
    best_index = None      # we don't know the best spot yet

    for i in range(9):     # check all 9 spots
        if board[i] != "X" and board[i] != "O":   # only empty spots
            saved = board[i]      # remember what was here
            board[i] = "O"        # pretend AI plays here

            # Ask Minimax: how good is this move? (human plays next → False)
            score = minimax(board, False)

            board[i] = saved      # undo the pretend move

            # Is this move better than what we've seen so far?
            if score > best_score:
                best_score = score
                best_index = i    # remember this spot as the best

    # Actually place the AI's O on the best spot found
    board[best_index] = "O"
    print(f"  Computer placed O on spot {best_index + 1}")


# ------------------------------------------------
# STEP 8: CONNECT EVERYTHING — THE MAIN GAME LOOP
# ------------------------------------------------
# This is where it all comes together.
# We alternate between the human's turn and the AI's turn
# until someone wins or the board is full.

def play_game():
    print("=" * 35)
    print("   Welcome to Tic-Tac-Toe!")
    print("   You are X  |  Computer is O")
    print("=" * 35)
    print()
    print("  The board positions are:")
    print("   1 | 2 | 3")
    print("  -----------")
    print("   4 | 5 | 6")
    print("  -----------")
    print("   7 | 8 | 9")

    # Create a fresh empty board to start the game
    board = create_board()

    # Show the board before any moves
    show_board(board)

    # The game loop — keeps going until the game is over
    while True:

        # ---- HUMAN'S TURN ----
        player_move(board)    # ask player to pick a spot
        show_board(board)     # show the updated board

        # Did the human just win?
        if check_winner(board, "X"):
            print("  🎉 You won! Congratulations!")
            break   # game over, exit the loop

        # Did the human's move fill the last spot (draw)?
        if check_draw(board):
            print("  It's a draw! Well played!")
            break

        # ---- AI'S TURN ----
        print("  Computer is thinking...")
        best_ai_move(board)   # AI picks the best spot using Minimax
        show_board(board)     # show the updated board

        # Did the AI just win?
        if check_winner(board, "O"):
            print("  Computer wins! Better luck next time.")
            break

        # Did the AI's move fill the last spot (draw)?
        if check_draw(board):
            print("  It's a draw! Well played!")
            break

    print()
    print("  Thanks for playing!")
    print("=" * 35)


# ------------------------------------------------
# STEP 9: RUN THE GAME
# ------------------------------------------------
# This line makes sure the game only starts when
# you run this file directly (not when it's imported
# by another file as a module).

if __name__ == "__main__":
    play_game()
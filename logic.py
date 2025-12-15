import random
import wx

# -----------------------------
# Constants
# -----------------------------

CODE_LENGTH = 4
COLORS = ["R", "G", "B", "Y"]
TRIES = 10

# -----------------------------
# Game Logic
# -----------------------------

def generate_code():
    """Generates a random code of 4 colors."""
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


def check_code_black_white(guess, real_code):
    """Returns (white, black) counts for a guess."""
    white = 0
    black = 0
    color_counts = {}

    for c in real_code:
        color_counts[c] = color_counts.get(c, 0) + 1

    # Count white pegs (correct color & position)
    for i in range(len(guess)):
        if guess[i] == real_code[i]:
            white += 1
            color_counts[guess[i]] -= 1

    # Count black pegs (correct color, wrong position)
    for i in range(len(guess)):
        if guess[i] != real_code[i] and color_counts.get(guess[i], 0) > 0:
            black += 1
            color_counts[guess[i]] -= 1

    return white, black


# -----------------------------
# Submit Handler
# -----------------------------

def on_submit(frame):
    """Handles a guess submission from the UI."""
    guess = [rb.GetStringSelection() for rb in frame.radio_choices]
    white, black = check_code_black_white(guess, frame.code)

    frame.history.AppendText(
        f"Try {frame.attempt}: {' '.join(guess)}  |  White: {white}, Black: {black}\n"
    )

    if white == CODE_LENGTH:
        wx.MessageBox(f"You solved it in {frame.attempt} tries!", "Winner")
        frame.Close()
        return

    if frame.attempt >= TRIES:
        wx.MessageBox(f"You lost! Code was: {' '.join(frame.code)}", "Game Over")
        frame.Close()
        return

    frame.attempt += 1

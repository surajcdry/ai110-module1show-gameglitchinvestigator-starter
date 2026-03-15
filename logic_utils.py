# def get_range_for_difficulty(difficulty: str):
#     """Return (low, high) inclusive range for a given difficulty."""
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIX: Was 1-50 in the original; should be 1-500 for Hard mode.
        return 1, 500
    return 1, 100

# def parse_guess(raw: str):
#     """
#     Parse user input into an int guess.

#     Returns: (ok: bool, guess_int: int | None, error_message: str | None)
#     """
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# def check_guess(guess, secret):
#     """
#     Compare guess to secret and return (outcome, message).

#     outcome examples: "Win", "Too High", "Too Low"
#     """
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

def check_guess(guess, secret):
    """Compare guess to secret and return outcome string."""
    # FIX: Original returned (outcome, message) tuple with swapped hint messages.
    # Refactored to return only the outcome; message handled separately in app.py.
    if guess == secret:
        return "Win"

    if guess < secret:
        return "Too Low"
    else:
        return "Too High"


# def update_score(current_score: int, outcome: str, attempt_number: int):
#     """Update score based on outcome and attempt number."""
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: Original code added +5 for "Too High" on even attempts instead of
    # consistently penalizing -5. Unified to always subtract 5 on a wrong guess.
    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5

    return current_score
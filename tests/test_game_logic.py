"""
Tests for logic_utils.py — verifies that all game logic functions
behave correctly after bug fixes.
"""

from logic_utils import (
    check_guess,
    parse_guess,
    update_score,
    get_range_for_difficulty,
)


# ───────────────────── check_guess ─────────────────────

def test_winning_guess():
    """If the secret is 50 and guess is 50, it should be a win."""
    assert check_guess(50, 50) == "Win"


def test_guess_too_high():
    """If secret is 50 and guess is 60, hint should be 'Too High'."""
    assert check_guess(60, 50) == "Too High"


def test_guess_too_low():
    """If secret is 50 and guess is 40, hint should be 'Too Low'."""
    assert check_guess(40, 50) == "Too Low"


def test_guess_off_by_one_high():
    """Guess is exactly one above the secret."""
    assert check_guess(51, 50) == "Too High"


def test_guess_off_by_one_low():
    """Guess is exactly one below the secret."""
    assert check_guess(49, 50) == "Too Low"


# ───────────────────── parse_guess ─────────────────────

def test_parse_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None


def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None
    assert "Enter a guess" in err


def test_parse_none():
    ok, val, err = parse_guess(None)
    assert ok is False
    assert val is None
    assert "Enter a guess" in err


def test_parse_non_numeric():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert val is None
    assert "not a number" in err


def test_parse_decimal():
    """Decimal input like '3.7' should be accepted and truncated to 3."""
    ok, val, err = parse_guess("3.7")
    assert ok is True
    assert val == 3
    assert err is None


def test_parse_negative_number():
    """Negative numbers should be accepted."""
    ok, val, err = parse_guess("-5")
    assert ok is True
    assert val == -5
    assert err is None


def test_parse_very_large_number():
    """Very large numbers should be accepted."""
    ok, val, err = parse_guess("999999")
    assert ok is True
    assert val == 999999


# ───────────────────── update_score ─────────────────────

def test_score_win_first_attempt():
    """Win on attempt 1 should award 100 - 10*(1+1) = 80 points."""
    assert update_score(0, "Win", 1) == 80


def test_score_win_late_attempt():
    """Win on attempt 9 — points = 100 - 10*10 = 0, floored to 10."""
    assert update_score(0, "Win", 9) == 10


def test_score_penalty_too_high():
    """'Too High' should subtract 5 points."""
    assert update_score(50, "Too High", 2) == 45


def test_score_penalty_too_low():
    """'Too Low' should subtract 5 points."""
    assert update_score(50, "Too Low", 3) == 45


def test_score_penalty_even_attempt():
    """'Too High' on an even attempt should STILL subtract 5 (bug was +5)."""
    assert update_score(50, "Too High", 4) == 45


# ───────────────────── get_range_for_difficulty ─────────────────────

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_range_hard():
    """Hard range should be 1-500, not 1-50 (original bug)."""
    assert get_range_for_difficulty("Hard") == (1, 500)


def test_range_unknown_fallback():
    """Unknown difficulty should fall back to Normal range (1-100)."""
    assert get_range_for_difficulty("Unknown") == (1, 100)

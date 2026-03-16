# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  1. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  **bugs:**
  1. higher/lower suggestion is broken (shows opposite)
  2. the secret keeps changing
    the code was converting secret to string on even-numbered attempts
  3. no restriction to only use a value within 1-100
  4. "New Game" button doesn't work when you win
    it keeps saying that "You already won. Start a new game to play again."
  5. the difficulty=Hard range is set to 1-50 instead of 500
  6. adding 5 points for every even number of attempts
  7. the attems starts with 1 instead of 0
  8. refactoring needed from app to logic_utils
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  1. Copilog
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  1. The AI suggested that I change f"Guess a number between {low} and {high}. " it was between 1 and 100.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  it suggested that i return "Win", "Too high" and "Too low" instead of tuples for the check_guess, but that breaks the program because in app.py, we are expecting a tuple to show message

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  1. running the test + playing the game
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
  1. to understand why one of the tests was not working. it is useful to use the "Ask" option instead of "Agent" so that i get to fix bugs myself

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  1. On every even-numbered attempt, the code ran `secret = str(st.session_state.secret)`, converting the secret from an integer to a string. That meant the comparison between the user's integer guess and the string secret almost always failed, and the hint messages didn't make sense. It effectively made the secret "invisible" on even turns.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  1. Every time you click a button or type something in Streamlit, the *entire* Python script reruns from top to bottom. If you store a variable the normal way (like `secret = 42`), it gets wiped and regenerated on every click. `st.session_state` is Streamlit's way of keeping data alive across those reruns — think of it like a small dictionary that survives each page reload. That's why you wrap your initial values in `if "key" not in st.session_state:` — so they only get set once, the first time the script runs, and stay stable after that.

- What change did you make that finally gave the game a stable secret number?
  1. I removed the `if st.session_state.attempts % 2 == 0: secret = str(...)` block entirely and replaced it with a simple `secret = st.session_state.secret`. This ensured the secret stayed as an integer on every attempt. The `st.session_state` was already doing its job of keeping the secret stable — the bug was in how we *read* it, not how we stored it.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Writing specific pytest cases *immediately* after fixing a bug. For example, after fixing the "Too High" hint, I wrote a test that checks `check_guess(60, 50) == "Too High"`. Having that test in place means I can confidently refactor later without worrying about regressions. This "fix it, test it" loop is something I want to keep doing.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I would use the "Ask" mode more often to understand the code *before* letting the AI change it. In this project I sometimes used Agent mode too early and had to undo changes because the AI made too many edits at once. Next time, I'll ask for an explanation first, form my own plan, and only then let the AI make targeted edits.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI-generated code can look confident and clean but still contain subtle logic bugs — like the swapped hint messages or the sneaky `str()` conversion. This project taught me to always verify AI output by running the app and writing tests, rather than trusting that it works just because the code "looks right."

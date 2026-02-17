import random
import os
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    CYAN    = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE   = "\033[97m"
    DIM     = "\033[2m"

def colorize(text, *colors):
    return "".join(colors) + text + Color.RESET

CHOICE_MAP = {"s": 1, "w": -1, "g": 0}
NAME_MAP   = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}
VALID_KEYS = list(CHOICE_MAP.keys())

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print(colorize("╔══════════════════════════════════════╗", Color.CYAN, Color.BOLD))
    print(colorize("║      🐍  SNAKE · WATER · GUN  🔫     ║", Color.CYAN, Color.BOLD))
    print(colorize("╚══════════════════════════════════════╝", Color.CYAN, Color.BOLD))
    print()

def print_rules():
    print(colorize("  RULES:", Color.YELLOW, Color.BOLD))
    print(colorize("  • Snake   drinks  Water  → Snake wins", Color.DIM + Color.WHITE))
    print(colorize("  • Water   douses  Gun    → Water wins", Color.DIM + Color.WHITE))
    print(colorize("  • Gun     shoots  Snake  → Gun wins", Color.DIM + Color.WHITE))
    print()

def print_scoreboard(scores, round_num, total_rounds):
    print(colorize(f"  Round {round_num}/{total_rounds}", Color.MAGENTA, Color.BOLD))
    print(colorize(
        f"  You: {scores['you']}  |  Computer: {scores['computer']}  |  Ties: {scores['ties']}",
        Color.WHITE
    ))
    print(colorize("  ──────────────────────────────────────", Color.DIM))
    print()

def get_player_choice():
    while True:
        raw = input(
            colorize("  Your choice ", Color.WHITE) +
            colorize("[s]nake", Color.GREEN) +
            colorize(" / ", Color.DIM) +
            colorize("[w]ater", Color.CYAN) +
            colorize(" / ", Color.DIM) +
            colorize("[g]un", Color.RED) +
            colorize(": ", Color.WHITE)
        ).strip().lower()

        if raw in VALID_KEYS:
            return CHOICE_MAP[raw]

        print(colorize(
            f"  ⚠  Invalid input '{raw}'. Please enter s, w, or g.\n",
            Color.YELLOW
        ))
def determine_result(you, computer):
    if you == computer:
        return "tie"
    winning_combos = {(1, -1), (0, 1), (-1, 0)}   # (you, computer) → you win
    return "win" if (you, computer) in winning_combos else "lose"

def play_round(scores, round_num, total_rounds):
    print()
    print_scoreboard(scores, round_num, total_rounds)

    you      = get_player_choice()
    computer = random.choice(list(CHOICE_MAP.values()))

    print()
    print(colorize(f"  You chose   : {NAME_MAP[you]}", Color.CYAN, Color.BOLD))
    print(colorize(f"  Computer    : {NAME_MAP[computer]}", Color.MAGENTA, Color.BOLD))
    print()

    result = determine_result(you, computer)

    if result == "tie":
        scores["ties"] += 1
        print(colorize("  🤝  It's a tie!", Color.YELLOW, Color.BOLD))
    elif result == "win":
        scores["you"] += 1
        print(colorize("  🎉  You win this round!", Color.GREEN, Color.BOLD))
    else:
        scores["computer"] += 1
        print(colorize("  💀  Computer wins this round!", Color.RED, Color.BOLD))

    print()
    input(colorize("  Press Enter to continue...", Color.DIM))

def print_summary(scores, total_rounds):
    clear()
    print_banner()
    print(colorize("  ══ FINAL RESULTS ══", Color.YELLOW, Color.BOLD))
    print()
    print(colorize(f"  Rounds played : {total_rounds}", Color.WHITE))
    print(colorize(f"  Your wins     : {scores['you']}", Color.GREEN, Color.BOLD))
    print(colorize(f"  Computer wins : {scores['computer']}", Color.RED, Color.BOLD))
    print(colorize(f"  Ties          : {scores['ties']}", Color.YELLOW))
    print()

    if scores["you"] > scores["computer"]:
        print(colorize("  🏆  CONGRATULATIONS — You won the match!", Color.GREEN, Color.BOLD))
    elif scores["computer"] > scores["you"]:
        print(colorize("  🤖  Computer wins the match. Better luck next time!", Color.RED, Color.BOLD))
    else:
        print(colorize("  🤝  The match ends in a draw!", Color.YELLOW, Color.BOLD))

    print()

def get_rounds():
    while True:
        try:
            n = int(input(colorize("  How many rounds? (1–10): ", Color.WHITE)).strip())
            if 1 <= n <= 10:
                return n
            print(colorize("  ⚠  Please enter a number between 1 and 10.\n", Color.YELLOW))
        except ValueError:
            print(colorize("  ⚠  That doesn't look like a number. Try again.\n", Color.YELLOW))

def main():
    clear()
    print_banner()
    print_rules()

    total_rounds = get_rounds()
    scores = {"you": 0, "computer": 0, "ties": 0}

    for round_num in range(1, total_rounds + 1):
        clear()
        print_banner()
        play_round(scores, round_num, total_rounds)

    print_summary(scores, total_rounds)

    again = input(colorize("  Play again? [y/n]: ", Color.CYAN)).strip().lower()
    if again == "y":
        main()
    else:
        print(colorize("\n  Thanks for playing! 👋\n", Color.CYAN, Color.BOLD))

if __name__ == "__main__":
    main()

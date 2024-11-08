# Predicting the 2024 election with odds from Polymarket on 2 November, by means
# of Monte Carlo simulation.

import random

SIMULATIONS = 1_000_000
TRUMP_WIN_ELECTORAL_THRESHOLD = 51

trump_win_count = 0

class SwingState:
    def __init__(self, name, electoral_votes, chance_trump_win):
        self.name = name
        self.electoral_votes = electoral_votes
        self.chance_trump_win = chance_trump_win

    def simulate(self):
        return random.random() < self.chance_trump_win

# Polymarket odds per state, 2 November 2024, 08:00
swing_states = [
    SwingState("Pennsylvania", 19, 0.565),
    SwingState("North Carolina", 16, 0.69),
    SwingState("Nevada", 6, 0.645),
    SwingState("Arizona", 11, 0.75),
    SwingState("Wisconsin", 10, 0.49),
    SwingState("Michigan", 15, 0.425),
    SwingState("Georgia", 16, 0.715),
]

for i in range(SIMULATIONS):
    total_electoral_votes = sum(state.electoral_votes for state in swing_states if state.simulate())
    if total_electoral_votes >= TRUMP_WIN_ELECTORAL_THRESHOLD:
        trump_win_count += 1

print("Candidate\tWon\t\tTotal\t\tPercentage")
print(f"Trump\t\t{trump_win_count:,}\t\t{SIMULATIONS:,}\t{(trump_win_count / SIMULATIONS * 100):.2f}%")
print(f"Harris\t\t{SIMULATIONS - trump_win_count:,}\t\t{SIMULATIONS:,}\t{((SIMULATIONS - trump_win_count) / SIMULATIONS * 100):.2f}%")

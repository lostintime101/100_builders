import random
import matplotlib.pyplot as plt
import numpy as np

none = [0, 0]
low = [-10, 10]
mid = [-30, 30]
high = [-55, 55]
degenerate = [-90, 90]


"""

This script simulates the airdrop randomness levels.

-- IMPORTANT --
This script is included for reference but to reduce bloat matplotlib and numpy libraries are NOT included in requirements.txt
If you wish to run this script, do so in a fresh virtual environment with those dependencies installed.

"""

# Initialize lists to store winnings
winnings_list = []

for _ in range(10_000):
    tokens = 10
    players = 10
    curr_players = 10

    # Initialize a list to store winnings for this round
    round_winnings = []

    for i in range(1, players + 1):
        winnings = round(tokens / curr_players, 4)
        winnings = round(winnings + winnings * (random.randint(-30, 30) / 100), 4)
        round_winnings.append(winnings)
        tokens -= winnings
        curr_players -= 1

    # Append the round winnings to the main list
    winnings_list.extend(round_winnings)

# Calculate mean and standard deviation of winnings
mean_winnings = np.mean(winnings_list)
std_deviation = np.std(winnings_list)

# Create a histogram of the winnings
plt.hist(winnings_list, bins=30, density=True, alpha=0.75, color='b')
plt.xlabel('Winnings')
plt.ylabel('Frequency')
plt.title('NONE')

# Add vertical lines for 1, 2, and 3 standard deviations from the mean
plt.axvline(mean_winnings - std_deviation, color='r', linestyle='dashed', linewidth=2, label='-1 Std Dev')
plt.axvline(mean_winnings, color='g', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(mean_winnings + std_deviation, color='b', linestyle='dashed', linewidth=2, label='+1 Std Dev')
plt.axvline(mean_winnings + 2 * std_deviation, color='m', linestyle='dashed', linewidth=2, label='+2 Std Dev')
plt.axvline(mean_winnings + 3 * std_deviation, color='c', linestyle='dashed', linewidth=2, label='+3 Std Dev')

plt.grid(True)
plt.legend()
plt.show()

import random

#input here
players = []
letters = []
matches = []

player_assignment = {}
for letter in letters:
    random_player = random.choice(players)
    player_assignment[letter] = random_player
    players.remove(random_player)


matches_changed = []

for match in matches:
    new_match = []
    for letter in match:
        new_match.append(player_assignment[letter])
    matches_changed.append(new_match)

print('\n', 'Player Assignment :', '\n', player_assignment, '\n')

for match in matches_changed:
    print(match)

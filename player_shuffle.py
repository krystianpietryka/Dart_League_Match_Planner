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

print('\n', 'Player Assignment :', '\n')
for letter in player_assignment:
    print(letter, ':', player_assignment[letter])

counter = 0
print('\n')
for match in matches_changed:
    counter += 1
    print(counter, ' '.join(match))
print('\n')

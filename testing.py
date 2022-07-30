import copy

matches = [[0, 5, 8, 9], [0, 1, 5, 7], [3, 6, 7, 8], [2, 5, 6, 7], [1, 3, 7, 9], [1, 2, 6, 9], [0, 1, 6, 8], [4, 7, 8, 9], [2, 3, 5, 8], [0, 2, 4, 7], [0, 2, 3, 9], [4, 5, 6, 9], [1, 3, 4, 5], [0, 3, 4, 6], [1, 2, 4, 8]]
mapping = {0:'A', 1:'B', 2:'C',3:'D',4:'E',5:'F', 6:'G',7:'H',8:'I',9:'J'}

matches_mapped = []

for match in matches:
    temp_list = []
    for player in match:
        temp_list.append(mapping[player])
    matches_mapped.append(temp_list)

print(matches_mapped)
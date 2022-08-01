from itertools import combinations
from teams_combination import teams
import copy
import random
import PySimpleGUI as sg


def Create_Pairs():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    pairs_temp = []
    pairs = []

    #cartesian product of numbers
    for i in range(10):
        for j in range(10):
            pairs_temp.append((numbers[i], numbers[j]))

    #exclude duplicates and reverse duplicates
    for pair in pairs_temp:
        if pair[0] != pair[1]:
            if (pair[1], pair[0]) not in pairs:
                pairs.append(pair)
    return pairs

#   Loop over every team, add the combination of pairs to temp pair count,
#   if any pair combination makes the count > 2, dont add this team
def Create_Matches():

    matches = []

    pairs_count = {}
    for pair in pairs:
            pairs_count[pair] = 0

    for team in teams:
        good_flag = 1

        temp_pairs_count = copy.deepcopy(pairs_count)
        list_combinations = list(combinations(team, 2))

        for combination in list_combinations:
            if temp_pairs_count[combination] < 2:
                temp_pairs_count[combination] += 1
            else:
                good_flag = 0
                break
        if good_flag == 1:
            matches.append(team)
            pairs_count = copy.deepcopy(temp_pairs_count)
    return matches
  
#checks if pairs count of returned matches configuration is valid (count = 2)
def Validity_Check(matches):
    pairs_count = {}
    valid_flag = 1

    for pair in pairs:
            pairs_count[pair] = 0

    for match in matches:
        list_combinations = combinations(match, 2)
        for combination in list_combinations:
            pairs_count[combination] += 1
    
    print(pairs_count)

    for value in pairs_count.values():
        if value != 2:
            valid_flag = 0
            break
    return valid_flag

def Numbers_To_Letters(matches):
    mapping = {0:'A', 1:'B', 2:'C',3:'D',4:'E',5:'F', 6:'G',7:'H',8:'I',9:'J'}
    matches_mapped = []

    for match in matches:
        temp_list = []
        for player in match:
            temp_list.append(mapping[player])
        matches_mapped.append(temp_list)

    return matches_mapped



def Create_Match_Table():
    #shuffles teams configuration randomly until the process returns valid matches
    matches_valid_flag = 0
    counter = 0


    while matches_valid_flag != 1:

        counter+=1
        print('\n', counter, '\n')

        random.shuffle(teams)

        matches = Create_Matches()

        #print(matches)

        matches_valid_flag = Validity_Check(matches)

    print(Numbers_To_Letters(matches))

#UI
def Intro():
    layout = [[sg.Text('Welcome to Dart League Match Planner!', size=(40, 1))], 
    [sg.Text('Choose parameters and run. This can take a while.', size=(40, 1))],
    [sg.Text('Amount of Players:', size=(35, 1)), sg.Input(key='amount_of_players', enable_events=True)],
    [sg.Text('Matches between player pair:', size=(35, 1)), sg.Input(key='amount_of_pair_matches', enable_events=True)],
    [sg.Button('Run'), sg.Button('Exit')]]
    return sg.Window("Dart_League", layout, finalize=True)


def Created_Matches_Layout():
    col = [[sg.Text(k="-OUTPUT-", size=(20, 50))]]
    layout = [
        [
            sg.Column(
                col,
                size=(150, 600),
                expand_x=True,
                vertical_scroll_only=True,
                justification="center",
                element_justification="center",
                scrollable=True,
            )
        ]
    ]
    return sg.Window("Matches", layout, location=(550, 0), finalize=True)


def main():
    window1, window2 = Intro(), None
    pairs = Create_Pairs()
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:  # if closing win 2, mark as closed
                window2 = None
            elif window == window1:  # if closing win 1, exit program
                break
        # Handling events
        if event == 'Run' and not window2:
            result = Create_Match_Table()
            window2 = Created_Matches_Layout
            window2["-OUTPUT-"].update(result)


if __name__ == "__main__":
    main()




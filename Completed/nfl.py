"""
Prompt the user for either an NFL conference and division or the name of an NFL team.
Based on the response, return either a list of teams in that division or the name of the team's division.

>>> NFL_TEAMS = {'foo':{'bar':['baz']}}

>>> get_teams_by_conference_and_division(NFL_TEAMS, 'foo', 'bar')
['baz']

>>> get_conference_and_division_by_team_name(NFL_TEAMS, 'baz')
('foo', 'bar')
"""


def get_teams_by_conference_and_division(NFL_TEAMS, input_conf, input_division):
    print(NFL_TEAMS[input_conf][input_division])
    return NFL_TEAMS[input_conf][input_division]


def get_conference_and_division_by_team_name(NFL_TEAMS, input_team):

    for conference, division in NFL_TEAMS.items():
        for div, teams in division.items():
            if input_team in teams:
                print(conference, div)



def main(NFL_TEAMS):
    """Prompt for user input, get a result from the data, print a nicely formatted answer"""

    user_input = input('Enter the name of either a conference (AFC or NFC) or team: ')
    if user_input in ("AFC", "NFC"):
        input_conf = user_input
        input_division = input("Which division? ")
        get_teams_by_conference_and_division(NFL_TEAMS, input_conf, input_division)
        #return NFL_TEAMS.items[user_input]

    else:
        # user_input in NFL_TEAMS.items():
        input_team = user_input
        get_conference_and_division_by_team_name(NFL_TEAMS, input_team)



if __name__ == '__main__':

    NFL_TEAMS = {
        'AFC': {
            'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
            'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers'],
            'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
            'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
        },
        'NFC': {
            'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
            'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
            'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
            'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']
        }
    }

main(NFL_TEAMS)

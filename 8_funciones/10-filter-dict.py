matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Brazil',
        'home_team_score': 0,
        'away_team_score': 1,
        'home_team_result': 'lose',
    },
    {
        'home_team': 'Argentina',
        'away_team': 'Brazil',
        'home_team_score': 1,
        'away_team_score': 0,
        'home_team_result': 'win',
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Chile',
        'home_team_score': 3,
        'away_team_score': 0,
        'home_team_result': 'win',
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Peru',
        'home_team_score': 2,
        'away_team_score': 2,
        'home_team_result': 'draw',
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Uruguay',
        'home_team_score': 2,
        'away_team_score': 1,
        'home_team_result': 'win',
    }
]

print(matches, '\n')
print(len(matches), '\n')

new_list = list(filter(lambda x: x['home_team_result'] == 'win', matches))

print(new_list, '\n')
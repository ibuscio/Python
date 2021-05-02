import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt


def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

def run():
    nba_teams = teams.get_teams()
    dict_nba_team = one_dict(nba_teams)
    df_teams = pd.DataFrame(dict_nba_team)
    df_teams.head()
    df_nuggets = df_teams[df_teams['nickname'] == 'Nuggets']
    id_nuggets = df_nuggets[['id']].values[0][0]
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_nuggets)
    # Tenemos ahora un número entero que puede usarse para solicitar información sobre los Warriors
    games = gamefinder.get_data_frames()[0]
    games_home = games[games['MATCHUP'] == 'DEN vs. GSW']
    games_away = games[games['MATCHUP'] == 'DEN @ GSW']

    fig, ax = plt.subplots()
    games_away.mean()['PLUS_MINUS']
    games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
    games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
    ax.legend(["away", "home"])
    plt.show()


if __name__=='__main__':
    run()

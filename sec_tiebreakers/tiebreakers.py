from utils import *

import csv

game_data = Util.load_data()

teams = Util.TEAMS
wins = [0 for i in range(len(teams))]
losses = [0 for i in range(len(teams))]

pointsScored = [0 for i in range(len(teams))]
pointsAllowed = [0 for i in range(len(teams))]

relativeEfficiency =  [0 for i in range(len(teams))]

for i in range(len(teams)):
    team = teams[i]
    w, l = Util.get_record(game_data, team)
    wins[i] = w
    losses[i] = l

    ps = Util.get_ave_points_scored(game_data, team)
    pa = Util.get_ave_points_allowed(game_data, team)
    pointsScored[i] = ps
    pointsAllowed[i] = pa

    re = Util.get_relative_efficiency(game_data, team)
    relativeEfficiency[i] = re

headers = ["Team", "Wins", "Losses", "Points Scored", "Points Allowed", "Relative Efficiency"]
rows = zip(teams, wins, losses, pointsScored, pointsAllowed, relativeEfficiency)

with open('standings.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(rows)
    

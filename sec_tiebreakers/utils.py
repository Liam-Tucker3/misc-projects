"""
Author: Liam Tucker
Date: 08/22/2024
Notes: This file contains the utility functions for the SEC Tiebreakers project. It is purposefully written to avoid needing any libraries installed, at the expense of efficiency. (It will only be run on small datasets).
"""

import csv

class Util:

    TEAMS = ["Alabama", "Arkansas", "Auburn", "Florida", "Georgia", "Kentucky", "LSU", "Mississippi State", "Missouri", "Oklahoma", "Ole Miss", "South Carolina", "Tennessee", "Texas", "Texas A&M", "Vanderbilt"]
    CONF_GAMES = 8

    # Using csv instead of pandas to avoid needing to install pandas
    @staticmethod
    def load_data():
        with open("scores.csv", mode='r') as file:
            reader = csv.reader(file)
            # Get the first row as the header (keys for the dictionary)
            headers = next(reader)
            
            # Initialize the dictionary with empty lists for each header
            data_dict = {header: [] for header in headers}
            
            # Populate the dictionary with the rest of the rows
            for row in reader:
                for header, value in zip(headers, row):
                    data_dict[header].append(value)
        
        for i in range(len(data_dict["Home Score"])):
            data_dict["Home Score"][i] = int(data_dict["Home Score"][i])
            data_dict["Away Score"][i] = int(data_dict["Away Score"][i])

        return data_dict

    @staticmethod
    def get_record(data, team):
        wins = 0
        losses = 0
        # print(data)
        for i in range(len(data["Home Team"])):
            if data["Home Team"][i] == team:
                if data["Home Score"][i] > data["Away Score"][i]:
                    wins += 1
                else:
                    losses += 1
            elif data["Away Team"][i] == team:
                if data["Away Score"][i] > data["Home Score"][i]:
                    wins += 1
                else:
                    losses += 1
        return wins, losses

    @staticmethod
    def get_ave_points_scored(data, team):
        total_points = 0
        num_games = 0
        # print(data)
        # print(data["Home Team"])
        # print(len(data["Home Team"]))
        # print("\n\n\n")
        for i in range(len(data["Home Team"])):
            if data["Home Team"][i] == team:
                total_points += data["Home Score"][i]
                num_games += 1
            elif data["Away Team"][i] == team:
                total_points += data["Away Score"][i]
                num_games += 1
        if num_games == 0:
            print(team)
            return 0
        return total_points / num_games

    @staticmethod
    def get_ave_points_allowed(data, team):
        total_points = 0
        num_games = 0
        for i in range(len(data["Home Team"])):
            if data["Home Team"][i] == team:
                total_points += data["Away Score"][i]
                num_games += 1
            elif data["Away Team"][i] == team:
                total_points += data["Home Score"][i]
                num_games += 1
        if num_games == 0:
            print(team)
            return 0
        return total_points / num_games

    @staticmethod
    def get_relative_efficiency(data, team):

        sum_efficiency = 0
        num_games = 0

        for i in range(len(data["Home Team"])):
            if data["Home Team"][i] == team:
                team1_score = data["Home Score"][i]
                team2_score = data["Away Score"][i]
                team2 = data["Away Team"][i]

                team2_ave_scored = Util.get_ave_points_scored(data, team2)
                team2_ave_allowed = Util.get_ave_points_allowed(data, team2)

                off_efficiency = min(100, (team1_score - team2_ave_allowed) / team2_ave_allowed * 100)
                def_efficiency = max(-100, (team2_ave_scored - team2_score) / team2_ave_scored * 100)
                sum_efficiency += (off_efficiency + def_efficiency)
                num_games += 1

            elif data["Away Team"][i] == team:
                team1_score = data["Away Score"][i]
                team2_score = data["Home Score"][i]
                team2 = data["Home Team"][i]

                team2_ave_scored = Util.get_ave_points_scored(data, team2)
                team2_ave_allowed = Util.get_ave_points_allowed(data, team2)

                off_efficiency = min(100, (team1_score - team2_ave_allowed) / team2_ave_allowed * 100)
                def_efficiency = max(-100, (team2_ave_scored - team2_score) / team2_ave_scored * 100)
                sum_efficiency += (off_efficiency + def_efficiency)
                num_games += 1

        return sum_efficiency / num_games
    
    @staticmethod
    def get_sos(data, team)
        
        opp_wins = 0
        opp_loses = 0

        for i in range(len(data["Home Team"])):
            

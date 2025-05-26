#Import Libraries
import pandas as pd
from tabulate import tabulate
import plotly.graph_objects as go
#####NEXT TIME ######
#Clean up script comments and add comments where needed to make sure I fully understand the script
#Add some other features to it and other more in depth functions?

#Steps to import multiple xls files from basketballreference.com
#My GitHub example is set up for Anthony Edwards stats --- https://www.basketball-reference.com/players/e/edwaran01.html

#Only run when you have a new player and new need files --- Will have to manually rename and save files to be csv and not xls files
#After that uncomment the below lines to get the new file to use
# List your Excel filenames


#filenames = [r"C:\Users\leeme\Downloads\sportsref_download (1).csv", r"C:\Users\leeme\Downloads\sportsref_download (2).csv", r"C:\Users\leeme\Downloads\sportsref_download (3).csv", r"C:\Users\leeme\Downloads\sportsref_download (4).csv", r"C:\Users\leeme\Downloads\sportsref_download (5).csv"]

#dfs = [pd.read_csv(fname) for fname in filenames]
#combined = pd.concat(dfs, ignore_index=True)
#combined.to_csv(r"C:\Users\leeme\Downloads\sportsref_combined.csv", index=False)

#print("CSV files combined and saved as sportsref_combined.csv in your Downloads folder.")


#Reads the CSV
df = pd.read_csv('sportsref_combined.csv') # Make sure the file is in the same directory or give full path
#Renames blank column to location to get home vs away games
if 'Unnamed: 5' in df.columns: #After combining the files from above the column to get whether it is an away game or not is labeled as this and we will change it to location
    df.rename(columns={'Unnamed: 5': 'Location'}, inplace=True)


#Global team variable to use in functions
team = input("Enter the team abbreviation you want to analyze: ").strip().upper()

#Calculates the average of a column
def column_avg(df, column_name):

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Convert to numeric, ignore non-numeric values and replaces non numeric values with NaN
    return pd.to_numeric(df[column_name], errors='coerce').mean()

#Gets the losses against one team
def losses_by_team(df, team):
    # Filter games against the specified team
    filtered = df[df['Opp'] == team]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    #Gets the result column where it starts with L to get a loss and gets the total of those
    total_losses = filtered['Result'].str.startswith('L').sum() #Gets count of all Result column that start with L
    return int(total_losses)

#Gets the losses for home games
def losses_by_team_home(df, team):
    # Filter games against the specified team for home games
    filtered = df[(df['Opp'] == team) & (df['Location'] != '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    #Gets the home losses only
    home_losses = filtered['Result'].str.startswith('L').sum()
    return int(home_losses)


#Gets the losses for away games only
def losses_by_team_away(df, team):
    # Filter games against the specified team for away games
    filtered = df[(df['Opp'] == team) & (df['Location'] == '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    #Gets the away losses only
    away_losses = filtered['Result'].str.startswith('L').sum()
    return int(away_losses)


#Gets wins against one team
def wins_by_team(df, team):
    # Filter rows where 'Opp' equals the target team
    filtered = df[df['Opp'] == team]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Sum the 'Result' column in filtered rows to count wins
    total_wins = filtered['Result'].str.startswith('W').sum()

    return total_wins

#Gets wins while playing at home
def wins_by_team_home(df, team):
    # Filter rows where 'Opp' equals the target team
    filtered = df[(df['Opp'] == team) & (df['Location'] != '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Sum the 'Win' column in filtered rows to count wins
    home_wins = filtered['Result'].str.startswith('W').sum()

    return home_wins

#Gets wins while playing away games
def wins_by_team_away(df, team):
    # Filter rows where 'Opp' equals the target team
    filtered = df[(df['Opp'] == team) & (df['Location'] == '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Sum the 'Win' column in filtered rows to count wins
    away_wins = filtered['Result'].str.startswith('W').sum()

    return away_wins

#Gets record against a team
def record_vs_team(wins_by_team, losses_by_team, team):
    wins = wins_by_team(df, team)
    losses = losses_by_team(df , team)
    return f"{wins} - {losses}"
    
    
#Gets away record against 1 team
def away_record_vs_team(wins_by_team_away, losses_by_team_away, team):
    wins = wins_by_team_away(df, team)
    losses = losses_by_team_away(df , team)
    return f"{wins} - {losses}"
    
#Gets home record against 1 tean
def home_record_vs_team(wins_by_team_home, losses_by_team_home, team):
    wins = wins_by_team_home(df, team)
    losses = losses_by_team_home(df , team)
    return f"{wins} - {losses}"

#Gets average stats against 1 team only
def get_avg_vs_1_team(df, column_avg, team):
    filtered_df = df[df['Opp'] == team]

    if filtered_df.empty:
        print(f"No games found against team '{team}'.")
        return

    skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'MP', 'FG%', '3P%', '2P%', 'eFG%', 'FT%' 'GmSc', '+/-']

    averages = {}
    for column in filtered_df.columns:
        if column in skip_columns:
            continue
        averages[column] = column_avg(filtered_df, column)
    
    return averages

#Gets the overall averages for the csv file
def get_ovr_averages(df, column_avg):

    
    skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'MP', 'FG%', '3P%', '2P%', 'eFG%', 'FT%' 'GmSc', '+/-']
    for column in df.columns:
        if column in skip_columns:
            continue  # Skip this iteration, move to next column
        
        averages = {} #Empty dictionary to store overall averages
    for column in df.columns:
        if column in skip_columns:
            continue
        averages[column] = column_avg(df, column)
        #averages.append([column, f"{average:.2f}"]) #Adds the original print statement output to the averages [] list

    #print(f"Averages:")
    #print(tabulate(averages, headers=["Stat", "Average"], tablefmt="fancy_grid"))
    
    return averages

#Gets the maximum value in a column
def column_max(df, column_name):

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    return pd.to_numeric(df[column_name], errors='coerce').max()

#Gets the highest value in one column
def get_column_maxes(df, column_max,team):
   #Gets the highest of one column
   
    filtered_df = df[df['Opp'] == team] #Filters to get just the opp team from the column

    if filtered_df.empty:
        print(f"No games found against team '{team}'.")
        return {}
    skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'MP', 'FG%', '3P%', '2P%', 'eFG%', 'FT%' 'GmSc', '+/-']
    
    maxes = {}
    for column in df.columns:
        if column in skip_columns:
            continue  # Skip this iteration, move to next column
        maxes[column] = column_max(df, column)
    return maxes

#Gets the minimum value of one column
def column_min(df, column_name):
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    return pd.to_numeric(df[column_name], errors='coerce').min()


#Gets all the column minimums
def get_column_minimums(df, column_min,team):
   #Gets the highest of one column
   
    filtered_df = df[df['Opp'] == team] #Filters to get just the opp team from the column

    if filtered_df.empty:
        print(f"No games found against team '{team}'.")
        return {}
    #skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'GmSc', '+/-'] #List the columns you want to skip over here
    skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'MP', 'FG%', '3P%', '2P%', 'eFG%', 'FT%' 'GmSc', '+/-']
    minimums = {}
    for column in df.columns:
        if column in skip_columns:
            continue  # Skip this iteration, move to next column
        minimums[column] = column_min(df, column)
    return minimums


#Prints the graph to view --- Eventually can make this into a different display if needed
def print_graph(df, column_avg, team):
    overall_avgs = get_ovr_averages(df, column_avg)
    team_avgs = get_avg_vs_1_team(df, column_avg, team)
    maximum = get_column_maxes(df, column_max, team)
    minimum = get_column_minimums(df, column_min, team)
    if not team_avgs:
        return  # No data for team, just exit
    
    ovr_record = record_vs_team(wins_by_team, losses_by_team, team)  # Gets ovr record
    home_record = home_record_vs_team(wins_by_team_home, losses_by_team_home, team)  # get home record like "5 - 3" for example
    away_record = away_record_vs_team(wins_by_team_away, losses_by_team_away, team)  # get away record in a string "5 - 3" for example

    table_data = []
    for stat in overall_avgs:
        overall = overall_avgs.get(stat, 999)
        team_avg = team_avgs.get(stat, 999)
        max_stat = maximum.get(stat, 999) #Gets the value if present in the dictionary, if not returns 999
        min_stat = minimum.get(stat, 999) 
        table_data.append([stat, f"{overall:.2f}", f"{team_avg:.2f}", f"{max_stat:.2f}" , f"{min_stat:.2f}",  ovr_record, home_record, away_record])

    headers = ["Stat", "Overall Avg", f"{team} Avg", "Maximum", "Minimum" ,"Overall Record", "Home Record", "Away Record"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
#Example
print_graph(df, column_avg, team) #Prints Overall AVG, Team Against Average, Record against team, max and min against specific team, home and away record against that team


#Plots a bar graph that opens in the browser to view
def plotly_graph(df, column_avg, team):
    #Same logic as console output
    overall_avgs = get_ovr_averages(df, column_avg)
    team_avgs = get_avg_vs_1_team(df, column_avg, team)
    maximum = get_column_maxes(df, column_max, team)
    minimum = get_column_minimums(df, column_min, team)
    ovr_record = record_vs_team(wins_by_team, losses_by_team, team)  # Gets ovr record
    home_record = home_record_vs_team(wins_by_team_home, losses_by_team_home, team)  # get home record like "5 - 3" for example
    away_record = away_record_vs_team(wins_by_team_away, losses_by_team_away, team)  # get away record in a string "5 - 3" for example

    exclude_columns = ["Gcar", "Gtm", "GmSc", "Location", "Opp", "Result"] #Excludes these columns for the graph
    stats = [stat for stat in overall_avgs.keys() if stat not in exclude_columns]
    
    fig = go.Figure(data=[
        go.Bar(name='Overall Avg', x=stats, y=[overall_avgs.get(stat, 999) for stat in stats]),
        go.Bar(name=f'{team} Avg', x=stats, y=[team_avgs.get(stat, 999) for stat in stats]),
        go.Bar(name=f'Max vs {team}', x=stats, y=[maximum.get(stat, 999) for stat in stats]),
        go.Bar(name=f'Min vs {team}', x=stats, y=[minimum.get(stat, 999) for stat in stats]),
       # go.Bar(name='Overall Record', x=stats, y=[ovr_record.get(stat, 999) for stat in stats]),
       # go.Bar(name='Home Record', x=stats, y=[home_record.get(stat, 999) for stat in stats]),
       # go.Bar(name='Away Record', x=stats, y=[away_record.get(stat, 999) for stat in stats]),
    ])

    fig.update_layout(
        title=f'Performance Comparison vs {team} Record: Overall Record: {ovr_record} Home Record: {home_record} Away Record: {away_record}',
        xaxis_title='Stat',
        yaxis_title='Value',
        yaxis=dict(dtick=5), # Y Axis increments by 5
        barmode='group'
    )

    fig.show()
    
plotly_graph(df,column_avg, team)



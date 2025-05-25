#Import Libraries
import pandas as pd
from tabulate import tabulate

#####NEXT TIME ######

#Work on cleaning up the CSV without manual intervention - Got the adding location in line 22, need something to delete the last line from the csv as well
#And then also something to make the CSV auto upload to the correct destination for us to use/ able to use script parameters to use it for another player 
#Clean up script comments and add comments where needed

#Look into updating win loss function to be able to get point differential and not just win or loss

#Get more realistic data into a CSV somehow after that to use for next NBA year# 

#input("Enter to continue:") #Add this wherever to add a pause for testing

#Upload CSV 
#df is for dataframe and is the standard that pandas uses

#df = pd.read_csv('michael-jordan-nba-career-regular-season-stats-by-game.csv') # Make sure the file is in the same directory or give full path
df = pd.read_csv('sportsref_download.csv') # Make sure the file is in the same directory or give full path
#Renames blank column to location to get home vs away games
if '' in df.columns:
    df.rename(columns={'': 'Location'}, inplace=True)

team = input("Enter the team abbreviation you want to analyze: ").strip().upper()

#Write how to get the averages for each column that has integers (Overall averages)  --- Function

def column_avg(df, column_name):
    """
    Calculate the average of a specified column in the DataFrame.

    Parameters:
    - df: pandas DataFrame
    - column_name: string, name of the column to average

    Returns:
    - float: average value of the column
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    #return df[column_name].mean()
    # Convert to numeric, ignore non-numeric values
    return pd.to_numeric(df[column_name], errors='coerce').mean()

#Losses vs a certain team

def losses_by_team(df, team):
    # Filter games against the specified team
    filtered = df[df['Opp'] == team]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Count where Win == 0
    #total_losses = (filtered['Win'] == 0).sum()
    total_losses = filtered['Result'].str.startswith('L').sum()
    return int(total_losses)



def losses_by_team_home(df, team):
    # Filter games against the specified team
    filtered = df[(df['Opp'] == team) & (df['Location'] != '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Count where Win == 0
    home_losses = filtered['Result'].str.startswith('L').sum()
    return int(home_losses)



def losses_by_team_away(df, team):
    # Filter games against the specified team
    filtered = df[(df['Opp'] == team) & (df['Location'] == '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Count where Win == 0
    away_losses = filtered['Result'].str.startswith('L').sum()
    return int(away_losses)

'''

#Example

team = input("Enter the opponent team name abbreviation: ")
losses_against_team = losses_by_team(df, team)
print(f"Losses against {team} is {losses_against_team}.")


'''

#Write how to get wins vs a certain team --- Function (count variable since its all 1 or 0) 

def wins_by_team(df, team):
    # Filter rows where 'Opp' equals the target team
    filtered = df[df['Opp'] == team]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Sum the 'Win' column in filtered rows to count wins
    total_wins = filtered['Result'].str.startswith('W').sum()

    return total_wins




def wins_by_team_home(df, team):
    # Filter rows where 'Opp' equals the target team
    filtered = df[(df['Opp'] == team) & (df['Location'] != '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Sum the 'Win' column in filtered rows to count wins
    home_wins = filtered['Result'].str.startswith('W').sum()

    return home_wins



def wins_by_team_away(df, team):
    # Filter rows where 'Opp' equals the target team
    filtered = df[(df['Opp'] == team) & (df['Location'] == '@')]

    if filtered.empty:
        print(f"No games found against team '{team}'.")
        return 0

    # Sum the 'Win' column in filtered rows to count wins
    away_wins = filtered['Result'].str.startswith('W').sum()

    return away_wins


'''
#Example
team = input("Enter the opponent team name abbreviation: ")
wins_against_team = wins_by_team(df, team)
print(f"Wins against {team} is {wins_against_team}.")

'''


#Gets record for a team

def record_vs_team(wins_by_team, losses_by_team, team):
    #team = input("Enter the team abbreviation you want a record against for: ")
    wins = wins_by_team(df, team)
    losses = losses_by_team(df , team)
    return f"{wins} - {losses}"
    #record = f"{wins} - {losses}"  # This is the correct f-string
    #print(f"Record vs {team}: {record}")
    
    
def away_record_vs_team(wins_by_team_away, losses_by_team_away, team):
    #team = input("Enter the team abbreviation you want a record against for: ")
    wins = wins_by_team_away(df, team)
    losses = losses_by_team_away(df , team)
    return f"{wins} - {losses}"
    #record = f"{wins} - {losses}"  # This is the correct f-string
    #print(f"Record vs {team}: {record}")
    
    
def home_record_vs_team(wins_by_team_home, losses_by_team_home, team):
    #team = input("Enter the team abbreviation you want a record against for: ")
    wins = wins_by_team_home(df, team)
    losses = losses_by_team_home(df , team)
    return f"{wins} - {losses}"
    #record = f"{wins} - {losses}"  # This is the correct f-string
    #print(f"Record vs {team}: {record}")

#Example
#record_vs_team(wins_by_team, losses_by_team)
def get_avg_vs_1_team(df, column_avg, team):
    #team = input("Enter the team abbreviation to calculate averages against: ")
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
        #averages.append([column, f"{average:.2f}"]) #Adds the original print statement output to the averages [] list

    #print(f"Averages vs {team}:")
    #print(tabulate(averages, headers=["Stat", "Average"], tablefmt="fancy_grid"))
    
    return averages



#Example
#get_avg_vs_1_team(column_avg)

#Prints total averages for the stats
def get_ovr_averages(df, column_avg):

    #skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'GmSc', '+/-']
    skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'MP', 'FG%', '3P%', '2P%', 'eFG%', 'FT%' 'GmSc', '+/-']
    for column in df.columns:
        if column in skip_columns:
            continue  # Skip this iteration, move to next column
        #average = column_avg(df,column)
       # print(f"Overall Average of {column}: {average:.2f}")
        
        averages = {} #Empty dictionary
    for column in df.columns:
        if column in skip_columns:
            continue
        averages[column] = column_avg(df, column)
        #averages.append([column, f"{average:.2f}"]) #Adds the original print statement output to the averages [] list

    #print(f"Averages:")
    #print(tabulate(averages, headers=["Stat", "Average"], tablefmt="fancy_grid"))
    
    return averages


def column_max(df, column_name):
    """
    Calculate the max of a specified column in the DataFrame.

    Parameters:
    - df: pandas DataFrame
    - column_name: string, name of the column to average

    Returns:
    - float: average value of the column
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    return pd.to_numeric(df[column_name], errors='coerce').max()




def get_column_maxes(df, column_max,team):
   #Gets the highest of one column
   
    filtered_df = df[df['Opp'] == team] #Filters to get just the opp team from the column

    if filtered_df.empty:
        print(f"No games found against team '{team}'.")
        return {}
    #skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'GmSc', '+/-']
    skip_columns = ['Rk', 'Gcar' 'Gtm', 'Date', 'Team', 'GS', 'MP', 'FG%', '3P%', '2P%', 'eFG%', 'FT%' 'GmSc', '+/-']
    
    maxes = {}
    for column in df.columns:
        if column in skip_columns:
            continue  # Skip this iteration, move to next column
        maxes[column] = column_max(df, column)
    return maxes


def column_min(df, column_name):
    """
    Calculate the min of a specified column in the DataFrame.

    Parameters:
    - df: pandas DataFrame
    - column_name: string, name of the column to average

    Returns:
    - float: average value of the column
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    return pd.to_numeric(df[column_name], errors='coerce').min()




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


#Example
#get_ovr_averages()


def print_graph(df, column_avg, team):
    overall_avgs = get_ovr_averages(df, column_avg)
    team_avgs = get_avg_vs_1_team(df, column_avg, team)
    maximum = get_column_maxes(df, column_max, team)
    minimum = get_column_minimums(df, column_min, team)
    if not team_avgs:
        return  # No data for team, just exit
    
    ovr_record = record_vs_team(wins_by_team, losses_by_team, team)  # This works and the column is correct
    home_record = home_record_vs_team(wins_by_team_home, losses_by_team_home, team)  # get record string like "5 - 3"
    away_record = away_record_vs_team(wins_by_team_away, losses_by_team_away, team)  # get record string like "5 - 3"

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
print_graph(df, column_avg, team) #Prints Overall AVG, Team Against Average, Record against team, max and min against specific team


#Menu to select search parameters etc --- Going to get averages vs one team, one year, etc as narrow as you want and then vs averages in general to compare them -- 

'''
name = input("Enter your name (or press Enter to skip): ")

if name:
    print(f"Hello, {name}!")
else:
    print("Hello, guest!")
'''




#Python Functions from other Repo that could be useful -- Going to put here in case we need them for something else

def clean_string(input_string: str) -> str:  #Expects the input to be a string for this to run
    # Remove any leading or trailing whitespace from the input string
    result_string = input_string.strip()
    
    # Return the string with whitespace removed from both ends
    return result_string


def char_frequency(string):
    # Initialize an empty dictionary named 'dict' to store character frequencies.
    dict = {}
    
    # Iterate through each character 'n' in the input string .
    for char in string:
        # Retrieve the keys (unique characters) in the 'dict' dictionary.
        keys = dict.keys() # Key is age: and 26 would be the value so in this case 'a' would be key and occurrences would be value
        
        # Check if the character 'n' is already a key in the dictionary.
        if char in keys:
            # If 'n' is already a key, increment its value (frequency) by 1.
            dict[char] += 1
        else:
            # If 'n' is not a key, add it to the dictionary with a frequency of 1.
            dict[char] = 1
    
    # Return the dictionary containing the frequency of each character in the input string.
    return dict
    
#print (char_frequency("asdfaskdfhaskdfhwieurihfbsiuhweiuhrihs"))
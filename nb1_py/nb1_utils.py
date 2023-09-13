# Extracting Dataframes by Race and calculating Statistics 





def create_race_sub_dataframes(dataframe):
    '''
    Overview: Accepts a dataframe from the insomnia_data and returns a bunch of
    the individual sub dataframes by race using the local variable (to the
    function) race_columns.

    '''
    # List of race column names
    race_columns = ['American_Indian', 'Asian', 'Native_Hawaiian', 'Black', 'White', 'unknown_Race', 'Hispanic', 'NotHispanic']

    # Create a dictionary to store sub DataFrames
    race_sub_dataframes = {}

    # Loop through the race columns
    for race in race_columns:
        # Filter the DataFrame for rows where the race column has a value of 1
        race_df = dataframe[dataframe[race] == 1]

        # Drop columns for the other races in the sub DataFrame
        other_races = [col for col in race_columns if col != race]
        race_df = race_df.drop(columns=other_races)

        # Store the sub DataFrame in the dictionary with the race name as the key
        race_sub_dataframes[race] = race_df

    return race_sub_dataframes


racesdfs=create_race_sub_dataframes(insomnia_data)


def calculate_statistics_for_sub_dataframes(sub_dataframes):
    """
    Calculate various statistics for each sub DataFrame.

    Args:
        sub_dataframes (dict): A dictionary of sub DataFrames, where each key is a race name and each value is a DataFrame.

    Returns:
        dict: A dictionary containing statistics for each sub DataFrame, including mean, median, minimum, and maximum values for numerical columns.
    """
    # Dictionary to store statistics for each sub DataFrame
    statistics = {}

    for race, sub_df in sub_dataframes.items():
        # Calculate statistics for numerical columns in the sub DataFrame
        numerical_columns = sub_df.select_dtypes(include=['int', 'float'])
        stats = {
            'Mean': numerical_columns.mean(),
            'Median': numerical_columns.median(),
            'Minimum': numerical_columns.min(),
            'Maximum': numerical_columns.max()
        }
        
        # Store the statistics in the dictionary with the race name as the key
        statistics[race] = stats

    return statistics


statistics_for_sub_dataframes = calculate_statistics_for_sub_dataframes(racesdfs)

# Now, statistics_for_sub_dataframes contains various statistics for each sub DataFrame.
# You can access and print the statistics like this:
for race, stats in statistics_for_sub_dataframes.items():
    print(f"Statistics for {race}:\n{stats}\n")


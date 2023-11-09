import matplotlib.pyplot as plt
import pandas as pd


# Reading the CSV files.
data = pd.read_csv(
    'C:/Users/USER/Desktop/ADS/Assignment/Dataset/college_wage_premium.csv')
data_study = pd.read_csv(
    'C:/Users/USER/Desktop/ADS/Assignment/Dataset/score_updated.csv')


"""
   Function for plot a linegraph with given data:

    Arguments:
    data: Pandas DataFrame - contains data to be plotted
    x_column: str - column name for the axis
    y_column: str - column name for y axis
    title: title for the line plot
    legend: str - legend for the line plot

    Returns:
    None

    """


def LineGraph(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['year'], data['high_school'],
             marker='o', label='High School Graduates')
    plt.plot(data['year'], data['bachelors_degree'],
             marker='s', label="Bachelor's Degree Holders")
    plt.xlabel('Year')
    plt.ylabel('Number of Graduates')
    plt.title('High School and Bachelor\'s Degree Graduates Over the Years')
    plt.legend()
    plt.show()


"""
   Function for plot a bargraph with given data:

    Arguments:
    data: Pandas DataFrame - contains data to be plotted
    x_column: str - column name for the axis
    y_column: str - column name for y axis
    title: title for the bar graph

    Returns:
    None

    """


def BarGraph(data):
    study_hours = data_study['Hours']
    study_score = data_study['Scores']
    plt.bar(study_hours, study_score)
    plt.xlabel('Hours')
    plt.ylabel('Scores')
    plt.title('Students Scores Based On Hours Of Study')
    plt.legend()
    plt.show()


"""
   Function for plot a Pie graph with given data:

    Arguments:
    data: Pandas DataFrame - contains data to be plotted
    x_column: str - column name for the axis
    y_column: str - column name for y axis
    title: title for the pie graph

    Returns:
    None

    """


def PieGraph(data):
    df_1973 = data[data['year'] == 1973]
    plt.figure(figsize=(8, 4))
    colors = ['#ff9999', '#66b3ff']
    plt.pie(df_1973[['men_bachelors_degree', 'women_bachelors_degree']].values[0], labels=[
            'Men', 'Women'], autopct='%1.1f%%', colors=colors)
    plt.title("Number of Male and Female Bachelor's Degree Holders in 1973")
    plt.show()

    df_2022 = data[data['year'] == 2022]
    plt.figure(figsize=(8, 4))
    colors = ['#ff9999', '#66b3ff']
    plt.pie(df_2022[['men_bachelors_degree', 'women_bachelors_degree',]].values[0], labels=[
            'Men', 'Women'], autopct='%1.1f%%', colors=colors)
    plt.title("Number of Male and Female Bachelor's Degree Holders in 2022")
    plt.show()


# Calling the graphs with data
PieGraph(data)
LineGraph(data)
BarGraph(data)

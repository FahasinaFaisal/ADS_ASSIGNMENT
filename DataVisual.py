import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv('C:/Users/USER/Desktop/ADS/Assignment/Dataset/college_wage_premium.csv')
data_study=pd.read_csv('C:/Users/USER/Desktop/ADS/Assignment/Dataset/score_updated.csv')
# print(data)


def LineGraph(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['year'], data['high_school'], marker='o', label='High School Graduates')
    plt.plot(data['year'], data['bachelors_degree'], marker='s', label="Bachelor's Degree Holders")
    plt.xlabel('Year')
    plt.ylabel('Number of Graduates')
    plt.title('High School and Bachelor\'s Degree Graduates Over the Years')
    plt.legend()
    plt.show()

def BarGraph(data):
    study_hours = data_study['Hours']
    study_score = data_study['Scores']
    plt.bar(study_hours,study_score)
    plt.show()


def PieGraph(data):
    df_1973 = data[data['year'] == 1973]
    plt.figure(figsize=(8, 4))
    colors = ['#ff9999', '#66b3ff']
    plt.pie(df_1973[['men_bachelors_degree', 'women_bachelors_degree']].values[0], labels=['Men', 'Women'], autopct='%1.1f%%', colors=colors)
    plt.title("Number of Male and Female Bachelor's Degree Holders in 1973")
    plt.show()

    df_2022 = data[data['year'] == 2022]
    plt.figure(figsize=(8, 4))
    colors = ['#ff9999', '#66b3ff']
    plt.pie(df_2022[['men_bachelors_degree', 'women_bachelors_degree',]].values[0], labels=['Men', 'Women'], autopct='%1.1f%%', colors=colors)
    plt.title("Number of Male and Female Bachelor's Degree Holders in 2022")
    plt.show()


PieGraph(data)
LineGraph(data)
BarGraph(data)